import random

# El programa elige un número aleatorio entre 1 y 50
numero_secreto = random.randint(1, 50)

# Inicializamos el contador de intentos
intentos = 0

print("¡Bienvenido al juego de adivinanza!")
print("Estoy pensando en un número entre 1 y 50...")

# Bucle para que el usuario intente adivinar
while True:
    # El usuario ingresa un número
    intento = int(input("Ingresa tu número: "))
    intentos += 1  # Aumentamos el contador

    # Verificamos si el número es correcto
    if intento == numero_secreto:
        print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
        break  # Salimos del bucle
    elif intento < numero_secreto:
        print("Demasiado bajo. Intenta de nuevo.")
    else:
        print("Demasiado alto. Intenta de nuevo.")