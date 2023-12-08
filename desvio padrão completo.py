import tkinter as tk
from tkinter import ttk
import math

def calcular_desvio_padrao():
    var1 = int(entry_var1.get())
    var2 = int(entry_var2.get())
    var3 = int(entry_var3.get())

    # Cálculo da média
    media = float(var1 + var2 + var3) / 3

    # Cálculo da variância
    variancia = int((var1 - media)**2 + (var2 - media)**2 + (var3 - media)**2) / 3

    # Cálculo do desvio padrão
    desvio_padrao = math.sqrt(variancia)

    resultado_label.config(text="O desvio padrão é {:.3f}".format(desvio_padrao))

# Criar a janela principal
root = tk.Tk()
root.title("Calculadora de Desvio Padrão")

# Criar e posicionar widgets
label_var1 = ttk.Label(root, text="Digite um valor:")
label_var1.grid(row=0, column=0, padx=10, pady=10)
entry_var1 = ttk.Entry(root)
entry_var1.grid(row=0, column=1, padx=10, pady=10)

label_var2 = ttk.Label(root, text="Digite um segundo valor:")
label_var2.grid(row=1, column=0, padx=10, pady=10)
entry_var2 = ttk.Entry(root)
entry_var2.grid(row=1, column=1, padx=10, pady=10)

label_var3 = ttk.Label(root, text="Digite o terceiro valor:")
label_var3.grid(row=2, column=0, padx=10, pady=10)
entry_var3 = ttk.Entry(root)
entry_var3.grid(row=2, column=1, padx=10, pady=10)

calcular_button = ttk.Button(root, text="Calcular Desvio Padrão", command=calcular_desvio_padrao)
calcular_button.grid(row=3, column=0, columnspan=2, pady=10)

resultado_label = ttk.Label(root, text="")
resultado_label.grid(row=4, column=0, columnspan=2, pady=10)

# Iniciar o loop da interface gráfica
root.mainloop()
