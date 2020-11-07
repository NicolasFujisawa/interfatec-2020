def solution():
    answer = []
    while True:
        [altura, comprimento, largura] = [
            float(value) for value in input().split(" ")]
        if(altura == 0 and comprimento == 0 and largura == 0):
            break
        inclinacao = altura * 100 / comprimento
        if round(inclinacao, 2) > 8.33 or largura < 0.8:
            answer.append("PROJETO ESPECIAL")
        else:
            answer.append("PROJETO SIMPLES")
    print("\n".join(answer))


solution()
