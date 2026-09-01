numero,hexadeciamal=30,""
if numero==0:print("0")
while numero>0:
    residuo=numero%16
    if residuo==10:
            hexadeciamal="A"+hexadeciamal
    elif residuo==11:
            hexadeciamal="B"+hexadeciamal
    elif residuo==12:
            hexadeciamal="C"+hexadeciamal
    elif residuo==13:
            hexadeciamal="D"+hexadeciamal
    elif residuo==14:
            hexadeciamal="E"+hexadeciamal
    elif residuo==15:
            hexadeciamal="F"+hexadeciamal
    else:hexadeciamal= str(residuo)+hexadeciamal
    numero=numero//16
print(hexadeciamal)