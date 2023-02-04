from youtube_search import YoutubeSearch
from spotipy.oauth2 import SpotifyClientCredentials
from pytube import YouTube
from moviepy.editor import *
from jinja2 import Template
import os, json, spotipy, subprocess

#Get playlist
def get_playlist_to_txt(sp, playlist_URI):
    print("Creando archivo txt...", "\n")
    tracks = []
    try:
        results = sp.playlist_tracks(playlist_URI)
    except:
        print("\a")
        print("La URL ingresada no es valida.")
        return False
    tracks = results['items']
    while results['next']: 
        results = sp.next(results)
        tracks.extend(results['items'])

    file = open("canciones.txt", 'w')
    i = 1
    for track in tracks:
        track_name = track["track"]["name"]
        artist_name = track["track"]["artists"][0]["name"]
        results_dict = json.loads(YoutubeSearch((artist_name + ' ' + track_name)).to_json())
        dic = results_dict['videos']
        if i == 1:
            file.write('https://www.youtube.com' + dic[0]['url_suffix'])
            i += 1
        else:
            file.write('\n' + 'https://www.youtube.com' + dic[0]['url_suffix'])
    file.close()   

    print("Archivo txt creado.")  
    return True

def get_mp3(url, omitidas, directorio):
    nombre = YouTube(url).title
    duracion = YouTube(url).length
    print("     Cancion: *", nombre, "\n")
    if duracion > 600:
        print("La cancion tiene una duracion de: ", (duracion//60), " minutos")
        print("¿Deseas continuar con la descarga? S(Si), N(no)")
        ok = input()
        while ok != 'S' and ok != 'N':
            print("Ingresa una respuesta correcta. S(Si), N(no)")
            ok = input()
        if(ok == "N"):
            omitidas.append(nombre)
            print("Descarga omitida.", "\n")
            return False
    print("     Comenzando descarga de cancion...")
    audio_file = YouTube(url).streams.filter(only_audio=True, subtype='mp4').first().download(directorio+"/")
    base, ext = os.path.splitext(audio_file)
    new_file = base + '.mp3'
    try:
        os.rename(audio_file, new_file)
    except:
        print("\a","\n")
        print("La cancion: ",nombre," ya existe")
        return False
    print("     Descarga finalizada con exito!")
    print() 
    return True

def canciones_a_descargar():
    with open("canciones.txt") as archivo:
        return len(archivo.readlines())

if __name__=='__main__':
    #Spotify setup
    print("Ingresa el Client ID")
    # cid = "2fe4fd32de64419988cfd0e7fb6e812e"
    cid = input()
    print("Ingresa el Client Secret ID")
    # secret = "6675fc7579a24e688a71dbda483d768e"
    secret = input()
    print("Ingresa la url de la playlist:", "\n")
    playlist_LINK = input()
    playlist_URI = playlist_LINK.split("/")[-1].split("?")[0]

    client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
    sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
       #Spotify to YoutubeUrl to Txt
    if get_playlist_to_txt(sp, playlist_URI):
        nombreCarpeta = sp.user_playlist(user=None, playlist_id=playlist_URI, fields="name")
        directorio = nombreCarpeta['name']
        print()
        #Youtube to Mp3
        omitidas = []
        total = canciones_a_descargar()
        restantes = 1
        print("Canciones a descargar: ", canciones_a_descargar(), "\n")     
        print("===========================================================", "\n")
        with open("canciones.txt") as archivo:
            for url in archivo:
                try:
                    if get_mp3(url, omitidas, directorio):
                        print("Se descargo cancion: ", restantes, " de ", total, "\n")
                        print("===========================================================", "\n")
                        restantes += 1
                except:
                    os.system('.\error.py')
                    omitidas.append(YouTube(url).title)
        if len(omitidas) > 0:
            print("Se omitio la descarga de:")
            for c in omitidas:
                print("     *",c)
    print()
    print("Programa finalizado.")
    input()





