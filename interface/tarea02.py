import tkinter as tk
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation
from matplotlib import pyplot as plt

def arquitas():
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ab = fig.gca(projection='3d')

    a = 35

    theta = np.linspace(-1 / 2 * np.pi, 1 / 2 * np.pi, 99)

    x1 = a * np.cos(theta) ** 2
    y1 = a * np.cos(theta) * np.sin(theta)
    z1 = - a * ((1 - np.cos(theta)) * (np.cos(theta)) ** 1 / 2)
    z = a * (((1 - np.cos(theta)) * np.cos(theta)) ** 1 / 2)
    x = a * np.cos(theta) ** 2
    y = a * np.cos(theta) * np.sin(theta)
    N = 100

    def gen(N):
        for theta in np.linspace(-1 / 2 * np.pi, 1 / 2 * np.pi, 100):
            x = a * np.cos(theta) ** 2
            y = a * np.cos(theta) * np.sin(theta)
            z = a * (((1 - np.cos(theta)) * np.cos(theta)) ** 1 / 2)
            yield np.array([x, y, z])

    def update(num, data, line):
        line.set_data(data[:2, :num])
        line.set_3d_properties(data[2, :num])

    def gen1(N):
        for theta in np.linspace(-1 / 2 * np.pi, 1 / 2 * np.pi, 100):
            x1 = a * np.cos(theta) ** 2
            y1 = a * np.cos(theta) * np.sin(theta)
            z1 = -a * (((1 - np.cos(theta)) * np.cos(theta)) ** 1 / 2)
            yield np.array([x1, y1, z1])

    def update1(num1, data1, line1):
        line1.set_data(data1[:2, :num1])
        line1.set_3d_properties(data1[2, :num1])

    data = np.array(list(gen(N))).T
    data1 = np.array(list(gen1(N))).T
    line, = ax.plot(data[2, 0:1], data[2, 0:1], data[2, 0:1])
    line1, = ab.plot(data1[2, 0:1], data1[-2, 0:1], data1[-2, 0:1])

    # Propiedades del plano
    ax.set_xlim3d([-40.0, 40.0])
    ax.set_xlabel('X')

    ab.set_xlim3d([-40.0, 40.0])
    ab.set_xlabel('X')

    ax.set_ylim3d([-40.0, 40.0])
    ax.set_ylabel('Y')

    ab.set_ylim3d([-40.0, 40.0])
    ab.set_ylabel('Y')

    ax.set_zlim3d([-40.0, 20.0])
    ax.set_zlabel('Z')

    ab.set_zlim3d([-40.0, 20.0])
    ab.set_zlabel('Z')

    ani = animation.FuncAnimation(fig, update, N, fargs=(data, line,), interval=100 / N, blit=False, repeat=False, )

    ani1 = animation.FuncAnimation(fig, update1, N, fargs=(data1, line1,), interval=100 / N, blit=False, repeat=False, )

    plt.show()

if __name__ == '__main__':
    # Creación de Ventanas
    root = tk.Tk()
    root.wm_title("Tarea 02 (15%)")
    root.geometry("800x600")

    # Crear frame contenedor de los elementos
    frame = tk.Frame(root)
    frame.pack(padx=20, pady=20)
    # arquitas_img = tk.PhotoImage(file="arquitas.png")
    curva_de_arquitas = tk.Button(master=frame, command=arquitas, height="100", width="100")
    curva_de_arquitas.pack(side=tk.BOTTOM, padx=10, pady=10)
    # Añadir titulo
    label = tk.Label(frame, text="Curvas Paramétricas Famosas", height="2")
    label.pack(fill=tk.X, expand=1)

    tk.mainloop()
