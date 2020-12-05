import pygame
import random
from settings import *

c_fondo = WHITE
c_lin_p = RED
c_lin_np = BLACK

class celda:
    def __init__(self, i, j, screen):
        self.pos = (i,j)
        self.screen = screen
        self.pulsada = random.choice((True, False))

    def update(self):
        pass

    def draw(self):
        if not self.pulsada:
            pygame.draw.rect(self.screen, c_lin_np,
                             (self.pos[0]+(self.pos[0]*tam_celda),
                              self.pos[1] + (self.pos[1] * tam_celda),
                              tam_celda, tam_celda),1)
        else:
            pygame.draw.rect(self.screen, c_lin_p,
                             (self.pos[0]+(self.pos[0]*tam_celda),
                              self.pos[1] + (self.pos[1] * tam_celda),
                              tam_celda, tam_celda),0)

class grid:
    def __init__(self, screen):
        self.pos = (0,0)
        self.celdas = []
        self.screen = screen
        self.makegrid()

    def makegrid(self):
        for i in range(filas):
            self.celdas.append([])
            for j in range(columnas):
                self.celdas[i].append(celda(i, j, self.screen))

    def update(self):
        for i in range(filas):
            for j in range(columnas):
                self.celdas[i][j].update()

    def draw(self):
        for i in range(filas):
            for j in range(columnas):
                self.celdas[i][j].draw()