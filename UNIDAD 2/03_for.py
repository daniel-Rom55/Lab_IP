for numero in range (0, 1000):
    cuadrado=numero**2
    print(numero, cuadrado)

materias =["python", "linux", "interfaces"]
for posicion, materia in enumerate(materias, start=1):
    print(f"{posicion} {materia}")

materias =["python", "linux", "interfaces"]

for materia in materias:
    print(materia)

cadena="peter"
for letra in cadena:
    print(letra)

cadena="1,2,3,4,5,6,7,8,9,A,B,C,D,E,F"
for letra in cadena:
    print(letra)


for i in range(len(cadena)):
    print(cadena[i])

for numero in range (0, 7, 2):
    cuadrado=numero**2
    print(numero, cuadrado)
