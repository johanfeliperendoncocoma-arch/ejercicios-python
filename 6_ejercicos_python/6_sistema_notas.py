archivo = open("notas.txt", "w")
n = int(input("Cuántos estudiantes vas a ingresar: "))
for i in range(n):
    nombre = input("Nombre: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))
    prom = (nota1 + nota2 + nota3) / 3
    archivo.write(nombre + "," + str(prom) + "\n")
archivo.close()
archivo = open("notas.txt", "r")
print("\n--- REPORTE ---")
for linea in archivo:
    partes = linea.strip().split(",")
    nombre = partes[0]
    promedio = float(partes[1])
    if promedio >= 3.0:
        print(nombre, "Aprobado")
    else:
        print(nombre, "Reprobado")
archivo.close()
