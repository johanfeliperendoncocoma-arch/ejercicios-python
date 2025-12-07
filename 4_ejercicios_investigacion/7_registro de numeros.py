numeros = []
print("Ingresa números positivos (0 para terminar):")
while True:
    n = int(input("Número: "))
    if n == 0:
        break
    if n > 0:
        numeros.append(n)
print("Cantidad de números ingresados:", len(numeros))
suma_total = sum(numeros)
print("Suma total:", suma_total)
suma_pares = 0
cantidad_pares = 0
for num in numeros:
    if num % 2 == 0:
        suma_pares += num
        cantidad_pares += 1
if cantidad_pares > 0:
    promedio_pares = suma_pares / cantidad_pares
    print("Promedio de números pares:", round(promedio_pares, 2))
else:
    print("No se ingresaron números pares.")
