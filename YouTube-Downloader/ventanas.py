import tkinter as tk
import os
import pytube
from tkinter import filedialog, Text

app = tk.Tk()

def ubicacion():
    directory = filedialog.askdirectory(initialdir="/", title="Selecciona una carpeta donde descargar los vídeos...")
    if directory != '':
        os.chdir(directory)
        print(directory)

exterior = tk.Canvas(app, height=700, width=600, bg="orange")
exterior.pack()
interior = tk.Frame(exterior, bg="#bcff1f")
interior.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

des_vid = tk.Button(app, text="Descargar un Vídeo", padx=10,
                    pady=5, fg="magenta", bg="cyan")
des_vid.pack()
des_play = tk.Button(app, text="Descargar una Playlist", padx=10,
                    pady=5, fg="white", bg="#FF00FF")
des_play.pack()
des_ub = tk.Button(interior, text="Cambiar la ubicación de descarga", padx=10,
                    pady=5, fg="orange", bg="white", command=ubicacion)
des_ub.pack()

app.mainloop()
