import math

def calcular_latas_tinta(area):
    # Cada lata de tinta cobre 54 metros quadrados (18 litros * 3 metros quadrados por litro)
    metros_por_lata = 54
    # Arredonda para cima a quantidade de latas necessárias
    latas_necessarias = math.ceil(area / metros_por_lata)
    return latas_necessarias

def calcular_preco_total(latas_necessarias):
    preco_por_lata = 80.00
    preco_total = latas_necessarias * preco_por_lata
    return preco_total

def main():
    try:
        area_pintada = float(input("Digite o tamanho em metros quadrados da área a ser pintada: "))
        latas_necessarias = calcular_latas_tinta(area_pintada)
        preco_total = calcular_preco_total(latas_necessarias)

        print(f"Quantidade de latas de tinta necessárias: {latas_necessarias}")
        print(f"Preço total: R$ {preco_total:.2f}")

    except ValueError:
        print("Valor inválido. Certifique-se de digitar um número válido para a área.")

if __name__ == "__main__":
    main()
