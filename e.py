import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

# Função para criar o gráfico
def create_plot():
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_xlabel('Eixo X')
    ax.set_ylabel('Eixo Y')
    ax.set_title('Simulador de Cache')
    
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

# Criar janela
root = tk.Tk()
root.title('Interface do Gráfico')

# Criar frame para o gráfico
frame = tk.Frame(root)
frame.pack()

# Botão para criar o gráfico
button = tk.Button(root, text='Criar Gráfico', command=create_plot)
button.pack()

# Executar a interface
root.mainloop()
