import tkinter as tk
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Hélice Conica

# Hélice Circular

# Corona Sinusoidal

# Curva de Viviani

# Hipopoda

# Espiral Cónica de Papus

# Curva de Arquitas

# Horóptera

# Curva Bicilindrica
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation
import matplotlib.pyplot as plt

#Se crea funcion

def bicilindrica():
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ab = fig.gca(projection='3d')

    a = 5
    c = 1
    b = 1
    theta = np.linspace(-4 * np.pi, 4* np.pi, 100)

#Se da valor a las variables

    x1 = a*np.cos(theta)**2
    y1 = np.sqrt(-(b*2 - (2*c + a*(np.sin(theta))**2)))
    z1 = - c+a*np.sin(theta)
    z = c+a*np.sin(theta)
    x = a*np.cos(theta)**2
    y = np.sqrt(-(b*2 - (2*c + a*(np.sin(theta))**2)))
    N = 1000
    t= 10

#Se aplica formula parametrica

    def gen(N):
        for theta in np.linspace(-4 * np.pi, 4 * np.pi, 100):
            x = a*np.cos(theta)
            y =  np.sqrt(-(b*2 - (2*c + a*(np.sin(theta))**2)))
            z = c+a*np.sin(theta)
            yield np.array([x, y, z])


    def update(num, data, line):
        line.set_data(data[:2, :num])
        line.set_3d_properties(data[2, :num])


    def gen1(N):
        for theta in np.linspace(-4 * np.pi, 4 * np.pi, 100):
            x1 = a*np.cos(theta)
            y1 = np.sqrt(-(b*2 - (2*c + a*(np.sin(theta))**2)))
            z1 = - (c+a*np.sin(theta))
            yield np.array([x1, y1, z1])


    def update1(num1, data1, line1):
        line1.set_data1(data1[:2, :num1])
        line1.set_3d_properties(data1[2, :num1])


    data = np.array(list(gen(N))).T
    data1 = np.array(list(gen1(N))).T
    line, = ax.plot(data[0, 0:1], data[1, 0:1], data[2, 0:1])
    line1, = ab.plot(data1[0, 0:1], data1[-1, 0:1], data1[-2, 0:1])

# Configuracion de ejes
    ax.set_xlim3d([-20.0, 20.0])
    ax.set_xlabel('X')

    ab.set_xlim3d([20.0, -20.0])
    ab.set_xlabel('Eje X')

    ax.set_ylim3d([-20.0, 20.0])
    ax.set_ylabel('Y')

    ab.set_ylim3d([20.0, -20.0])
    ab.set_ylabel('Eje Y')

    ax.set_zlim3d([-20.0, 10.0])
    ax.set_zlabel('Z')

    ab.set_zlim3d([20.0, -10.0])
    ab.set_zlabel('Eje Z')

    ani = animation.FuncAnimation(fig, update, N, fargs=(data, line), interval=10000 / N, blit=False)

    ani1 = animation.FuncAnimation(fig, update1, N, fargs=(data1, line1), interval=10000 / N, blit=False)


    plt.show()

if __name__ == '__main__':
    # Creación de Ventanas
    root = tk.Tk()
    root.wm_title("Tarea 02 (15%)")
    root.geometry("800x600")

    # Crear frame contenedor de los elementos
    frame = tk.Frame(root)
    frame.pack(padx=20, pady=20)
    # Añadir titulo
    label = tk.Label(frame, text="Curvas Paramétricas Famosas", height="2")
    label.pack(fill=tk.X, expand=1)
    # imagen = tk.PhotoImage(file="image.jpg")
    boton = tk.Button(master=frame, text="Curva Bicilindrica", command=bicilindrica)
    boton.pack(side=tk.BOTTOM, padx=10, pady=10)

    tk.mainloop()
