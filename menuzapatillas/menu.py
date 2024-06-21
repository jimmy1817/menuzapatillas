import os
os.system("cls")

def buscar_id(id):
    try:
        i = productos.index(id)
        return i
    except ValueError:
        return -1


def get_folio():
    if ventas:
        ultimo_folio = ventas[-1][0]
        return ultimo_folio + 1
    else:
        return 1001 




productos = []
archivo='productos.txt'
ventas = []
ventas='ventas.txt'
#--------------------------------------------------------------------
def leer_datos_archivo(archivo):
    # Lista para almacenar los datos
    lista_datos = []   

    # Abrimos el archivo en modo lectura
    with open(archivo, 'r') as file:
        # Leemos cada línea del archivo
       
        for linea in file:
            # Eliminamos los espacios en blanco y los saltos de línea
            linea = linea.strip()
            # Dividimos la línea por comas
            datos = linea.split(',')
            # Creamos un diccionario con los datos
            lista_datos.append(datos[0])
            lista_datos.append(datos[1])
            lista_datos.append(datos[2])
            lista_datos.append(int(datos[3]))
            lista_datos.append(int(datos[4]))

    return lista_datos

def imprimir_datos(lista_datos):
    for i in range (0,len(lista_datos),5):
        print(f"{lista_datos[i]}, {lista_datos[i+1]}, {lista_datos[i+2]}, {lista_datos[i+3]}, {lista_datos[i+4]}")

def eliminar(rut):
    # Lista para almacenar los datos actualizados
    lista_datos_actualizada = []
    
    existe=buscar_id(rut)
    
    if existe != -1:
        # Abrimos el archivo en modo lectura
        with open(archivo, 'r') as file:
            # Leemos cada línea del archivo
            for linea in file:
                # Eliminamos los espacios en blanco y los saltos de línea
                linea = linea.strip()
                # Dividimos la línea por comas
                datos = linea.split(',')
                # Verificamos si el RUT no coincide con el RUT a eliminar
                if datos[0] != rut:
                    # Si no coincide, añadimos el registro a la lista actualizada
                    lista_datos_actualizada.append(linea)
                #else:
                #    sw=0 #rut no existe
        
        # Abrimos el archivo en modo escritura para actualizar el contenido
        with open(archivo, 'w') as file:
            # Escribimos cada registro actualizado en el archivo
            for linea in lista_datos_actualizada:
                file.write(linea + '\n')
        return 1 #eliminado    
    else:
        return -1




