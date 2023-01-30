from pytube import YouTube
from moviepy.editor import *
from jinja2 import Template
import os, shutil, time


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




