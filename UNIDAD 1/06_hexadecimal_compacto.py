numero, hexadecimal = 30, ""

while numero > 0:
    residuo = numero % 16
    hexadecimal = "0123456789ABCDEF"[residuo] + hexadecimal
    numero //= 16

print(hexadecimal)