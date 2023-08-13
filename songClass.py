class song():
    
    def __init__(self,name,artists):
        self.name = name
        self.artistList = []
        for artist in artists:
            self.artistList.append(artist["name"])
        
    def getName(self):
        return self.name
    
    def getArtist(self):
        
        return self.artistList
    

    
    