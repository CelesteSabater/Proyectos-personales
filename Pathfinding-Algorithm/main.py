import pygame
from pathfinder import *
from settings import *
from tablero import *

start_pos = [-1, -1]
end_pos = [-1, -1]
state_end = False
state_start = False

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
            if event.key == pygame.K_ESCAPE:
                laberinto.del_path()
                state_end = False
                state_start = False
                for i in range(len(data)):
                    for j in range(len(data[0])):
                        data[i][j] = 0

            if event.key == pygame.K_SPACE:
                a = AStar_Solver(start_pos, end_pos)
                a.Solve()
                for i in range(len(a.closed)):
                    nodo = a.closed[i]
                    laberinto.celdas[nodo[1]][nodo[0]].investigado = True

                for item in a.open:
                    nodo = item.value
                    laberinto.celdas[nodo[1]][nodo[0]].open = True

                for i in range(len(a.path)):
                    print(str(i) + ")" + " " + str(a.path[i][0]))
                    nodo = a.path[i][0]
                    laberinto.celdas[nodo[1]][nodo[0]].path()