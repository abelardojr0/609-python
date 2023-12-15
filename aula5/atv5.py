par_impar = lambda numero : f"O {numero} é par" if numero % 2 == 0 else f"O {numero} é ímpar"


numero = int(input("Digite um número: "))

print(par_impar(numero=numero))