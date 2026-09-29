def consultar_saldo():
    print("saldo: 0.00")
def depositar():
    print("deposito realizado")
def retirar():
    print("retiro realizado")
def salir():
    print("saliendo del cajero")

while True:
    print("1. consultar saldo")
    print("2. depositar")
    print("3. retirar")
    print("4. salir")

    opcion= input("opcion:")
    if opcion == "1":
        consultar_saldo()
    elif opcion == "2":
        depositar()
    elif opcion=="3":
        retirar()
    elif opcion == "4":
        salir() 
        break
    else:
      print("opcion no valida")
