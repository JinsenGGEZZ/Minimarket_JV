import os
producto = []
precio = []


def añadir_producto():
    while True:
        print("-----------------------------------")
        print("        AÑADIR PRODUCTO")
        print("-----------------------------------")
        print("PRESIONE Q PARA GUARDAR")
        ingresar_producto = input("ingresa un producto: ")
        if ingresar_producto == 'q':
            break
            
        ingresar_precio = input("ingresa precio: ")

        if ingresar_precio == 'q':
            break
        producto.append(ingresar_producto)
        precio.append(ingresar_precio)


        for i in range(len(producto)):
            print(f"{producto[i]} = {precio[i]}")

def comprar():
    while True:
        print("-----------------------------------")
        print("        comprar")
        print("-----------------------------------")

        ver_lista()
        print("PRESIONE Q PARA GUARDAR")
        filtro = input("ingresa un producto que quieres: ")
        if ingresar_producto == 'q':
            break
            
        ingresar_cantidad = input("ingresa cantidad: ")

        producto.append(ingresar_producto)
        precio.append(ingresar_precio)
    

def ver_lista():
        for i in range(len(producto)):
            print(f"{producto[i]} = {precio[i]}")


    


def menu_principal():
    seleccion()
    
    


def seleccion():
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce una opcion de la lista: "))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entre las opciones de la lista')
     
    return num
 
salir = False
opcion = 0
 
while not salir:
 
    print ("1. Añadir producto")
    print ("2. Comprar")
    print ("3. Ver lista")
    print ("4. Boleta")
     
    print ("Elige una opcion")
 
    opcion = seleccion()
 
    if opcion == 1:
        print ("añadir producto")
        añadir_producto()
    elif opcion == 2:
        print ("comprar")
        comprar()
    elif opcion == 3:
        print("ver lista")
        ver_lista()
    elif opcion == 4:
        print("ver boleta")
        salir = True
    else:
        print ("Introduce un numero entre 1 y 3")
 
print ("Fin")

menu_principal()
