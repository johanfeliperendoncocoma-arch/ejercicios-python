archivo = open("nombres.txt", "w")
n = int(input("¿Cuántos nombres vas a ingresar? "))

for i in range(n):
    nombre = input("Nombre: ")
    archivo.write(nombre + "\n")

archivo.close()

archivo = open("nombres.txt", "r")
print("\n--- NOMBRES GUARDADOS ---")
for linea in archivo:
    print(linea.strip())

archivo.close()
