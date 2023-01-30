import spotipy
import json
from youtube_search import YoutubeSearch
from spotipy.oauth2 import SpotifyClientCredentials

#Spotify setup
cid = "2fe4fd32de64419988cfd0e7fb6e812e"
secret = "6675fc7579a24e688a71dbda483d768e"
playlist_LINK = "https://open.spotify.com/playlist/4vhuJVte1N0JRZRjthflQj?si=ffcba3cef0494fea"

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
playlist_URI = playlist_LINK.split("/")[-1].split("?")[0]
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

#Get playlist
tracks = []
next_pages = 10
results = sp.playlist_tracks(playlist_URI)
tracks = results['items']
while results['next']: 
    results = sp.next(results)
    tracks.extend(results['items'])

songlist = []

for track in tracks:
    track_name = track["track"]["name"]
    artist_name = track["track"]["artists"][0]["name"]
    songlist.append(artist_name + ' - ' + track_name)

videosSearch = YoutubeSearch(songlist[1]).to_json()

results_dict = json.loads(videosSearch)

file = open("canciones.txt", 'w')
i = 1
for v in results_dict['videos']:
    if i == 1:
        print(v['url_suffix'])
        file.write('https://www.youtube.com' + v['url_suffix'])
        i += 1
    else:
        file.write('\n' + 'https://www.youtube.com' + v['url_suffix'])
file.close()    

input()
