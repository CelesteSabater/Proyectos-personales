import tkinter as tk
import os
import pytube
import tkinter.simpledialog as tks
from tkinter import filedialog


path = ""
app = tk.Tk()
#si quieres sentirte diseñador gráfico toquetea esta basura
c_exterior = "#263D42"
c_interior = "white"
c_button = "#263D42"
c_l_button = "white"
c_l_interior = "black"


#descarga un vídeo y a los audios además le cambia el formato a .mp3, es sencillo
def descarga(video, name, option, path):
    #por algún motivo la puta mierda de pytube crea conflictos si un archivo tiene ciertos carácteres
    #estos sé por seguro que dan error, si encuentras algún otro carácter que falle mándame un mensaje
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
    dir1 = tk.Label(interior, text=texto, fg=c_l_interior, bg=c_interior)
    dir1.pack()
    stream.download(filename=nombre)
    if option == "2":
        viejo = path + nombre + ".webm"
        new = path + nombre + ".mp3"
        os.rename(viejo, new)
    dir1 = tk.Label(interior, text="¡Listo!", fg=c_l_interior, bg=c_interior)
    dir1.pack()

#esta puta mierda lo que hace es que el usuario pueda seleccionar donde se realizarán las descargas
def ubicacion():
    path = filedialog.askdirectory(initialdir="/", title="Selecciona una carpeta donde descargar los vídeos...")
    if path != '':
        os.chdir(path)
        dir1 = tk.Label(interior, text="Ubicación de descarga actual:", fg=c_l_interior, bg=c_interior)
        dir1.pack()
        dir2 = tk.Label(interior, text=path, fg=c_l_interior, bg=c_interior)
        dir2.pack()

#descarga una playlist llamando a la primera función
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

#manda un mensaje a la primera función para que haga su thing
def dw_vid():
    opcion = tks.askstring("Opción...", "Descargar vídeo y audio: 1. Descargar solo audio: 2.")
    while opcion != "1" and opcion != "2":
        opcion = tks.askstring("Opción...", "Opción no válida. Descargar vídeos: 1. Descargar solo audio: 2.")
    url = tks.askstring("URL", "Pon la url")
    video = pytube.YouTube(url)
    raw_name = video.title
    descarga(video, raw_name, opcion, path)

#limpia toda la puta mierda innecesaria que hay en pantalla
def limpieza():
    for basura in interior.winfo_children():
        basura.destroy()
    textito_rico = tk.Label(interior, text="Ubicación de descarga actual:", fg=c_l_interior, bg=c_interior)
    textito_rico.pack()
    direcciooooon = tk.Label(interior, text=os.getcwd(), fg=c_l_interior, bg=c_interior)
    direcciooooon.pack()


# https://i0.kym-cdn.com/photos/images/facebook/001/018/866/e44.png
exterior = tk.Canvas(app, height=700, width=600, bg=c_exterior)
exterior.pack()
interior = tk.Frame(exterior, bg=c_interior)
interior.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

#                                                        ____________
#                                  (`-..________....---''  ____..._.-`
#                                   \\`._______.._,.---'''     ,'
#        No toques el                ; )`.      __..-'`-.      /
#       código de abajo             / /     _.-' _,.;;._ `-._,'
#           porfi                  / /   ,-' _.-'  //   ``--._``._
#                               ,','_.-' ,-' _.- (( =-    -. `-._`-._____
#                             ,;.''__..-'   _..--.\\.--'````--.._``-.`-._`.
#              _          |\,' .-''        ```-'`---'`-...__,._  ``-.`-.`-.`.
#   _     _.-,'(__)\__)\-'' `     ___  .          `     \      `--._
# ,',)---' /|)          `     `      ``-.   `     /     /     `     `-.
# \_____--.  '`  `               __..-.  \     . (   < _...-----..._   `.
#  \_,--..__. \\ .-`.\----'';``,..-.__ \  \      ,`_. `.,-'`--'`---''`.  )
#            `.\`.\  `_.-..' ,'   _,-..'  /..,-''(, ,' ; ( _______`___..'__
#                    ((,(,__(    ((,(,__,'  ``'-- `'`.(\  `.,..______
#                                                       ``--------..._``--.__


textito_rico = tk.Label(interior, text="Ubicación de descarga actual:", fg=c_l_interior, bg=c_interior)
textito_rico.pack()
direcciooooon = tk.Label(interior, text=os.getcwd(), fg=c_l_interior, bg=c_interior)
direcciooooon.pack()

limpiar = tk.Button(app, text="Limpiar texto de arriba", padx=10,
                    pady=5, fg=c_l_button, bg=c_button, command=limpieza)
limpiar.pack()

des_ub = tk.Button(app, text="Cambiar la ubicación de descarga", padx=10,
                    pady=5, fg=c_l_button, bg=c_button, command=ubicacion)
des_ub.pack()

des_vid = tk.Button(app, text="Descargar un Vídeo", padx=10,
                    pady=5, fg=c_l_button, bg=c_button, command=dw_vid)
des_vid.pack()

des_play = tk.Button(app, text="Descargar una Playlist", padx=10,
                    pady=5, fg=c_l_button, bg=c_button, command=dw_playlist)
des_play.pack()


app.mainloop()
