# Tasas fijas de conversión
dolar = 0.00025
euro = 0.00023
yen = 0.037

# Pedir cantidad en pesos colombianos
pesos = float(input("Escribe la cantidad en pesos colombianos: "))

# Calcular conversiones
usd = pesos * dolar
eur = pesos * euro
jpy = pesos * yen

# Mostrar resultados
print("Dólares:", usd)
print("Euros:", eur)
print("Yenes:", jpy)
