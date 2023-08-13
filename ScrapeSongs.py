import bs4
import requests
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

def main():
    SongList = ["Thats what You Get by Paramore"]
    results = Search_Tube(SongList)
    print(results) 
    return
