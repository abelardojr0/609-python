numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

resultado = 0

operacao = int(input("""
            Escolha uma operação:
            1 - Somar
            2 - Subtrair
            3 - Multiplicar
            4 - Dividir
"""))

match operacao:
    case 1:
        resultado = numero1 + numero2
    case 2:
        resultado = numero1 - numero2
    case 3:
        resultado = numero1 * numero2
    case 4:
        resultado = numero1 / numero2
    case _:
        print("Operação Inválida")

if resultado % 2 == 0:
    print(f"{resultado} é par")
else:
    print(f"{resultado} é ímpar")

if resultado > 0:
    print(f"{resultado} é positivo")
elif resultado < 0:
    print(f"{resultado} é negativo")
else:
    print(f"{resultado} é neutro")







