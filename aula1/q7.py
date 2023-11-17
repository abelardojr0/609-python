import time

numero = int(input("Digite um número inteiro e positivo: "))

if numero > 0:
    for i in range(numero, -1, -1):
        print(i)
        time.sleep(1)
else:
    print("POSITIVOOO MEU FI, ACIMAAAAA DE 0")