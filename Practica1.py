def adivina_el_numero():
    numero_secreto = 54

    nombre = input("Por favor, ingrese su nombre: ")
    apellido = input("Por favor, ingrese su apellido: ")
    edad = input("Por favor, ingrese su edad: ")

    intento = int(input(f"Hola {nombre} {apellido}, ingresa un número para adivinar el número secreto: "))

    if intento == numero_secreto:
        print(f"¡Felicidades {nombre} {apellido}! Has acertado el número secreto, que era {numero_secreto}.")
    else:
        print(f"Gracias por participar, {nombre} {apellido}. El número ingresado no es el correcto.")

adivina_el_numero ()

   
