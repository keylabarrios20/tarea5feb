import random

# Definir los límites para el número aleatorio
a = 1
b = 100

# Generar número aleatorio dentro del rango [a, b]
numero_aleatorio = random.randint(a, b)

# el número aleatorio 
print(numero_aleatorio)

# variable intentos
intentos = 0

# bienvenida
print("¡Bienvenido a Adivina el número!! Empecemos..")

# Ciclo while para adivinar el número
while True:
    intentos += 1

    # Pedir al usuario que ingrese un número
    numero_usuario = int(input("Ingresa un número entre 1 y 100: "))

    # Comprobar si el número es igual al número secreto
    if numero_usuario == numero_aleatorio:
        print(f"¡Felicidades! ¡Adivinaste el número en {intentos} intentos!")
        break
    elif numero_usuario < numero_aleatorio:
        print("El número es demasiado bajo. Intenta de nuevo.")
    else:
        print("El número es demasiado alto. Intenta de nuevo.")

# mensaje de despedida y número secreto
print(f"¡Gracias por jugar! El número secreto era: {numero_aleatorio}")
