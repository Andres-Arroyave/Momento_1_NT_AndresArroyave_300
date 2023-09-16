# Base de datos de usuarios (Número de tarjeta usuario, nombre usuario, contraseña)
usuarios = []

# Base de datos de bicicletas (Número de ID)
bicicletas = [1, 2, 3, 4, 5]

# Diccionario para realizar un seguimiento del estado de las bicicletas (ID de bicicleta -> Estado)
estado_bicicletas = {}

def registrar_usuario():
    num_tarjeta = input("Ingrese el número de tarjeta del usuario: ")
    nombre = input("Ingrese el nombre del usuario: ")
    contraseña = input("Ingrese la contraseña del usuario: ")
    usuarios.append({'numero_tarjeta': num_tarjeta, 'nombre': nombre, 'contraseña': contraseña})
    print("Usuario registrado con éxito.")

def iniciar_sesion():
    num_tarjeta = input("Ingrese el número de tarjeta: ")
    contraseña = input("Ingrese la contraseña: ")
    for usuario in usuarios:
        if usuario['numero_tarjeta'] == num_tarjeta and usuario['contraseña'] == contraseña:
            return True
    return False

def prestar_bicicleta():
    if not iniciar_sesion():
        print("Inicio de sesión fallido. Verifique el número de tarjeta y la contraseña.")
        return
    if bicicletas:
        print("Bicicletas disponibles:")
        for id_bicicleta in bicicletas:
            print(f"ID de bicicleta: {id_bicicleta}")
        
        id_bicicleta = int(input("Ingrese el ID de la bicicleta que desea prestar: "))
        
        if id_bicicleta in bicicletas:
            sede_prestamo = input("Ingrese la sede donde desea prestar la bicicleta (Medellin, Bello, Itagüí): ")
            if sede_prestamo in ["Medellin", "Bello", "Itagui", "Envigado"]:
                bicicletas.remove(id_bicicleta)
                estado_bicicletas[id_bicicleta] = {'estado': 'prestada', 'sede_prestamo': sede_prestamo}
                print(f"Bicicleta con ID {id_bicicleta} prestada con éxito en la sede {sede_prestamo}.")
            else:
                print("Sede no válida. Por favor, ingrese una sede válida.")
        else:
            print("ID de bicicleta no válido. Verifique el ID ingresado.")
    else:
        print("Todas las bicicletas están prestadas en este momento.")

def devolver_bicicleta():
    if not iniciar_sesion():
        print("Inicio de sesión fallido. Verifique el número de tarjeta y la contraseña.")
        return
    
    id_bicicleta = int(input("Ingrese el ID de la bicicleta que desea devolver: "))
    
    if id_bicicleta in estado_bicicletas and estado_bicicletas[id_bicicleta]['estado'] == 'prestada':
        sede_devolucion = input("Ingrese la sede donde desea devolver la bicicleta (Medellin, Bello, Itagüí): ")
        if sede_devolucion in ["Medellin", "Bello", "Itagui", "Envigado"]:
            bicicletas.append(id_bicicleta)
            estado_bicicletas[id_bicicleta] = {'estado': 'disponible', 'sede_devolucion': sede_devolucion}
            print(f"Bicicleta con ID {id_bicicleta} devuelta con éxito en la sede {sede_devolucion}.")
        else:
            print("Sede no válida. Por favor, ingrese una sede válida.")
    else:
        print("La bicicleta no se puede devolver. Verifique el ID o el estado.")


def consultar_usuarios():
    print("Listado de usuarios:")
    for usuario in usuarios:
        print(f"Número de tarjeta: {usuario['numero_tarjeta']}, Nombre: {usuario['nombre']}")

def consultar_bicicletas():
    print("Listado de bicicletas:")
    for id_bicicleta, estado in estado_bicicletas.items():
        print(f"ID: {id_bicicleta}, Estado: {estado}")

while True:
    print("\nMenú:")
    print("1. Registrar usuario")
    print("2. Iniciar sesión en la Plataforma")
    print("3. Prestar bicicleta")
    print("4. Devolver bicicleta")
    print("5. Consultar listado de usuarios Registrados")
    print("6. Consultar listado de bicicletas Prestadas")
    print("7. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == '1':
        registrar_usuario()
    elif opcion == '2':
        iniciar_sesion()
    elif opcion == '3':
        prestar_bicicleta()
    elif opcion == '4':
        devolver_bicicleta()
    elif opcion == '5':
        consultar_usuarios()
    elif opcion == '6':
        consultar_bicicletas()
    elif opcion == '7':
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
