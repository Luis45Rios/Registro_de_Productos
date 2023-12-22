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
lbl_cantidad=Label(ventana, text="Cantidad: ", font="Arial, 15", bg="#454546", fg="#8ae0db")
lbl_cantidad.place(x=121, y=110)
entry_cantidad=Entry(ventana)
entry_cantidad.place(x=214, y=115)

# lbl_cantidad=Label(ventana, text="Precio: ", font="Arial, 15", bg="#454546", fg="#8ae0db")
# lbl_cantidad.place(x=141, y=150)
# entry_cantidad=Entry(ventana)
# entry_cantidad.place(x=214, y=155)

#Funciones
#FUNCION AÑADIR
def añadir():
    nombre_producto = entry_nombre_producto.get()
    cantidad= entry_cantidad.get()
    if nombre_producto == "" or cantidad == "":
        messagebox.showerror("ERROR", "Error, debe llenar los campos")
    else:
        print("Nombre del producto: ",entry_nombre_producto.get(), "Cantidad: ", entry_cantidad.get())

def editar():
    pass

#Botones
#BOTON AÑADIR
btn_añadir=Button(ventana, text="Añadir Producto", bg="#8ae0db", fg="#000", command=añadir)
btn_añadir.place(x=430, y=90)
#BOTON EDITAR
btn_editar=Button(ventana, text="Editar", bg="#8ae0db", fg="#000")
btn_editar.place(x=430, y=150)

ventana.mainloop()