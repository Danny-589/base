#Sistema de Alquiler de Autos
#Programador: Daniel Reátegui
#Módulo principal
#Fecha: 21/01/226
#Version: 1

import tkinter as tk
import customtkinter as ctk
from tkinter import PhotoImage, messagebox  #<- agraga el message box
from clienteprot import agregar_cliente_db


def crear_ventana_titulo(titulo):
    ventana_aux=ctk.CTkToplevel()
    ventana_aux.title(titulo)
    ventana_aux.geometry("750x400")
    return ventana_aux


#Método para crear la interfaz para agragar clientes
def agregar_cliente():
    ventana_agregar=crear_ventana_titulo("Agregar Cliente")
    ctk.CTkLabel(ventana_agregar, text="Cédula:").grid(row=0, column=0, padx=10, pady=10)
    entry_cedula=ctk.CTkEntry(ventana_agregar)
    entry_cedula.grid(row=0, column=1, padx=80, pady=10)

    ctk.CTkLabel(ventana_agregar, text="Nombres:").grid(row=0, column=2, padx=10, pady=10)
    entry_nombres=ctk.CTkEntry(ventana_agregar)
    entry_nombres.grid(row=0, column=3, padx=10, pady=10)

    ctk.CTkLabel(ventana_agregar, text="Apellidos:").grid(row=1, column=0, padx=10, pady=10)
    entry_apellidos=ctk.CTkEntry(ventana_agregar)
    entry_apellidos.grid(row=1, column=1, padx=80, pady=10)

    ctk.CTkLabel(ventana_agregar, text="Sexo:").grid(row=1, column=2, padx=10, pady=10)
    entry_sexo=ctk.CTkEntry(ventana_agregar)
    entry_sexo.grid(row=1, column=3, padx=10, pady=10)

    ctk.CTkLabel(ventana_agregar, text="Dirección:").grid(row=2, column=0, padx=10, pady=10)
    entry_direccion=ctk.CTkEntry(ventana_agregar)
    entry_direccion.grid(row=2, column=1, padx=80, pady=10)

    ctk.CTkLabel(ventana_agregar, text="Teléfono:").grid(row=2, column=2, padx=10, pady=10)
    entry_telefono=ctk.CTkEntry(ventana_agregar)
    entry_telefono.grid(row=2, column=3, padx=10, pady=10)

    ctk.CTkLabel(ventana_agregar, text="Correo:").grid(row=3, column=0, padx=10, pady=10)
    entry_correo=ctk.CTkEntry(ventana_agregar)
    entry_correo.grid(row=3, column=1, padx=80, pady=10)

    ctk.CTkLabel(ventana_agregar, text="Fecha de nacimiento:").grid(row=3, column=2, padx=10, pady=10)
    entry_fecha_nac=ctk.CTkEntry(ventana_agregar)
    entry_fecha_nac.grid(row=3, column=3, padx=10, pady=10)
    
    ctk.CTkButton(ventana_agregar, text="Guardar", command=lambda:
    guardar_datos("Agregar", entry_cedula.get(),entry_nombres.get(),
                  entry_apellidos.get(),entry_sexo.get(),entry_direccion.get(),
                  entry_telefono.get(),entry_correo.get(),entry_fecha_nac.get())).grid(row=4, column=0, columnspan=4, pady=10)         

def guardar_datos(accion, cedula=None, nombres=None, apellidos=None, sexo=None, 
                  direccion=None, telefono=None, correo=None, fecha_nac=None):
    if accion=="Agregar":
        if cedula and nombres and apellidos and sexo and direccion and telefono and correo and fecha_nac:
            agregar_cliente_db(cedula, nombres, apellidos, sexo, direccion, telefono, correo, fecha_nac)
            messagebox.showinfo("Éxito", "Cliente agregado correctamente")
        else:
            messagebox.showwarning("Error", "Faltan datos para modigicar cliente")

def salir():
    ventana.destroy()



#Crear ventana principal
ventana=ctk.CTk()
ventana.geometry("1200x800")
ventana.title("SISTEMA DE ALQUILER DE AUTOS")



#Incluir fondo y logo
background_image=PhotoImage(file="FOndo.png") 
#logo_image= PhotoImage(file="logotipo.png") 
background_label = tk.Label(ventana, image=background_image)
background_label.place(relwidth=1, relheight=1)
#logo_label = ctk.CTkLabel(ventana, image=logo_image, bg="lightblue")
#logo_label.place(x=10, y=10)



#Crear el menú principal
menu_principal = tk.Menu(ventana)
ventana.configure(menu=menu_principal)



#Crear el menú clientes
menu_clientes = tk.Menu(menu_principal, tearoff=0)
menu_clientes.add_command(label="Agregar", font=("arial", 10), command=agregar_cliente)
menu_clientes.add_command(label="Modificar", font=("arial", 10), command="modificar_cliente")
menu_clientes.add_command(label="Eliminar", font=("arial", 10), command="eliminar_cliente")
menu_clientes.add_command(label="Consultar", font=("arial", 10), command="consultar_cliente")
menu_principal.add_cascade(label="Clientes", menu=menu_clientes)



#Crear el menú autos
menu_autos = tk.Menu(menu_principal,tearoff=0)
menu_autos.add_command(label="Agregar", font=("arial", 10), command="agregar_autos")
menu_autos.add_command(label="Modificar", font=("arial", 10), command="modificar_autos")
menu_autos.add_command(label="Eliminar", font=("arial", 10), command="eliminar_autos")
menu_autos.add_command(label="Consultar", font=("arial", 10), command="consultar_autos")
menu_principal.add_cascade(label="Autos", menu=menu_autos)




#Crear el menú alquiler
menu_alquiler = tk.Menu(menu_principal,tearoff=0)
menu_alquiler.add_command(label="Agregar", font=("arial", 10), command="agregar_alquiler")
menu_alquiler.add_command(label="Modificar", font=("arial", 10), command="modificar_alquiler")
menu_alquiler.add_command(label="Eliminar", font=("arial", 10), command="eliminar_alquiler")
menu_alquiler.add_command(label="Consultar", font=("arial", 10), command="consultar_alquiler")
menu_principal.add_cascade(label="Alquiler", menu=menu_alquiler)




#Crear el menú ayuda
menu_ayuda = tk.Menu(menu_principal,tearoff=0)
menu_ayuda.add_command(label="Documentación", font=("arial", 10), command="agregar_ayuda")
menu_ayuda.add_command(label="Tutorial", font=("arial", 10), command="modificar_ayuda")
menu_ayuda.add_command(label="Licencia", font=("arial", 10), command="eliminar_ayuda")
menu_ayuda.add_command(label="Guía Online", font=("arial", 10), command="consultar_ayuda")
menu_ayuda.add_command(label="Registro de Usuarios", font=("arial", 10), command="consultar_ayuda")
menu_principal.add_cascade(label="Ayuda", menu=menu_ayuda)






#Crear la opción salir en el menú
menu_principal.add_command(label="salir",command=salir)
ventana.configure(menu=menu_principal)



#Iniciar el bucle principal de la ventana
ventana.mainloop()
