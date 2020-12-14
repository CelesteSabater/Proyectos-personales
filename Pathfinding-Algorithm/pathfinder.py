from settings import *
from queue import PriorityQueue

class State_Pos(object):
    def __init__(self, value, parent,
                 start = 0, goal = 0):
        self.children = []
        self.parent = parent
        self.value = value
        self.dist_f = 0

        if parent:
            self.start = parent.start
            self.goal = parent.goal
            self.path = parent.path.copy()
            self.path.append((value, parent.value))
            if (self.value[0] - parent.value[0] != 0) and (self.value[1] - parent.value[1] != 0):
                self.dist_g = parent.dist_g + 2
            else:
                self.dist_g = parent.dist_g + 1
        else:
            self.path = [(value, -1)]
            self.start = start
            self.goal = goal
            self.dist_g = 0

        self.dist_f = self.GetDist()

    def GetDist(self):

        if self.value[0] == self.goal[0] and self.value[1] == self.goal[1]:
            return -1

        i = self.value[0]
        j = self.value[1]

        dist_x = abs(i - self.goal[0])
        dist_y = abs(j - self.goal[1])
        dist_h = abs(dist_x-dist_y)  # h_cost = distancia a destino

        dist_f = self.dist_g + dist_h

        return dist_f

    def CreateChildren(self):
        if not self.children:
            i = self.value[0]
            j = self.value[1]
            north = [i - 1, j]
            no_ea = [i - 1, j + 1]
            east = [i, j + 1]
            so_ea = [i + 1, j + 1]
            south = [i + 1, j]
            so_we = [i + 1, j - 1]
            west = [i, j - 1]
            no_we = [i - 1, j - 1]
            neighbours = [north, east, south, west, no_ea, no_we, so_ea, so_we]
            i = 0
            while i < len(neighbours):
                #si ocurre esto es que vecino está fuera de la matriz
                out_index = neighbours[i][0] < 0 or neighbours[i][0] >= filas or neighbours[i][1] < 0 or neighbours[i][1] >= columnas
                if out_index:
                    neighbours.pop(i)
                else:
                    #en data los muros se representan con un 1, y pasar por un muro no es posible
                    if data[neighbours[i][1]][neighbours[i][0]] == 1:
                        neighbours.pop(i)
                    else:
                        i += 1

            for neighbour in neighbours:
                child = State_Pos(neighbour, self)
                self.children.append(child)

class AStar_Solver:
    def __init__(self, start , goal):
        self.path          = []
        self.open          = []
        self.closed        = []
        self.priorityQueue = PriorityQueue()
        self.start         = start
        self.goal          = goal

    def Solve(self):
        #el 0 representa que no tiene hijos
        startPoint = State_Pos(self.start,
                                  0,
                                  self.start,
                                  self.goal)
        count = 0
        self.priorityQueue.put((0,count,startPoint))
        self.open.append(startPoint)
        #mientras el path esté vacio y mientra priorityq tiene
        #una medida...
        while(not self.path and self.priorityQueue.qsize()):
            #obtiene el hijo con mejor puntuación de la lista
            closestPoint = self.priorityQueue.get()[2]
            #y luego le creamos sus hijos respectivos
            closestPoint.CreateChildren()
            for child in closestPoint.children:
                self.open.append(child)
                if child.value not in self.closed:
                    count +=1
                    if child.dist_f == -1:
                        self.path = child.path
                        break
                    self.priorityQueue.put((child.dist_f,count,child))
            #añadimos el hijo este a la lista de visitados
            self.closed.append(closestPoint.value)
            #quitamos el hijo de open
            for i in range(len(self.open)):
                if self.open[i].value[0] == closestPoint.value[0] and self.open[i].value[1] == closestPoint.value[1]:
                    self.open.pop(i)
                    break

        #esto está por si no hay forma de llegar al objetivo
        if not self.path:
            print("Goal of [", str(self.goal[0]), ",", str(self.goal[1]), "] is not possible!")

        return self.path