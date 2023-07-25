import os
from dotenv import load_dotenv
import base64
import json
from requests import post,get
import tkinter as tk
from tkinter import *
import customtkinter as ctk
import SpotifyRequest as req

ctk.set_appearance_mode("System")

ctk.set_default_color_theme("blue")

class App(ctk.CTk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.title("Fetcher")
        self.geometry("400x400")

#creates the window to fetch user info
def getUserInfoWindow():
    top = tk.Tk()
    top.title("Fido")
    top.frame()
    #background color set to dark grey
    top.configure(bg = '#1e1d21')
    top.geometry("400x400")

    return top



def main():


    token = req.get_token()
    #create window
    top = App()

    w = tk.Text(top,height=2, width=40)
    w.tag_configure("tag_name", justify='center')
    w.insert(tk.END, "Enter your Spotify UserName or User ID")
    w.tag_add("tag_name", "1.0", "end")
    w.pack()
    
    user_Id = tk.StringVar()
    entry = Entry(top,textvariable = user_Id, width = 20)
    entry.pack()

    #get user button, have them pass their user ID
    submitButton = tk.Button(top,text="Enter",command=top.quit)
    submitButton.pack()
    top.mainloop()
    userID = user_Id.get()
    print(userID)
    
    '''
    send query to spotipy api.
    Returns an array of dictionaries 
    containing playlist info
    More recently played songs will be at the front of the array
    '''
    result = req.search_for_user_playlists(token, userID)
    
    playArray = []
    clicked = StringVar()

    clicked.set("--playlist--")

    #create tuple of names of the playlsits
    for playlist in result:
        playArray.append(playlist["name"])
    

    drop = OptionMenu(top ,clicked ,*playArray )
    drop.pack()
    top.mainloop()

if __name__ == "__main__":
    main()