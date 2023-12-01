lista_de_itens = []

while True:
    nome_produto = str(input("Digite o nome do produto: "))
    if nome_produto == "sair":
        break
    valor_produto = float(input("Digite o valor do produto: "))

    lista_de_itens.append({
        "nome": nome_produto,
        "preço": valor_produto
        })
    
print(lista_de_itens)