contactos = []
opcion = ""
while opcion != "5":
    print("\n--- MENÚ ---")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Eliminar contacto")
    print("4. Ver todos los contactos")
    print("5. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        nombre = input("Nombre: ")
        telefono = input("Teléfono: ")
        correo = input("Correo: ")
        contacto = {"nombre": nombre, "telefono": telefono, "correo": correo}
        contactos.append(contacto)
        print("Contacto guardado.")

    elif opcion == "2":
        buscar = input("Nombre a buscar: ")
        encontrado = False
        for c in contactos:
            if c["nombre"] == buscar:
                print("Nombre:", c["nombre"])
                print("Teléfono:", c["telefono"])
                print("Correo:", c["correo"])
                encontrado = True
        if not encontrado:
            print("No se encontró el contacto.")

    elif opcion == "3":
        eliminar = input("Nombre a eliminar: ")
        for c in contactos:
            if c["nombre"] == eliminar:
                contactos.remove(c)
                print("Contacto eliminado.")
                break
        else:
            print("No se encontró el contacto.")

    elif opcion == "4":
        if len(contactos) == 0:
            print("No hay contactos.")
        else:
            for c in contactos:
                print("Nombre:", c["nombre"], "| Teléfono:", c["telefono"], "| Correo:", c["correo"])

    elif opcion == "5":
        print("Saliendo del programa...")

    else:
        print("Opción no válida.")
