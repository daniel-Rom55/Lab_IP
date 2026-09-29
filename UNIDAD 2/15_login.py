MAX=3
for intento in range (1, MAX+1):
    usuario=input ("Usuario: ").strip().lower()
    clave= input ("contraseña: ")
    
    if usuario=="daniel" and clave == "dani":
        print ("bienvenido ")
        break
    print("credenciales incorrectas")
else:
    print("acceso bloqueado")
