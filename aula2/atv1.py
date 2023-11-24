# frutas = ["banana", "mamão", "maça", "abacaxi"]


# for i in range(1,5):
#     fruta_nova = str(input(f"Digite a {i}ª fruta: "))
#     frutas.append(fruta_nova)


# print(frutas)






frutas = ["banana", "mamão", "maça", "abacaxi"]

indice = 1
while True:
    fruta_nova = str(input(f"Digite a {indice}ª fruta: "))

    indice += 1

    if fruta_nova == "sair":
        break

    frutas.append(fruta_nova)

print(frutas)