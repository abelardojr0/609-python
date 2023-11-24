produtos = [
    ("Maçã", 2.50),
    ("Banana", 1.75),
    ("Laranja", 3.00)
]
soma = 0
for item_atual in produtos:
    soma = soma + item_atual[1]

print(soma)