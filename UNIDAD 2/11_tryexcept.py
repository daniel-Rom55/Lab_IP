while True:
    try:
        edad= int(input("Ingresa tu edad: "))
        if 0<=edad<=120:
            break
        else:
            print("Edad invalida. Intenta de nuevo.")
    except ValueError:
        print("Edad invalida. Intenta de nuevo.")
print(f"Edad registrada: {edad}")
    