opcion=0
while opcion != 5:
    os.system("cls")
    print("""
           SISTEMA DE VENTAS
    ------------------------------
    1. Vender productos
    2. Reportes.
    3. Mantenedores
    4. Administración de productos
    5. Salir
    """)

    opcion = int(input("Ingrese una opción entre 1-5: "))

    if opcion == 1:
        os.system("cls")
        print(" Vender productos \n")
        id_producto = input("Ingrese ID del producto: ")
        indice_producto = buscar_id(id_producto)

        if indice_producto != -1:
            print("Producto encontrado en el índice", indice_producto)
            producto = productos[indice_producto:indice_producto + 5]
            print(f"Producto: {producto[1]} {producto[2]}")
            precio_unitario = producto[3]
            stock_disponible = producto[4]
            cantidad = int(input("Ingrese cantidad a comprar: "))

            if cantidad <= stock_disponible:
                print("Stock disponible.")
                total = cantidad * precio_unitario
                print(f"Total a pagar por {cantidad} productos: ${total}")
                respuesta = input("¿Desea realizar la compra? (s/n): ")

                if respuesta.lower() == "s":
                    productos[indice_producto + 4] -= cantidad 
                    
                    nuevo_folio = get_folio()
                    fecha_actual = "28-06-2024"
                    
                    ventas.append([nuevo_folio, fecha_actual, id_producto, cantidad, total])
                    print("¡Venta registrada!")
                    input("Presione Enter para continuar...")
            else:
                print("No hay suficiente stock para realizar la venta.")
                input("Presione Enter para continuar...")
        else:
            print(f"Producto con ID '{id_producto}' no encontrado.")
            input("Presione Enter para continuar...")

    elif opcion == 2:
        while True:
            os.system("cls")
            print("""
                    REPORTES
            --------------------------
            1. General de ventas
            2. Ventas por fecha especifica (con total)
            3. Ventas por rango de fecha (con total)
            4. Salir al menu principal

            """)
            op = int(input("Ingrese una opción (1-4): "))

            if op == 1:
                total_ventas = sum(venta[4] for venta in ventas)
                print("Reporte General de Ventas")
                print("-------------------------")
                for venta in ventas:
                    print(f"Folio: {venta[0]}, Fecha: {venta[1]}, Producto: {venta[2]}, Cantidad: {venta[3]}, Total: ${venta[4]}")
                print(f"Total ventas: ${total_ventas}")
                input("Presione Enter para continuar...")

            elif op == 2:
                fecha = input("Ingrese fecha (dd-mm-yyyy): ")
                total_ventas_fecha = 0
                print(f"Reporte de Ventas para la fecha {fecha}")
                print("-------------------------------------")
                for venta in ventas:
                    if venta[1] == fecha:
                        total_ventas_fecha += venta[4]
                        print(f"Folio: {venta[0]}, Producto: {venta[2]}, Cantidad: {venta[3]}, Total: ${venta[4]}")
                print(f"Total ventas para la fecha {fecha}: ${total_ventas_fecha}")
                input("Presione Enter para continuar...")

            elif op == 3:
                fecha_inicio = input("Ingrese fecha de inicio (dd-mm-yyyy): ")
                fecha_fin = input("Ingrese fecha de fin (dd-mm-yyyy): ")
                total_ventas_rango = 0
                print(f"Reporte de Ventas para el rango {fecha_inicio} al {fecha_fin}")
                print("----------------------------------------------------")
                for venta in ventas:
                    if fecha_inicio <= venta[1] <= fecha_fin:
                        total_ventas_rango += venta[4]
                        print(f"Folio: {venta[0]}, Fecha: {venta[1]}, Producto: {venta[2]}, Cantidad: {venta[3]}, Total: ${venta[4]}")
                print(f"Total ventas para el rango {fecha_inicio} al {fecha_fin}: ${total_ventas_rango}")
                input("Presione Enter para continuar...")

            elif op == 4:
                break

            else:
                print("Opción no válida. Intente nuevamente.")
                input("Presione Enter para continuar...")

    elif opcion == 3:
        while True:
            os.system("cls")
            print("Menú de Mantenedores de Productos")
            print("---------------------------------")
            print("1. Agregar producto")
            print("2. Buscar producto por código")
            print("3. Eliminar producto por código")
            print("4. Modificar producto por código")
            print("5. Listar todos los productos")
            print("6. Salir al menú principal")
            print("---------------------------------")

            opcion_2 = int(input("Ingrese una opción [1-6]: "))

            if opcion_2 == 1:
                print("\nAgregar Producto\n")
                id = input("Ingrese código de producto: ")
                marca = input("Ingrese marca del producto: ")
                modelo = input("Ingrese modelo del producto: ")
                precio = int(input("Ingrese precio del producto: "))
                stock = int(input("Ingrese stock del producto: "))
                productos.extend([id, marca, modelo, precio, stock])
                print("\nProducto agregado correctamente.")
                input("Presione Enter para continuar...")

            elif opcion_2 == 2:
                print("\nBuscar Producto por ID\n")
                id = input("Ingrese código de producto: ")
                indice_producto = buscar_id(id)
                if indice_producto != -1:
                    print("Producto encontrado en el índice", indice_producto)
                    print(f"Producto: {productos[indice_producto + 1]} {productos[indice_producto + 2]}")
                    input("Presione Enter para continuar...")
                else:
                    print(f"Producto con ID '{id}' no encontrado.")
                    input("Presione Enter para continuar...")

            elif opcion_2 == 3:
                print("\nEliminar Producto por ID\n")
                id = input("Ingrese código de producto: ")
                indice_producto = buscar_id(id)
                if indice_producto != -1:
                    productos.pop(indice_producto + 4)
                    productos.pop(indice_producto + 3)
                    productos.pop(indice_producto + 2)
                    productos.pop(indice_producto + 1)
                    productos.pop(indice_producto)
                    print(f"Producto con ID '{id}' eliminado correctamente.")
                    input("Presione Enter para continuar...")
                else:
                    print(f"Producto con ID '{id}' no encontrado.")
                    input("Presione Enter para continuar...")

            elif opcion_2 == 4:
                print("\nModificar Producto por ID\n")
                id = input("Ingrese código de producto: ")
                indice_producto = buscar_id(id)
                if indice_producto != -1:
                    print("Producto encontrado en el índice", indice_producto)
                    print("Datos actuales del producto:")
                    print(f"Código: {productos[indice_producto]}")
                    print(f"Marca: {productos[indice_producto + 1]}")
                    print(f"Modelo: {productos[indice_producto + 2]}")
                    print(f"Precio: ${productos[indice_producto + 3]}")
                    print(f"Stock: {productos[indice_producto + 4]}")
                    
                    nueva_marca = input("Ingrese nueva marca (Enter para mantener): ")
                    nuevo_modelo = input("Ingrese nuevo modelo (Enter para mantener): ")
                    nuevo_precio = input("Ingrese nuevo precio (Enter para mantener): ")
                    nuevo_stock = input("Ingrese nuevo stock (Enter para mantener): ")

                    if nueva_marca:
                        productos[indice_producto + 1] = nueva_marca
                    if nuevo_modelo:
                        productos[indice_producto + 2] = nuevo_modelo
                    if nuevo_precio:
                        productos[indice_producto + 3] = int(nuevo_precio)
                    if nuevo_stock:
                        productos[indice_producto + 4] = int(nuevo_stock)

                    print("Producto modificado correctamente.")
                    input("Presione Enter para continuar...")
                else:
                    print(f"Producto con ID '{id}' no encontrado.")
                    input("Presione Enter para continuar...")

            elif opcion_2 == 5:
                print("\nListado de Productos\n")
                productos = leer_datos_archivo(archivo)
                imprimir_datos(productos)
                input("Presione Enter para continuar...")

            elif opcion_2 == 6:
                break

            else:
                print("Opción no válida. Intente nuevamente.")
                input("Presione Enter para continuar...")

    elif opcion == 4:
         """

        1.cargar datos
        2.respaldar datos
        3.salir

        cargar datos: esto lee todo lo que contiene los archivos productos.txt y 
                     ventas.txt y carga las listas productos y ventas

        respaldar datos: esta opcion graba  (actualiza) todo los contenidos en las listas productos y ventas en los archivos txt correspondiente

        observaciones 1. debe tener que si su lista de productos y ventas ya tienen datos no debe cargar datos desde los txt.
        
    """
    os.system("cls")
    print("ADMINISTRACIÓN DE PRODUCTOS")
    print("---------------------------")
    print("1. Cargar datos de productos desde archivo")
    print("2. Respaldar datos de productos a archivo")
    print("3. Observaciones 1")
    print("4. Regresar al menú principal")
    print("---------------------------")

    opcion_3 = int(input("Ingrese una opción [1-4]: "))
    
    if opcion_3 == 1: pass
    elif opcion_3 == 2: 
        with open(archivo, 'w') as file:
            # Escribimos cada registro actualizado en el archivo
            for linea in archivo:
                file.write(linea + '\n')
        with open(ventas,'w') as file:
            for linea in ventas:
                file.write(linea + '\n')
        print("Respaldo de los archivos guardados")
        input("Ingrese una tecla para continuar")
    elif opcion_3 == 3: pass
    elif opcion_3 == 4:
        break
    
    
""""
    …or create a new repository on the command line
echo "# menuzpatillas" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/jimmy1817/menuzpatillas.git
git push -u origin main



…or push an existing repository from the command line
git remote add origin https://github.com/jimmy1817/menuzpatillas.git
git branch -M main
git push -u origin main


"""