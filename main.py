import tkinter as tk
from tkinter.filedialog import askopenfilename
import customtkinter as ctk
import SpotifyRequest as req
import tkinter as tk
import ScrapeSongs as ScS
from songClass import song


ctk.set_appearance_mode("System")

ctk.set_default_color_theme("green")


class App(ctk.CTk):

    def __init__(self, title,dimensions, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.title(title)
        self.geometry(dimensions)
        
        
class DropMenu(ctk.CTkOptionMenu):
    
    def __init__(self,master):
        super().__init__(master)
        self.Menu = ctk.CTkOptionMenu(master=master,dynamic_resizing=True)
    
    #will be called after the menu gets created, and after the program gets te list of playlists, but before the menue gets packed
    def add_options(self,value_list):
        self.Menu.configure(values=value_list)
             
        
class ScrollFrame(ctk.CTkScrollableFrame):
    
    def __init__(self,master,**kwargs):
        super().__init__(master,**kwargs)
        self.configure(width = 250)
        self.grid_columnconfigure(0,weight=1)
        self.checkItems = []


    def add_Songs(self,songList): 
        
        #create selection menu of songs to search for
        
        for song in songList:
            checkbox = ctk.CTkCheckBox(master=self, text=song.getName(),variable = ctk.IntVar(self,0),
                                    onvalue= 0, offvalue= 1)
            checkbox.grid(row=len(self.checkItems),column=0, pady=(0,10),sticky=ctk.W)
            self.checkItems.append(checkbox)

    #pass an empty list to get the list of songs that the user has checked off
    def get_Checked(self,list_of_checked):

        for check_box in self.checkItems:
            if check_box.get()==0:
                list_of_checked.append(check_box.text)
         
        

def main():

    
    #get token
    token = req.get_token()
    #create window
    top = App("Fetcher", "400x500")
    pathPop =("")

    #ask user for their username
    prompt = ctk.CTkLabel(top,text="Enter your Spotify UserName or User ID",fg_color="transparent",font=("arial",15))
    prompt.pack(padx=10)
    #entry field for user submission
    user_Id = tk.StringVar()
    entry = ctk.CTkEntry(top,textvariable=user_Id, width=200)
    entry.pack(padx=20, pady=10)


    #get user button, have them pass their user ID
    submitButton = ctk.CTkButton(top,text="Enter",command=lambda:[top.quit(),submitButton.configure(state="disabled")])
    submitButton.pack()
    top.mainloop()

    UserID = user_Id.get()
    
   
    
    '''
    send query to spotipy api.
    Returns an array of objects 
    containing playlist info
    '''

    playDict = req.search_for_user_playlists(token, UserID)


    #create variabe to store song names
    songsList = []
    
    #dropdown menu containing playlist names
    drop = ctk.CTkOptionMenu(master=top, values=list(playDict.keys()), dynamic_resizing=True)
    drop.pack(pady = 10)
    
    SongFrame = ScrollFrame(master=top)
    fetch_button = ctk.CTkButton(master=top,text="Fetch",command = ScS.download_songs(SongFrame.get_Checked()))

    #hitting submit gets songs from the playlist, and adds the items to a list of checkboxes
    get_songs = ctk.CTkButton(master=top, text="Get Songs", command=lambda:
                              [req.get_playlist_items(token,playDict[drop.get()],songsList),
                               SongFrame.add_Songs(songsList),
                               SongFrame.pack(pady=10),
                               fetch_button.pack(pady=10),
                               get_songs.configure(state="disabled")])
    get_songs.pack()

    

    
    top.mainloop()



if __name__ == "__main__":
    main()