import os
import tkinter as tk
from tkinter import *
import customtkinter as ctk
import SpotifyRequest as req

#TODO: fix ctk window sizing issues on windows 10 devices


ctk.set_appearance_mode("System")

ctk.set_default_color_theme("blue")

class App(ctk.CTk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.title("Fetcher")
        self.geometry("400x400")

def main():


    token = req.get_token()
    #create window
    top = App()

    prompt = ctk.CTkLabel(top,text="Enter your Spotify UserName or User ID",fg_color="transparent",font=("arial",15))
    prompt.pack(padx = 10)

    
    user_Id = ctk.StringVar()
    entry = ctk.CTkEntry(top,textvariable = user_Id, width = 200)
    entry.pack(padx=20, pady=10)

    #get user button, have them pass their user ID
    submitButton = ctk.CTkButton(top,text="Enter",command=top.quit)
    submitButton.pack()
    top.mainloop()
    userID = user_Id.get()
    
    '''
    send query to spotipy api.
    Returns an array of dictionaries 
    containing playlist info
    More recently played songs will be at the front of the array
    '''
    result = req.search_for_user_playlists(token, userID)
    
    #play array will hold every found playlist
    playList = []
    playDict = {}
    clicked = StringVar()

    clicked.set("--playlists--")

    #create tuple of names of the playlsits
    for item in result:
        playList.append(item["name"])
        playDict.update({item["name"] : item["id"]})
    
    songsList = []
    

    drop = ctk.CTkOptionMenu(master = top ,command = clicked ,values = playList, dynamic_resizing=True)
    drop.pack()
    get_songs = ctk.CTkButton(master = top, text = "Get Songs", command=req.get_playlist_items(token,playDict[drop.get()],songsList))
    get_songs.pack()
    #button to submit selected playlist
    top.mainloop()
    print(songsList[0]["name"])

if __name__ == "__main__":
    main()