semaforo = lambda cor : "acelere" if cor == "verde" else "pare" if cor == "vermelho" else "atenção" if cor == "amarelo" else "opção inválida"


cor = str(input("Digite uma cor: "))

print(semaforo(cor=cor))