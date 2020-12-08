from tkinter import *
import pygame
from pathfinder import *
from settings import *
from tablero import *


root = Tk()
start_pos = [-1, -1]
end_pos = [-1, -1]
state_end = False
state_start = False

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
    state_start = True
    dettect_num(end_text.get(), end_pos)
    state_end = True
    if start_pos["i"] != -1 and end_pos["i"] != -1 and start_pos["j"] != -1 and end_pos["j"] != -1:
        root.destroy()

#pygame, crear ventana
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pathfinding Algorithm")
screen.fill(background_colour)
pygame.display.flip()

#creación laberinto
laberinto = grid(screen)

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
                if state_start and state_end:
                    laberinto.click(pos_grid)
                elif not state_start:
                    laberinto.celdas[pos_grid[0]][pos_grid[1]].start_end()
                    data[pos_grid[1]][pos_grid[0]] = 2
                    start_pos[0] = pos_grid[1]
                    start_pos[1] = pos_grid[0]
                    state_start = True
                else:
                    laberinto.celdas[pos_grid[0]][pos_grid[1]].start_end()
                    data[pos_grid[1]][pos_grid[0]] = 3
                    end_pos[0] = pos_grid[1]
                    end_pos[1] = pos_grid[0]
                    state_end = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                a = AStar_Solver(start_pos, end_pos)
                a.Solve()
                for i in range(len(a.path)):
                    print(str(i) + ")" + " " + str(a.path[i][0]))
                    print("Padre", str(a.path[i][1]))
                    nodo = a.path[i][0]
                    laberinto.celdas[nodo[1]][nodo[0]].path()