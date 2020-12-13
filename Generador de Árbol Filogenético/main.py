from settings       import *
from commands       import *
import tkinter as tk

#canvas general
root = tk.Tk()
fondo = tk.Canvas(root, height=altura, width=anchura, bg=color_f)
fondo.pack()
root.resizable(width=False, height=False)
i = 0
load_data()

#botón añadir especie
an_especie = tk.Button(fondo, text="Añadir especie", padx=10, pady=2.5, fg=color_texto, bg=color_boton, command=an_especie_f)
i = 1
button1_window = fondo.create_window((anchura+10)/2, i * 30, window=an_especie)

#botón obtener gen
ob_gen = tk.Button(fondo, text="Obtener gen especie", padx=10, pady=2.5, fg=color_texto, bg=color_boton, command=get_esp)
i += 1
button2_window = fondo.create_window((anchura+10)/2, i * 30, window=ob_gen)

#botón obtener distacia
ob_dis = tk.Button(fondo, text="Obtener distancia entre especies", padx=10, pady=2.5, fg=color_texto, bg=color_boton, command=distance)
i += 1
button3_window = fondo.create_window((anchura+10)/2, i * 30 , window=ob_dis)

#botón eliminar especies
deletos_es = tk.Button(fondo, text="Eliminar una especie", padx=10, pady=2.5, fg=color_texto, bg=color_boton, command=deletos)
i += 1
button4_window = fondo.create_window((anchura+10)/2, i * 30 , window=deletos_es)

#botón existe especie
esiste = tk.Button(fondo, text="Verificar existencia especie", padx=10, pady=2.5, fg=color_texto, bg=color_boton, command=esiste)
i += 1
button5_window = fondo.create_window((anchura+10)/2, i * 30 , window=esiste)

#botón leer cjt especies
leer_especies = tk.Button(fondo, text="Añadir conjunto especies", padx=10, pady=2.5, fg=color_texto, bg=color_boton, command=cjt_esp)
i += 1
button6_window = fondo.create_window((anchura+10)/2, i * 30 , window=leer_especies)

#botón imprimir cjt especies
print_cjt_especies = tk.Button(fondo, text="Imprimir conjunto especies", padx=10, pady=2.5, fg=color_texto, bg=color_boton, command=print_esps)
i += 1
button7_window = fondo.create_window((anchura+10)/2, i * 30 , window=print_cjt_especies)

#boton imprimir tabla distancia
print_tabla = tk.Button(fondo, text="Imprimir tabla distancias", padx=10, pady=2.5, fg=color_texto, bg=color_boton, command=tabla_dist)
i += 1
button8_window = fondo.create_window((anchura+10)/2, i * 30 , window=print_tabla)


root.mainloop()

save_esps()