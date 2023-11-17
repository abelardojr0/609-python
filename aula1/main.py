ano = int(input("Digite o ano que você nasceu: "))

idade = 2023 - ano

if idade >= 0:
    if idade >= 18:
        print("Você já pode ser preso")
    else:
        print("Você ainda ta de boa com a vida")
else:
    print("Digite um ano válido")