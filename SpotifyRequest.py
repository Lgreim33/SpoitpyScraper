import os
from dotenv import load_dotenv
import base64
import json
from requests import post,get




#get user token 
def get_token():   
         
    load_dotenv()
    client_id = os.getenv("CLIENT_ID")
    client_secret =os.getenv("CLIENT_SECRET")
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

#get list of user playlist,store in result
def search_for_user_playlists(token,user_id):
    url = f"https://api.spotify.com/v1/users/{user_id}/playlists"
    headers = get_auth_header(token)
    
    result = get(url,headers=headers)
    json_result = json.loads(result.content)["items"]
    
    if(len(json_result) == 0):
        return None
    
    return json_result

def get_playlist_items(token,playlist_id,songList):
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
    headers = get_auth_header(token)

    result = get(url,headers = headers)
    json_result = json.loads(result.content)["items"]

    if(len(json_result) == 0):
        songList = None
        return
    
    for item in json_result:
        songList.append(item["track"])
    return

