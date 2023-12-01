frutas = []

for i in range(1,6):
    fruta = str(input(f"Digite a {i}ª fruta: "))
    preco = float(input(f"Digite o preco da {fruta}"))
    frutas.append({
        "nome": fruta,
        "preço": preco
    })

print(frutas)
