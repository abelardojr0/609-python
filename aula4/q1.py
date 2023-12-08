def cumprimento(horario):
    if horario >= 5 and horario <= 12:
        return "Bom dia"
    elif horario > 12 and horario < 18:
        return "Boa tarde"
    else:
        return "Boa noite"
    


hora_atual = int(input("Digite a hora atual: "))
print(cumprimento(hora_atual))