def calcular_media(av1, av2, av3):
    #Calcula a media das tres avaliacoes, com uma casa decimal.
    return round((av1 + av2 + av3) / 3, 1)


def situacao(media):
    #Diz a situacao do aluno a partir da media.
    
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado" #reprovado