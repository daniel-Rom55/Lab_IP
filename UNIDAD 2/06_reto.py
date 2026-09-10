total = float(input("ingresa el total de la cuenta:"))
propina = float(input("ingresa porcentaje de propina::"))
personas=int(input("total de personas que van a pagar la cuenta:"))

propina=total*(propina/100)
totalconpropina= total+propina
total_por_persona= totalconpropina/personas

print(f"total de la cuenta: {total: .2f}")
print(f"total con propina: {totalconpropina: .2f}")
print(f"total por persona: {total_por_persona: .2f}")