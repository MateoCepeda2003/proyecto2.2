import registro_camper

def main_menu():
    print("\nBienvenido al sistema de gestión de CampusLands")
    print("Seleccione una opción:")
    print("1. Coordinación")
    print("2. Gestión de entrenadores")
    print("3. Informes")
    print("4. Salir")

    while True:
        try:
            choice = int(input("Ingrese el número de su opción: "))
        except ValueError:
            print("Opción inválida. Por favor, ingrese un número válido.")
            continue

        if choice == 1:
            coordination_menu()
        elif choice == 2:
            trainers_menu()
        elif choice == 3:
            reports_menu()
        elif choice == 4:
            print("Gracias por usar CampusLands, hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

def coordination_menu():
    print("\nOpciones de coordinación:")
    print("1. registrar camper")
    print("2. evaluar camper")
    print("3. eliminar camper")
    print("4. Volver al menú principal")

    while True:
        try:
            option = int(input("Ingrese el número de la opción deseada: "))
        except ValueError:
            print("Opción inválida. Por favor, ingrese un número válido.")
            continue

        if option == 1:
            # Implementar función para crear camper aqui
            documento= input("ingrese el numero de documento ")
            nombre = input("Ingrese el nombre del camper: ")
            apellido = input("Ingrese el apellido del camper: ")
            direccion = input("Ingrese la dirección del camper: ")
            acudiente = input("Ingrese el nombre del acudiente del camper: ")
            telefonos_contacto = input("Ingrese los teléfonos de contacto: ")
            estado = input("Ingrese el estado del camper: ")
            riesgo = input("Ingrese el riesgo del camper: ")

            registro_camper.crear_camper_con_validacion( nombre, apellido, direccion, acudiente, telefonos_contacto, estado, riesgo,documento)
        elif option == 2:
            # Implementar función para evaluar camper aqui
            pass
        elif option == 3:
            # Implementar funcion para eliminar camper aqui
            pass
        elif option == 4:
            main_menu()
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

def trainers_menu():
    # Implementar opciones de gestión de entrenadores aquí
    pass

def reports_menu():
    # Implementar opciones de informes aquí
    pass

if __name__ == "__main__":
    main_menu()