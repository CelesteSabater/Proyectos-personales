import pytube
import os
import time


def descarga(video, name, option, path):

    char_nopermitidos = ["/","&","-","_",":","\\"]
    nombre = ""
    for letra in name:
        if letra not in char_nopermitidos:
            nombre = nombre + letra

    if option == 1:
        if 'itag="22"' in str(video.streams):
            stream = video.streams.get_by_itag(22)
        else:
            stream = video.streams.get_highest_resolution()
    else:
        stream = video.streams.filter(only_audio=True)[1]

    print('Descargando ' + nombre + '...')
    stream.download(filename=nombre)
    if option == 2:
        viejo = path + nombre + ".webm"
        new = path + nombre + ".mp3"
        os.rename(viejo, new)
    print("¡Listo!")


opcion = int(input("Descargar vídeos: 1. Descargar solo audio: 2.\n"))
while opcion != 1 and opcion != 2:
    opcion = int(input("Opción no válida.\n"))
opcion2 = int(input("Descargar vídeo sueltos: 1. Descargar playlist: 2.\n"))
while opcion2 != 1 and opcion2 != 2:
    opcion2 = int(input("Opción no válida.\n"))

path = r'D:\github\Proyectos-personales\YouTube-Downloader' + '\\'

if opcion2 == 1:

    lista_de_descarga = []
    nombres = []

    while True:
        url = input("Pon la url, para parar escribe STOP...\n")
        if url == "STOP":
            break
        video = pytube.YouTube(url)
        lista_de_descarga.append(video)
        nombres.append(video.title)

    for x in range(len(lista_de_descarga)):
        raw_name = nombres[x]
        descarga(lista_de_descarga[x], raw_name, opcion, path)

else:
    url = input("Pon la url de la playlist...\n")
    playlist = pytube.Playlist(url)
    for url in playlist:
        video = pytube.YouTube(url)
        raw_name = video.title
        descarga(video, raw_name, opcion, path)

print("")
print("Gracias por usarme, cerrando automáticamente la venta en 10s...\n")
time.sleep(10)