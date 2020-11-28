import pytube

opcion = int(input("Descargar vídeos: 1. Descargar solo audio: 2.\n"))
while opcion != 1 and opcion != 2:
    opcion = int(input("Opción no válida.\n"))
opcion2 = int(input("Descargar vídeo sueltos: 1. Descargar playlist: 2.\n"))
while opcion2 != 1 and opcion != 2:
    opcion2 = int(input("Opción no válida.\n"))

if opcion2 == 1:

    lista_de_descarga = []
    nombres = []

    while True:
        url = input("Pon la url, para parar escribe STOP...\n")
        #transformamos video en un objeto con la url que escojamos
        if url == "STOP":
            break
        video = pytube.YouTube(url)
        lista_de_descarga.append(video)
        nombres.append(video.title)

    for x in range(len(lista_de_descarga)):
        if opcion == 1:
            if 'itag="22"' in str(lista_de_descarga[x].streams):
                stream = lista_de_descarga[x].streams.get_by_itag(22)
            else:
                stream = lista_de_descarga[x].streams.get_highest_resolution()
        else:
            stream = lista_de_descarga[x].streams.filter(only_audio=True)[0]
        print('Descargando '+nombres[x]+'...')
        stream.download(filename=nombres[x])
        print("¡Listo!")

else:
    url = input("Pon la url de la playlist...\n")
    playlist = pytube.Playlist(url)
    for url in playlist:
        video = pytube.YouTube(url)
        if opcion == 1:
            if 'itag="22"' in str(video.streams):
                stream = video.streams.get_by_itag(22)
            else:
                stream = video.streams.get_highest_resolution()
        else:
            stream = video.streams.filter(only_audio=True)[1]
        print('Descargando '+video.title+'...')
        stream.download(filename=video.title)
        print("¡Listo!")