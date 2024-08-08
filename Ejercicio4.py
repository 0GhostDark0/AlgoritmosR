import matplotlib.pyplot as plt
import numpy as np

# Definir los nombres de los integrantes del grupo
names = ["Alejandro", "Alfonso", "Galvis"]

# Definir las coordenadas x e y para cada nombre
x_coords = [0, 2, 4]
y_coords = [0, 1, 2]

# Crear un plot en 2D
fig, ax = plt.subplots()

# Dibujar las líneas rectas que conectan los nombres
ax.plot([x_coords[0], x_coords[1]], [y_coords[0], y_coords[1]], 'k-')
ax.plot([x_coords[1], x_coords[2]], [y_coords[1], y_coords[2]], 'k-')

# Dibujar las curvas que rodean cada nombre
for i, name in enumerate(names):
    ax.plot(x_coords[i] + np.cos(np.linspace(0, 2*np.pi, 100)), 
            y_coords[i] + np.sin(np.linspace(0, 2*np.pi, 100)), 
            'b-')

# Agregar los nombres como texto en el plot
for i, name in enumerate(names):
    ax.text(x_coords[i], y_coords[i], name, ha='center', va='center')

# Configurar el plot
ax.set_xlim(-1, 5)
ax.set_ylim(-1, 3)
ax.set_title("Integrantes del grupo")
ax.set_xlabel("X")
ax.set_ylabel("Y")

# Mostrar el plot
plt.show()