import tkinter as tk
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation
from tkinter import *


def start_curve(a=1,t=13,anima="ON",contador=0,presionado="vacio"):
	# Esos son parametros opcionales, estos parametros se tomaran cuando se inicie el programa
	# El programa se base es una recursividad o actulizacion de la ventana (siempre usara la misma cantida de memoria)
	# Los parametros cambiaran cuando se invoque la funcion "recuperar" en la linea 136
	# La funcion recuperar se encarga de rescatar TODOS los valores que puedan cambiar 

	ventana = Tk()
	ventana.title("Fisica interactiva") 
	ventana.resizable(0,0) # impide que se expanda la ventana
	ventana.geometry("900x900") # dimension de la ventana en pixeles
	# FRAMES
	# Se crearon 3 frames para organizar mejor el programa
	principal_frame = Frame(ventana,width=900,height=100).place(x=0,y=0)
	botones_frame = Frame(ventana,width=250,height=800).place(x=0,y=100)
	grafico_frame = Frame(ventana,width=650,height=800).place(x=250,y=100)


	# ------------------------------- PRINCIPAL FRAME -------------------
	# titulo
	Label(principal_frame,text="Curva de viviani",font=(50)).place(x=400,y=50)
	# boton de salida
	Button(principal_frame,text="<<",font=(50),command=lambda:salir_viviani(ventana)).place(x=50,y=50)
	# Opciones de animacion
	Label(principal_frame,text="Animacion",font=(50)).place(x=710,y=50)
	Button(principal_frame,text="ON",command=lambda:recuperar(ventana,entry_a,entry_t,"ON",contador,presionado)).place(x=830,y=50)
	Button(principal_frame,text="OFF",command=lambda:recuperar(ventana,entry_a,entry_t,"OFF",contador,presionado)).place(x=860,y=50)
	# ------------------------------- PRINCIPAL FRAME -------------------


	# ------------------------------- BOTONES FRAME -------------------
	# botones
	# Se utilizo ancho 27 y altura 2 por que 27 se aproxima a 200p y 2 por que son exactamente 40p
	# se hiso una division de 400p / 11 (por que son 11 espacio vacios) y se aproximo a 36p (es decir 36p de espacio entre botones)
	# como el boton ocupa 40p y 36p de espacio entre botones cada boton tendra 76p de distancia (40+36=76)
	Button(botones_frame,text="Posicion",width=27,height=2,command=lambda:recuperar(ventana,entry_a,entry_t,anima,contador,"Posicion")).place(x=50,y=136) 
	Button(botones_frame,text="Velocidad",width=27,height=2,command=lambda:recuperar(ventana,entry_a,entry_t,anima,contador,"Velocidad")).place(x=50,y=212)
	Button(botones_frame,text="Velocidad media",width=27,height=2,command=lambda:recuperar(ventana,entry_a,entry_t,anima,contador,"Velocidad media")).place(x=50,y=288)
	Button(botones_frame,text="Aceleracion",width=27,height=2,command=lambda:recuperar(ventana,entry_a,entry_t,anima,contador,"Aceleracion")).place(x=50,y=364)
	Button(botones_frame,text="Aceleracion media",width=27,height=2,command=lambda:recuperar(ventana,entry_a,entry_t,anima,contador,"Aceleracion media")).place(x=50,y=440)
	Button(botones_frame,text="Curvatura",width=27,height=2,command=lambda:recuperar(ventana,entry_a,entry_t,anima,contador,"Curvatura")).place(x=50,y=516)
	Button(botones_frame,text="Radio de curvatura",width=27,height=2,command=lambda:recuperar(ventana,entry_a,entry_t,anima,contador,"Radio de curvatura")).place(x=50,y=592)
	Button(botones_frame,text="Torsion",width=27,height=2,command=lambda:recuperar(ventana,entry_a,entry_t,anima,contador,"Torsion")).place(x=50,y=668)
	Button(botones_frame,text="Radio de torsion",width=27,height=2,command=lambda:recuperar(ventana,entry_a,entry_t,anima,contador,"Radion de torsion")).place(x=50,y=744)
	Button(botones_frame,text="Longitud de arco",width=27,height=2,command=lambda:recuperar(ventana,entry_a,entry_t,anima,contador,"Longitud")).place(x=50,y=823)
	# ------------------------------- BOTONES FRAME -------------------


	# ------------------------------- GRAFICO FRAME -------------------
	# Los input
	# se puso 32 y no 27 como en los anteriores debido a que entry no trabaja con las mismas proporciones
	# se usaron 83p de distancia entre los input
	# como mide aproximadamente 200p entonces entre cada input existen 283p entre los entry
	# el mensaje que esta al lado esta a 30p del entry
	entry_a = StringVar()
	entry_a.set("")
	entry_t = StringVar()
	entry_t.set("")
	# entre la linea 66 y 69 se evitaran futuros bug en el programa
	if contador != 0:
		# Las siguientes dos linea actulizaran los entry con los datos ingresados por el usuario
		entry_a.set(a)
		entry_t.set(t)
		# La siguiente funcion evitara todos los errores posibles (para mas detalles ir a la linea 151)
		a,t = evitar_errores(a,t)
	# width=12 por que da los 75p
	# los 30p de alto nose logro debido que entry no acepta height
	Entry(grafico_frame,textvariable=entry_a,width=12,justify="center").place(x=333,y=823) # justify centrara el "texto" escrito
	Label(grafico_frame,text="a=",font=(35)).place(x=303,y=823)
	Entry(grafico_frame,textvariable=entry_t,width=12,justify="center").place(x=616,y=823)
	Label(grafico_frame,text="t=",font=(35)).place(x=589,y=823)
	# Este boton se encargara de recuperar los datos en los entry
	Button(grafico_frame,text="Graficar",command=lambda:recuperar(ventana,entry_a,entry_t,anima,contador,presionado)).place(x=800,y=823)

	if presionado != "vacio":
		# Esto se activa si se preciona algun boton
		# La siguiente linea pondra un label y su texto sera el mismo del boton presionado
		Label(grafico_frame,text=presionado).place(x=400,y=744)
		# La siguiente funcion hara los calcuos dependiendo del boton que se presiono
		resultado = operacion(presionado,a,t)
		# la siguiente linea pondra un label con la respuesta del calculo hecho en la linea anterior
		Label(grafico_frame,text=resultado).place(x=450,y=744)

	# implementar grafico
	
	fig = plt.figure()
	canvas = FigureCanvasTkAgg(fig,ventana)
	canvas.get_tk_widget().place(x=255.,y=212)
	canvas._tkcanvas.place(x=255.,y=212)
	grafico = Axes3D(fig) 
	grafico.set_xlabel('X') 
	grafico.set_ylabel('Y') 
	grafico.set_zlabel('Z')
	# La siguiente lineas existe por si se quiere conocer posicion en t = 0 
	if t == 0:
		t = np.linspace(-0.1, t,60)
		# esta entre -0.1 y 0 para que se logre visializar una linea (aunque es pequeña)
		# si estuviera entre 0 y 0 no se graficaria nada
	else:

		t = np.linspace(0, t,60)


	x = a * (1 + np.cos(t))
	y = a * np.sin(t)
	z = 2 * a * np.sin(t/2)

	# Las siguientes dos lineas estan para dar el conjunto de cordenada a la animacion
	eje = [x,y,z]
	ejes = np.array(eje)

	if anima == "ON":
		linea, = grafico.plot(x, y, z, 'b', label="Curva de Viviani", lw=1)
		animacion = animation.FuncAnimation(fig, animacion_viviani, fargs=(ejes, linea),frames=60,interval=16.6, blit=False, repeate=False)
		
	else:
		linea, = grafico.plot(x, y, z, 'b', label="Curva de Viviani", lw=1)


	ventana.mainloop()

