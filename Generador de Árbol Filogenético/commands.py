from settings       import *
import tkinter as tk
from tkinter import simpledialog as tks


def an_especie_f():
    name = tks.askstring("Nombre", "Pon el nombre de la especie:")
    name = name.lower()
    dna = tks.askstring("ADN", "Pon el ADN de la especie:")
    dna = dna.lower()
    specie = Specie(name, dna, k)
    esta = ssp.add_specie(specie)
    if esta == -1:
        respuesta = tk.Tk()
        tk.Label(respuesta, text="La especie ya está en los datos.")

def get_esp():
    name = tks.askstring("Nombre", "Pon el nombre de la especie:")
    name.lower()
    adn = ssp.print_dna(name)
    respuesta = tk.Tk()
    if adn != "-1":
        texto = "El ADN de la especie '" + name + "' es '" + adn.upper() + "'"
        tk.Label(respuesta, text=texto).pack()
    else:
        tk.Label(respuesta, text="Esa especie no está en los datos.").pack()

def distance():
    name1 = tks.askstring("Nombre", "Pon el nombre de la primera especie:")
    name2 = tks.askstring("Nombre", "Pon el nombre de la segunda especie:")
    name1.lower()
    name2.lower()
    distancia = ssp.distance(name1, name2)
    respuesta = tk.Tk()
    if distancia != "-1":
        texto = "La distancia genética entre las especies '" + name1 + "' y '" + name2 + "' es: " + str(distancia) + "."
        tk.Label(respuesta, text=texto).pack()
    else:
        tk.Label(respuesta, text="Una de las especies no está en los datos.").pack()

def deletos():
    name = tks.askstring("Nombre", "Pon el nombre de la especie:")
    name.lower()
    opcion = ssp.deletos(name)
    respuesta = tk.Tk()
    if opcion != -1:
        texto = "La especie '" + name + "' ha sido eliminada."
        tk.Label(respuesta, text=texto).pack()
    else:
        tk.Label(respuesta, text="Esa especie no está en los datos.").pack()

def esiste():
    name = tks.askstring("Nombre", "Pon el nombre de la especie:")
    name.lower()
    opcion = ssp.esiste(name)
    respuesta = tk.Tk()
    texto = "La especie '" + name + "'"
    if opcion:
        texto = texto + " existe."
        tk.Label(respuesta, text=texto).pack()
    else:
        texto = texto + " no existe."
        tk.Label(respuesta, text=texto).pack()

def cjt_esp():
    num = tks.askinteger("Número", "Pon el número de especies:")
    for _ in range(num):
        an_especie_f()

def print_esps():
    lista = ssp.get_cjt()
    respuesta = tk.Tk()
    tk.Label(respuesta, text="Especies en los datos:").pack()
    i = 1
    for especie in lista:
        texto = str(i) + ") Nombre: '" + especie[0] + "' ADN: '" + especie[1].upper() + "'"
        tk.Label(respuesta, text=texto).pack()
        i += 1

def tabla_dist():
    dist = ssp.matrix_distance()
    output = []
    for i in range(len(dist)):
        texto = ssp.ssp[i].name + ") "
        j = 0
        while j < len(dist[i]):
            texto = texto + ssp.ssp[i+j+1].name + ":" + str(dist[i][j]) + " "
            j += 1
        output.append(texto)
    respuesta = tk.Tk()
    tk.Label(respuesta, text="Tabla de distancias:").pack()
    for texto in output:
        tk.Label(respuesta, text=texto, justify="left").pack()


def save_esps():
    lista = ssp.get_cjt()
    output = []
    for especie in lista:
        texto = "@" + especie[0] + "#" + especie[1]
        output.append(texto)
    output.append("@")
    f = open("data.txt", 'w')
    f.writelines(output)
    f.close()

def load_data():
    f = open("data.txt", 'r')
    state = False  # estado si estamos leyendo el nombre
    name = ""
    dna = ""
    for line in f:
        for chr in line:
            if chr == "@":
                if dna != "":
                    a = Specie(name, dna, k)
                    ssp.add_specie(a)
                    name = ""
                    dna = ""
                state = True
            elif chr == "#":
                state = False
            elif state:
                name = name + chr
            else:
                dna = dna + chr