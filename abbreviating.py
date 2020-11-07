def solution():
    nomes = []
    while True:
        text = ''
        try:
            text = input()
        except:
            break
        nome = text.split(" ")
        n = len(nome)
        answer = []
        answer.append(nome[0])
        for i in range(1, n - 1):
            answer.append('{nome}.'.format(nome=nome[i][:1]))
        if len(nome) > 1:
            answer.append(nome[-1])
        result = " ".join(answer)
        nomes.append(result)
    nomes.sort()
    print("\n".join(nomes))


solution()
