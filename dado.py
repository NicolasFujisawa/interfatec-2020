def solution():
    jogadas = int(input())
    dados = [int(x) for x in input().split(" ")]
    luiza = 0
    antonio = 0
    luiza_vez = True
    for i in range(0, jogadas):
        dado = dados[i]
        if(luiza_vez):
            if(dado != 6):
                luiza_vez = False
            luiza += dado
        else:
            if(dado != 6):
                luiza_vez = True
            antonio += dado

    if(antonio > luiza):
        print('ANTONIO {antonio}'.format(antonio=antonio))
    elif(luiza > antonio):
        print('LUISA {luiza}'.format(luiza=luiza))
    else:
        print('EMPATE {luiza}'.format(luiza=luiza))


solution()
