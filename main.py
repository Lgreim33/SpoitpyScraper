import SpotifyRequest as req
import ScrapeSongs as ScS
from songClass import song
  
def printSongs(songList):
    print("------")
    print("Songs:")
    print("------")
    for i,songs in enumerate(songList):
        print(str(i+1)+".",songs.name)
    return
        
        
        
def removeSong(songList):
    
    while True:
        
        songToRemove = int(input("Enter an integer identifier of the song to remove: "))
        
        if not 1 < songToRemove  <= len(songList):
            print("Invalid Entry")
            continue
        break
    del songList[songToRemove-1]
    return

def downloadSongs(songList):
    
    #TODO get path to save songs to
    
    ScS.download_songs(songList)
    
    return
def main():

    


    while True:
        #ask user for their username    
        userID = input("Enter your Spotify UserName or User ID:\n")
    
    
        #get token
        token = req.get_token()
        
        ''' 
        send query to spotipy api.
        Returns an array of objects 
        containing playlist info
        '''

        playDict = req.search_for_user_playlists(token, userID)
        if playDict == None:
            print(f"No playlists were found for user: {userID}")
            
            
            tryAgain = str(input("Try again?[y/n]: "))
            
            if tryAgain == 'y': 
                continue
            else:
                return
        break
                
                
            
    if(len(playDict) == 0):
        print("\nNo playlists found")
        return
    
    songList = []
    #print list of playlists
    for i,items in enumerate(playDict):
        print(str(i+1)+".",items)
    while True:
        try:
            selectedPlaylist = int(input(f'Pick Playlist to Return(1-{len(playDict)}): '))
        except ValueError:
           print("Please Enter A numerical value")
           continue
       
        if not 1 <= selectedPlaylist <= len(playDict):
            print(f"Please Enter a value between 1 and {len(playDict)}")
            continue
        break

    req.get_playlist_items(token,playDict[list(playDict.keys())[selectedPlaylist-1]],songList)
    
    
    printSongs(songList)
    
    
    #menu for removing songs before fetching
    while True:
        while True:
            print("--------")
            print("Menu")
            print("--------")
            
            try:
                userSelection = int(input("1.Remove Song From List\n2.Fetch Songs\n3.Cancel\n"))
            except ValueError:
                print("Woah, thats not a valid entry! Please enter an integer between 1 and 3")
                continue
            if not 1 <= userSelection <=3 :
                print("Please Select a Valid Option")
                continue
            break
            
        if userSelection == 1:
            removeSong(songList)
            printSongs(songList)
            continue
        elif userSelection == 2:
            downloadSongs(songList)
            break
        elif userSelection == 3:
                return         
    
    


if __name__ == "__main__":
    main()