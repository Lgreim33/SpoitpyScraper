import SpotifyRequest as req
import ScrapeSongs as ScS
from songClass import song
  
def removeSong():
    return

def downloadSongs():
    return
def main():

    
    #get token
    token = req.get_token()

    #ask user for their username    
    userID = input("Enter your Spotify UserName or User ID:\n")
   
    ''' 
    send query to spotipy api.
    Returns an array of objects 
    containing playlist info
    '''

    playDict = req.search_for_user_playlists(token, userID)
    if playDict == None:
        print(f"No playlists were found for user: {userID}")
    if(len(playDict) == 0):
        print("\nNo playlists found")
        return
    
    songsList = []
    #print list of playlists
    for i,items in enumerate(playDict):
        print(i+1,"."+items)
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

    req.get_playlist_items(token,playDict[list(playDict.keys())[selectedPlaylist-1]],songsList)
    
    
    print("------")
    print("Songs:")
    print("------")
    for songs in songsList:
        print(songs.name)
    
    
    #menu for removing songs before fetching
    
    while True:
        try:
            userSelection = int(input("1.Remove Song From List\n2.Fetch Songs\n3.Quit\n"))
        except ValueError:
            print("Woah, thats not a valid entry! Please enter an integer between 1 and 3")
            continue
        if not 1 <= userSelection <=3 :
            print("Please Select a Valid Option")
            continue
        break
            
    if userSelection == 1:
        removeSong()
    elif userSelection == 2:
        downloadSongs()
    elif userSelection == 3:
            return         
    
    


if __name__ == "__main__":
    main()