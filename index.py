from tkinter import *
from tkinter import messagebox

ventana= Tk()
ventana.title("Nuevo Producto")
ventana.geometry("1300x599")
ventana.config(bg="#454546")

#Titulo "NUEVO PRODUCTO"
titulo_nuevo_producto=Label(ventana, text= "Nuevo producto", font="Arial, 35", bg="#454546", fg="#8ae0db")
titulo_nuevo_producto.place(x=725, y=30, anchor=CENTER)

#Labels and inputs
#PRODUCTO
lbl_nombre_producto=Label(ventana, text="Nombre del Producto: ", font="Arial, 15", bg="#454546", fg="#8ae0db")
lbl_nombre_producto.place(x=15, y=70)
entry_nombre_producto=Entry(ventana)
entry_nombre_producto.place(x=214, y=75)

#CANTIDAD
lbl_cantidad=Label(ventana, text="Cantidad", font="Arial, 15", bg="#454546", fg="#8ae0db")

ventana.mainloop()