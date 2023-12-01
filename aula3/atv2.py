modelo_pessoa_serasa = {
    "nome": str(input("Digite o nome da pessoa: ")),
    "cpf": str(input("Digite seu cpf: ")),
    "valor": 50000,
    "endereco": "rua logo ali, 50"
}

modelo_pessoa_serasa["valor"] = 20000
modelo_pessoa_serasa["RG"] = int(input("Digite seu RG: "))

print(modelo_pessoa_serasa)

if modelo_pessoa_serasa["valor"] > 30000:
    print("Ta lascado")
else:
    print("Ta de boa")