def salir_viviani(ventana):
    ventana.quit()
    ventana.destroy()

def recuperar(ventana,entry_a,entry_t,anima,contador,presionado):
	entry_a.set(entry_a.get()) 
	entry_t.set(entry_t.get()) 
	# los valores de los entry los almacenaremos como string para luego solo incorporalos en la linea 72 y 73
	a = str(entry_a.get())
	t = str(entry_t.get())
	contador = contador + 1
	salir_viviani(ventana) # cerraremos la ventana
	# Ahora se abrira otra ventana con todos los datos actualizados
	start_curve(a,t,anima,contador,presionado)

def animacion_viviani(num, ejes, linea):
    linea.set_data(ejes[:2, :num])
    linea.set_3d_properties(ejes[2, :num])

def evitar_errores(a,t):
	if a == "":
		# entra aqui si no se ingreso nada en el entry
		a = 1
	else:
		if "," in a or "." in a:
			# entra aqui se el numero ingresado en el entry es de la siguiente manera: 2,3 o 2.3
			# eso implica que es un flotante asi que prodeceremos a convertir el string en flotante
			a = a.replace(",",".")
			a = float(a)
		else:
			# sino significa que se ingreso un entero
			a = int(a)
	if t == "":
		t = 13
	else:
		if "," in t or "." in t:
			t = t.replace(",",".")
			t = float(t)
		else:
			t = int(t)
	return a,t

def operacion(presionado,a,t):
	if presionado == "Posicion":
		x = str(a * (1 + np.cos(t)))
		y = str(a * np.sin(t))
		z = str(2 * a * np.sin(t/2))
		cordenada = "(" + x + " , " + y + " , "+ z + ")"
	elif presionado == "Velocidad":
		x = str(a * (- np.sin(t)))
		y = str(a * np.cos(t))
		z = str(a * np.cos(t/2))
		cordenada = "(" + x + " , " + y + " , "+ z + ")"
	elif presionado == "Aceleracion":
		x = str(-a * np.cos(t))
		y = str(a * (- np.sin(t)))
		z = str((-(a * np.sin(t/2)))/2)
		cordenada = "(" + x + " , " + y + " , "+ z + ")"
	elif presionado == "Velocidad media":
		x = str((a * (-1 + np.cos(t)))/t)
		y = str((a * np.sin(t))/t)
		z = str((2 * a * np.sin(t/2))/t)
		cordenada = "(" + x + " , " + y + " , "+ z + ")"
	elif presionado == "Aceleracion media":
		x = str((-a * np.sin(t))/t)
		y = str((a * (np.cos(t) - 1))/t)
		z = str((a * (np.cos(t/2) - 1))/t)
		cordenada = "(" + x + " , " + y + " , "+ z + ")"
	else:
		cordenada = "Estamos trabajando para ello"
	return cordenada




_name_ = "_main_"
if _name_ == "_main_":
	 start_curve()