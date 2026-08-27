n = int(input("Introduce un numero: "))
if n<=1:
    print("El numero no es primo")
i=2
while i<n:
    if n%i==0:
        print("El numero no es primo")
        break
    i+=1
else:
    print("El numero es primo")
    