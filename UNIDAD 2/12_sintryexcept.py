while True:
    edad=int(input("Ingresa tu edad: "))
    if not type (edad) == int:
        print("escrube un numero entero valido:")
    if 0<=edad<=120:
        break
    else:
        print("Edad invalida. Intenta de nuevo.")
print(f"Edad registrada: {edad}")