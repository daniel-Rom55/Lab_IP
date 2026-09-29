USUARIO= "alumno"
CLAVE= "python"

usuario= input("usuario: ").strip().lower()
clave=input("contraseña: ")

if usuario == USUARIO and clave == CLAVE:
    print("bienvenido")
else:
    print("contraseña incorrecta")