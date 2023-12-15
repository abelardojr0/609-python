def calcular_area_retangulo(comp, larg):
    return comp * larg

comprimento = float(input("Digite o comprimento do retângulo:"))
largura = float(input("Digite a largura do retângulo: "))

area = calcular_area_retangulo(comp=comprimento, larg=largura)

print(f"A área do retângulo é {area:.2f}")