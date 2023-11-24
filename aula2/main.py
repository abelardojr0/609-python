serasa = [ 
    ["Abel", 7000],
    ["Gustavo", 3000],
    ["Sid", 20000], 
    ["João", 8000],
    ["Maria", 2000],
    ["Ana", 30000]
]

lista_dos_perdoados = []

for item_atual in serasa:
    if item_atual[1] < 5000:
        lista_dos_perdoados.append(item_atual)

print(lista_dos_perdoados)