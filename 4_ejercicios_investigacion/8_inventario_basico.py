inventario = []
n = int(input("¿Cuántos productos vas a ingresar? "))

for i in range(n):
    nombre = input("Nombre del producto: ")
    cantidad = int(input("Cantidad: "))
    producto = {"nombre": nombre, "cantidad": cantidad}
    inventario.append(producto)

print("\n--- INVENTARIO ---")
for item in inventario:
    print(item["nombre"], "-", item["cantidad"])
