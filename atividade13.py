peso = float(input("Informe o peso de peixes em quilos: "))
limite = 50
excesso = max(0, peso - limite)
multa = excesso * 4.00

print(f"Peso de peixes: {peso:.2f} kg")
if excesso > 0:
    print(f"Peso excedente: {excesso:.2f} kg")
    print(f"Valor da multa: R$ {multa:.2f}")
else:
    print("Não houve excesso de peso. Nenhuma multa será aplicada.")