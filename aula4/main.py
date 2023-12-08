def cumprimento(horario, nome):
    if horario >= 5 and horario <= 12:
        return f"Bom dia, {nome}"
    elif horario > 12 and horario < 18:
        return f"Bom tarde, {nome}"
    else:
        return f"Bom noite, {nome}"
    


hora_atual = int(input("Digite a hora atual: "))
nome = str(input("Digite seu nome: "))
print(cumprimento(hora_atual, nome))