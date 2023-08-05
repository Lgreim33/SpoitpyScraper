import customtkinter as ctk
import SpotifyRequest as req
import tkinter as tk
import ScrapeSongs as ScS


ctk.set_appearance_mode("System")

ctk.set_default_color_theme("green")

class App(ctk.CTk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.title("Fetcher")
        self.geometry("400x450")
        
        #ask user for their username
        prompt = ctk.CTkLabel(self,text="Enter your Spotify UserName or User ID",fg_color="transparent",font=("arial",15))
        prompt.pack(padx = 10)
        
class DropMenu(ctk.CTkOptionMenu):
    
    def __init__(self,master,values_list):
        super().__init__(master)
        self.values = values_list
        
        
        
        
class ScrollFrame(ctk.CTkScrollableFrame):
    
    def __init__(self,master,songList,**kwargs):
        super().__init__(master,**kwargs)
        self.configure(width = 250)
        self.grid_columnconfigure(0,weight=1)
        self.checkItems = []
        self.add_Songs(songList)

    def add_Songs(self,songsList): 
        
        #create selection menu of songs to search for
        
        for song in songsList:
            checkbox = ctk.CTkCheckBox(master=self, text=song["name"],variable = ctk.IntVar(self,0),
                                    onvalue= 0, offvalue= 1)
            checkbox.grid(row = len(self.checkItems),column = 0, pady = (0,10),sticky = ctk.W)
            self.checkItems.append(checkbox)

    #pass an empty list to get the list of songs that the user has checked off
    def get_Checked(self,list_of_checked):

        for check_box in self.checkItems:
            if check_box.get() == 0:
                list_of_checked.append(check_box.text)
        

            
            
        

def main():


    #get token
    token = req.get_token()
    #create window
    top = App()


    #entry field for user submission
    user_Id = tk.StringVar()
    entry = ctk.CTkEntry(top,textvariable = user_Id, width = 200)
    entry.pack(padx=20, pady=10)

    
    #get user button, have them pass their user ID
    submitButton = ctk.CTkButton(top,text="Enter",command=top.quit)
    submitButton.pack()
    top.mainloop()
    
   
    
    '''
    send query to spotipy api.
    Returns an array of objects 
    containing playlist info
    '''
    result = req.search_for_user_playlists(token, user_Id.get())

  
    #play array will hold every found playlist
    playDict = {}

    #fill playlist dictionary
    for item in result:
        playDict.update({item["name"] : item["id"]})
    
    songsList = []
    
    #dropdown menu containing playlist names
    drop = ctk.CTkOptionMenu(master = top,values = list(playDict.keys()), dynamic_resizing=True)
    drop.pack(pady = 10)
    
    
    #hitting submit gets songs from the playlist, and adds the items to a list of checkboxes
    get_songs = ctk.CTkButton(master = top, text = "Get Songs", command= lambda:
                              [req.get_playlist_items(token,playDict[drop.get()],songsList),
                               ScrollFrame(top,songsList).pack(pady = 10)])
    get_songs.pack()
    
    
    
    
    
    top.mainloop()




if __name__ == "__main__":
    main()