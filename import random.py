import random

palabras = ["futbol", "peliculas", "verde", "nacional", "socios", "universidad"]
palabra_secreta = random.choice(palabras)
letras_adivinadas = []
vidas = 5

print ('welcome')

while vidas > 0:
    mensaje = ''
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            mensaje += letra
        else:
            mensaje +='_ '

    print(f"palabra actual: {mensaje}")

    if "_ " not in mensaje:
        print ("congratulations")
        break 

    print(f"tus vidas son: {vidas}")

    intento = input ("ingrese una letra:"). lower()

    if intento in letras_adivinadas:
        print("intente con otra letra")
    elif intento in palabra_secreta:
        print ("muy bien la letra esta en la palabra")
        letras_adivinadas.append(intento)
    else: 
        print("incorrecto pierde vida")
        letras_adivinadas.append(intento)
        vidas -=1 