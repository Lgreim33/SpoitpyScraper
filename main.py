import os
from dotenv import load_dotenv
import base64
import json
from requests import post,get
import tkinter as tk
from tkinter import *
import customtkinter as CTk
import SpotifyRequest

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret =os.getenv("CLIENT_SECRET")

#get user token 
def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes),"utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = post(url,headers=headers,data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

#get list of user playlist
def search_for_user_playlists(token,user_id):
    url = f"https://api.spotify.com/v1/users/{user_id}/playlists"
    headers = get_auth_header(token)
    
    result = get(url,headers=headers)
    json_result = json.loads(result.content)["items"]
    
    if(len(json_result) == 0):
        print(f"{user_id} has no playlists")
        return None
    
    return json_result

#creates the window to fetch user info
def getUserInfo():
    top = tk.Tk()
    top.title("Fido")
    top.geometry("400x400")
    w = tk.Text(top,height=2, width=40)
    w.tag_configure("tag_name", justify='center')
    w.insert(tk.END, "Enter your Spotify UserName or User ID")
    w.tag_add("tag_name", "1.0", "end")
    w.pack()
    return top





def main():

    token = get_token()
    #create window
    top = getUserInfo()

    user_Id = tk.StringVar()
    entry = Entry(top,textvariable = user_Id, width = 20)
    entry.pack()

    #get user button, have them pass their user ID
    submitButton = tk.Button(top,text="Enter",command=top.quit)
    submitButton.pack()
    tk.mainloop()
    userID = user_Id.get()
    print(userID)
    
    '''
    send query to spotipy api.
    Returns an array of dictionaries 
    containing playlist info
    More recently played songs will be at the front of the array
    '''
    result = search_for_user_playlists(token, userID)

    print(result[0]["name"])

if __name__ == "__main__":
    main()