import tkinter as tk
import os
import pytube
import tkinter.simpledialog as tks
from tkinter import filedialog


path = ""
app = tk.Tk()


def descarga(video, name, option, path):

    char_nopermitidos = ["'", '"', ":", ",", "|", "/","&","-","_","\\"]
    nombre = ""
    for letra in name:
        if letra not in char_nopermitidos:
            nombre = nombre + letra

    if option == "1":
        if 'itag="22"' in str(video.streams):
            stream = video.streams.get_by_itag(22)
        else:
            stream = video.streams.get_highest_resolution()
    else:
        stream = video.streams.filter(only_audio=True)[1]
    texto = 'Descargando ' + nombre + '...'
    dir1 = tk.Label(interior, text=texto, fg="black", bg="#bcff1f")
    dir1.pack()
    stream.download(filename=nombre)
    if option == "2":
        viejo = path + nombre + ".webm"
        new = path + nombre + ".mp3"
        os.rename(viejo, new)
    dir1 = tk.Label(interior, text="¡Listo!", fg="black", bg="#bcff1f")
    dir1.pack()

def ubicacion():
    for basura in interior.winfo_children():
        basura.destroy()

    path = filedialog.askdirectory(initialdir="/", title="Selecciona una carpeta donde descargar los vídeos...")
    if path != '':
        os.chdir(path)
    dir1 = tk.Label(interior, text="Ubicación de descarga actual:", fg="black", bg="#bcff1f")
    dir1.pack()
    dir2 = tk.Label(interior, text=path, fg="black", bg="#bcff1f")
    dir2.pack()

def dw_playlist():
    opcion = tks.askstring("Opción...", "Descargar vídeo y audio: 1. Descargar solo audio: 2.")
    while opcion != "1" and opcion != "2":
        opcion = tks.askstring("Opción...", "Opción no válida. Descargar vídeos: 1. Descargar solo audio: 2.")
    url = tks.askstring("URL", "Pon la url")
    playlist = pytube.Playlist(url)
    for url in playlist:
        video = pytube.YouTube(url)
        raw_name = video.title
        descarga(video, raw_name, opcion, path)

def dw_vid():
    opcion = tks.askstring("Opción...", "Descargar vídeo y audio: 1. Descargar solo audio: 2.")
    while opcion != "1" and opcion != "2":
        opcion = tks.askstring("Opción...", "Opción no válida. Descargar vídeos: 1. Descargar solo audio: 2.")
    url = tks.askstring("URL", "Pon la url")
    video = pytube.YouTube(url)
    raw_name = video.title
    descarga(video, raw_name, opcion, path)

exterior = tk.Canvas(app, height=700, width=600, bg="orange")
exterior.pack()
interior = tk.Frame(exterior, bg="#bcff1f")
interior.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

des_vid = tk.Button(app, text="Descargar un Vídeo", padx=10,
                    pady=5, fg="magenta", bg="cyan", command=dw_vid)
des_vid.pack()
des_play = tk.Button(app, text="Descargar una Playlist", padx=10,
                    pady=5, fg="black", bg="#FF00FF", command=dw_playlist)
des_play.pack()
des_ub = tk.Button(app, text="Cambiar la ubicación de descarga", padx=10,
                    pady=5, fg="orange", bg="grey", command=ubicacion)
des_ub.pack()

app.mainloop()
