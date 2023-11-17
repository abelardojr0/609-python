frase = str(input("Digite uma frase: "))

contador_vogais = 0

for letra in frase:
    if letra.lower() in 'aeiouáâãéêíàóõôú':
        contador_vogais += 1

print(f"A frase digitado contém {contador_vogais} de vogais")