import pytube

def Search_Tube(SongList):
    results = list()
    for song in SongList:
        s = pytube.Search(song)
        #if we got back any results, go ahead and add the first youtube object to our results list
        if len(s.results) != 0:
            results.append(s.results[0])
    if len(results) == 0:
        return None
    return results


def download_songs(SongList):
    songsToDownload = []
    songsToDownload = Search_Tube(SongList)
    print(songsToDownload)
    
        
    
