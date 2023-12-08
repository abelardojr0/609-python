def contar_vogais(palavra):
    contador = 0

    for letra in palavra:
        if letra in 'aeiouáâãéêíóôõú':
            contador += 1

    return contador



texto = str(input("Digite um texto qualquer: "))
print(contar_vogais(palavra=texto))