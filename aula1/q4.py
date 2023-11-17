letra = str(input("Digite uma letra do alfabeto: ")).lower().strip()


if len(letra) == 1:
    if letra in 'aeiou':
        print(f"'{letra}' é uma vogal")
    elif letra in 'bcdfghjklmnpqrstvxywz':
        print(f"'{letra}' é uma consoante")
    else:
        print("Digite uma letra do alfabeto")
else:
    print("Digite apenas uma letra")
