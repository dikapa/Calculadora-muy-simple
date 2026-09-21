import tkinter as tk

#funciones de la calculadora
def click_boton(valor):
    pantalla.insert(tk.END, valor)

def borrar():
    pantalla.delete(0, tk.END)

def calcular():
    try:
        resultado = eval(pantalla.get())
        borrar()
        pantalla.insert(tk.END, str(resultado))
    except Exception:
        borrar()
        pantalla.insert(tk.END, "Error")

ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("300x400")

#pantalla de texto
pantalla = tk.Entry(ventana, font=("Arial", 20), justify="right", bd=10, insertwidth=4, width=14)
pantalla.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# definicion de botones
botones = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

#crear y colocar botones en la ventana.

for (texto, fila, columna) in botones:
    if texto == '=':
        accion = calcular
    elif texto == 'C':
        accion = borrar
    else:
        accion = lambda t=texto: click_boton(t)
    tk.Button(ventana, text=texto, padx=20, pady=20, font=("Arial", 14), command=accion).grid(row=fila, column=columna, sticky="nsew")

for i in range(5):
    ventana.grid_rowconfigure(i, weight=1)
for i in range(4):
    ventana.grid_columnconfigure(i, weight=1)

# Iniciar la aplicación
ventana.mainloop()