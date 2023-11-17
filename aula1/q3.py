sexo = str(input("Digite seu sexo [M | F]: ")).upper().strip()

if len(sexo) == 1:
    if sexo == "F":
        print("F - Feminino")
    elif sexo == "M":
        print("M - Masculino")
    else:
        print("Escolha inválida")
else:
    print("Digite apenas uma letra")