from tkinter import *
import pygame
from pathfinder import *
from settings import *
from tablero import *


root = Tk()
start_pos = {"i": -1, "j": -1}
end_pos = {"i": -1, "j": -1}


def dettect_num(original, dict):
    num1 = ""
    num2 = ""
    comma = False
    for letra in original:
        if letra == ',':
            comma = True
        elif ord(letra) >= ord("0") and ord(letra) <= ord("9") and not comma:
            num1 = num1 + letra
        elif ord(letra) >= ord("0") and ord(letra) <= ord("9") and comma:
            num2 = num2 + letra
    if (int(num1) > filas or int(num1) < 0) or (int(num2) > filas or int(num2) < 0):
        dict["i"] = -1
        dict["j"] = -1
    else:
        dict["i"] = int(num1)
        dict["j"] = int(num2)

def click():
    dettect_num(start_text.get(), start_pos)
    dettect_num(end_text.get(), end_pos)
    if start_pos["i"] != -1 and end_pos["i"] != -1 and start_pos["j"] != -1 and end_pos["j"] != -1:
        root.destroy()


#ventana emergente que pide posición inicial y final del algoritmo de búsqueda
text_1 = Label(root, text="Start:(i, j)")
text_1.pack()
start_text = Entry(root, width=20, borderwidth=5)
start_text.pack()
text_2 = Label(root, text="End:(i, j)")
text_2.pack()
end_text = Entry(root, width=20, borderwidth=5)
end_text.pack()
boton = Button(root, text="Aceptar posición", command=click)
boton.pack()
root.mainloop()

#pygame, crear ventana
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pathfinding Algorithm")
screen.fill(background_colour)
pygame.display.flip()

#creación laberinto
laberinto = grid(screen)
laberinto.celdas[start_pos["j"]][start_pos["i"]].start_end()
data[start_pos["i"]][start_pos["j"]] = 2
laberinto.celdas[end_pos["j"]][end_pos["i"]].start_end()
data[end_pos["i"]][end_pos["j"]] = 3

for lineas in data:
    print(lineas)

#bucle ventana
running = True
while running:
    screen.fill(background_colour)
    laberinto.draw()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
          pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if click_on_grid(pygame.mouse.get_pos()):
                pos_grid = get_grid_pos(pygame.mouse.get_pos())
                laberinto.click(pos_grid)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pathfinder(data)

print("\n", "==========", "\n")
for lineas in data:
    print(lineas)