



# lista_de_numeros = [1,4,9,5,2,7]

# lista_dos_pares = []

# for numero in lista_de_numeros:
#     if numero % 2 == 0:
#         lista_dos_pares.append(numero)

# print(lista_dos_pares)



lista_de_numeros = [1,4,9,5,2,7]
lista_dos_pares = list(filter(lambda numero : numero % 2 == 0, lista_de_numeros))
