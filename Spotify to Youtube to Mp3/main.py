from youtube_search import YoutubeSearch
from spotipy.oauth2 import SpotifyClientCredentials
from pytube import YouTube
from moviepy.editor import *
from jinja2 import Template
import os, json, spotipy

#Get playlist
def get_playlist_to_txt(sp, playlist_URI):
    tracks = []
    next_pages = 10
    results = sp.playlist_tracks(playlist_URI)
    tracks = results['items']
    while results['next']: 
        results = sp.next(results)
        tracks.extend(results['items'])

    urlJsonList = []

    file = open("canciones.txt", 'w')
    i = 1
    for track in tracks:
        track_name = track["track"]["name"]
        artist_name = track["track"]["artists"][0]["name"]
        print(artist_name + ' - ' + track_name)
        results_dict = json.loads(YoutubeSearch((artist_name + ' ' + track_name)).to_json())
        dic = results_dict['videos']
        if i == 1:
            file.write('https://www.youtube.com' + dic[0]['url_suffix'])
            i += 1
        else:
            file.write('\n' + 'https://www.youtube.com' + dic[0]['url_suffix'])
    file.close()   

    print("Archivo txt creado")  
    return True

def get_mp3(url):
    output = "mp3"
    nombre = YouTube(url).title
    print("     Cancion:", nombre )
    print("     Comenzando descarga de video...")
    mp4 = YouTube(url).streams.get_highest_resolution().download()
    mp3 = mp4.split(".mp4", 1)[0] + f".{output}"
    

    video_clip = VideoFileClip(mp4)
    audio_clip = video_clip.audio
    print("     Convirtiendo video a mp3...")
    audio_clip.write_audiofile(mp3)

    audio_clip.close()
    video_clip.close()

    os.remove(mp4)
    print("     Video mp4 eliminado.")
    print("     Descarga finalizada con exito!")
    print()
    return True 

def canciones_a_descargar():
    with open("canciones.txt") as archivo:
        return len(archivo.readlines())

if __name__=='__main__':
    #Spotify setup
    cid = "2fe4fd32de64419988cfd0e7fb6e812e"
    secret = "6675fc7579a24e688a71dbda483d768e"
    print("Ingresa la url de la playlist:")
    playlist_LINK = input()

    client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
    playlist_URI = playlist_LINK.split("/")[-1].split("?")[0]
    sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

    #Spotify to YoutubeUrl to Txt
    get_playlist_to_txt(sp, playlist_URI)

    #Youtube to Mp3
    total = canciones_a_descargar()
    restantes = 1
    print("Canciones a descargar: ", canciones_a_descargar())
    print()
    with open("canciones.txt") as archivo:
        for url in archivo:
            while True:
                if get_mp3(url):
                    break
            print("Se descargo cancion: ", restantes, " de ", total)
            print("===========================================================")
            restantes += 1
    print("Descarga finalizada.")
    input()





