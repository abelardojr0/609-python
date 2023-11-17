numero1 = int(input("Digite o primeiro valor: "))
numero2 = int(input("Digite o segundo valor: "))

if numero1 > numero2:
    print(f"O {numero1} é maior que o {numero2}")
elif numero2 > numero1:
    print(f"O {numero2} é maior que o {numero1}")
else:
    print("Os números são iguais")
