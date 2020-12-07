from settings import *
import math

def in_data(node, list):
    for nodo in list:
        if node[0] == nodo[0] and node[1] == nodo[1]:
            return True
    return False

def calc_cost(pos, obj):
    hor = pos[0] - obj[0]
    ver = pos[1] - obj[1]
    if hor < 0:
        hor = hor * -1
    if ver < 0:
        ver = ver * -1
    cost = 0
    while hor > 0 or ver > 0:
        if hor > 0 and ver > 0:
            cost += 14
            hor -= 1
            ver -= 1

        elif ver > 0:
            cost += 10
            ver -= 1

        else:
            cost += 10
            hor -= 1

    return cost

def pathfinder(data, start_pos, end_pos):
    open = []
    closed = []
    i = end_pos[0]
    j = end_pos[1]
    objective = (i, j)
    i = start_pos[0]
    j = start_pos[1]
    cost = calc_cost((i, j), (objective[0], objective[1]))
    open.append((i, j, (cost, cost, 0), None))
    finished = False
    aux = None
    while not finished:
        best = 0
        current = open[0]
        for i in range(len(open)):
            if open[i][2][1] < open[best][2][1] or (open[i][2][1] == open[best][2][1] and open[i][2][0] < open[best][2][0]):
                best = i
                current = open[i]
        open.pop(best)


        # miramos los vecinos
        i = current[0]
        j = current[1]
        north = (i - 1, j)
        no_ea = (i - 1, j + 1)
        east = (i, j + 1)
        so_ea = (i + 1, i + 1)
        south = (i + 1, j)
        so_we = (i + 1, j - 1)
        west = (i, j - 1)
        no_we = (i - 1, j - 1)
        vecinitos = [north, east, south, west, no_ea, no_we so_ea, so_we]
        i = 0
        while i < len(vecinitos):
            if vecinitos[i][0] < 0 or vecinitos[i][0] >= filas or vecinitos[i][1] < 0 or vecinitos[i][1] >= columnas:
                vecinitos.pop(i)
            else:
                i += 1

        for pos in vecinitos:

            if pos[0] == objective[0] and pos[1] == objective[1]:
                finished = True
                aux = current
                break

            aparecio = False
            for nodo in closed:
                if nodo[0] == pos[0] and nodo[1] == pos[1]:
                    aparecio = True
                    break

            if data[pos[1]][pos[0]] == 1:
                pass
            else:
                # calculo del f_cost del vecino
                hor = pos[0] - current[0]
                ver = pos[1] - current[1]
                if hor < 0:
                    hor = hor * -1
                if ver < 0:
                    ver = ver * -1
                # g_cost = ditancia desde el origen
                if hor == 1 and ver == 1:
                    g_cost = current[2][2] + 14
                else:
                    g_cost = current[2][2] + 10

                dist_x = (pos[0] - objective[0]) * 2
                if dist_x < 0:
                    dist_x *= -1
                dist_y = (pos[1] - objective[1]) * 2
                if dist_y < 0:
                    dist_y *= -1

                h_cost = math.sqrt( dist_x + dist_y )  # h_cost = distancia a destino
                f_cost = g_cost + h_cost
                # el nodo[3] representa de donde viene el nodo
                nodo = (pos[0], pos[1], (h_cost, f_cost, g_cost), current)
                in_open = in_data(nodo, open)
                in_closed = in_data(nodo, closed)
                if in_open:
                    for i in range(len(open)):
                        if open[i][0] == pos[0] and open[i][1] == pos[1]:
                            if open[i][2][1] >  f_cost or (open[i][2][1] == f_cost and open[i][2][0] > h_cost):
                                open[i] = nodo
                                break
                            else:
                                break

                elif in_closed:
                    for i in range(len(closed)):
                        if closed[i][0] == pos[0] and closed[i][1] == pos[1]:
                            if closed[i][2][1] > f_cost or (closed[i][2][1] == f_cost and closed[i][2][0] > h_cost):
                                open.append(nodo)
                                break
                            else:
                                break
                else:
                    open.append(nodo)

        closed.append(current)

    path = []
    while aux[3] != None:
        path.append(aux)
        for nodo in closed:
            if nodo[0] == aux[3][0] and nodo[1] == aux[3][1]:
                aux = nodo
                break

    return path