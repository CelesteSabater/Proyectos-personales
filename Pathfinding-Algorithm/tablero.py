import pygame
from settings import *

c_fondo = WHITE
c_lin_p = RED
c_lin_np = BLACK
c_special = UGLY_PINK

def click_on_grid(pos):
    if pos[0] > 0 and pos[0] < ((tam_celda+1)*filas) and pos[1] > 0 and pos[1] < ((tam_celda+1) * filas):
        return True
    else:
        return False

def get_grid_pos(pos):
    i = pos[0]//(tam_celda+1)
    j = pos[1]//(tam_celda+1)
    return (i, j)

class celda:
    def __init__(self, i, j, screen):
        self.pos = (i,j)
        self.screen = screen
        self.pulsada = False
        self.special = False

    def draw(self):
        if self.special:
            pygame.draw.rect(self.screen, c_special,
                             (self.pos[0]+(self.pos[0]*tam_celda),
                              self.pos[1] + (self.pos[1] * tam_celda),
                              tam_celda, tam_celda),0)

        elif not self.pulsada:
            pygame.draw.rect(self.screen, c_lin_np,
                             (self.pos[0]+(self.pos[0]*tam_celda),
                              self.pos[1] + (self.pos[1] * tam_celda),
                              tam_celda, tam_celda),1)
        else:
            pygame.draw.rect(self.screen, c_lin_p,
                             (self.pos[0]+(self.pos[0]*tam_celda),
                              self.pos[1] + (self.pos[1] * tam_celda),
                              tam_celda, tam_celda),0)

    def pulso(self):
        if not self.special:
            self.pulsada = not self.pulsada

    def start_end(self):
        self.special = True


class grid:
    def __init__(self, screen):
        self.pos = (0,0)
        self.celdas = []
        self.screen = screen
        self.makegrid()

    def makegrid(self):
        for i in range(filas):
            self.celdas.append([])
            data.append([])
            for j in range(columnas):
                self.celdas[i].append(celda(i, j, self.screen))
                data[i].append(0)

    def draw(self):
        for i in range(filas):
            for j in range(columnas):
                self.celdas[i][j].draw()

    def click(self, pos):
        i = pos[0]
        j = pos[1]
        self.celdas[i][j].pulso()
        if data[j][i] == 0:
            data[j][i] = 1
        else:
            data[j][i] = 0