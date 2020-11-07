def moda(conjunto):
    most_occur = 0
    mode = []
    freq = {}
    for val in conjunto:
        if val in freq:
            freq[val] += 1
        else:
            freq[val] = 1

    for k, v in freq.items():
        if v > most_occur:
            most_occur = v

    for k, v in freq.items():
        if v == most_occur:
            mode.append(k)

    mode.sort()
    return mode


def media(conjunto):  # e1 +..en / 2
    return sum(conjunto) / len(conjunto)


def mediana(conjunto):
    n = len(conjunto)
    conj_sorted = sorted(conjunto)
    if(n % 2 == 0):
        return (conj_sorted[n // 2 - 1] + conj_sorted[n // 2]) / 2
    else:
        return conj_sorted[n // 2]


def entradas():
    number_of_students = 0
    entradas = []
    entrada = []
    while True:
        number = ''
        try:
            number = input()
        except:
            entradas.append(entrada)
            break
        if number_of_students == 0:
            number_of_students = int(number)
            if entrada:
                entradas.append(entrada)
                entrada = []
        else:
            number_of_students -= 1
            entrada.append(int(number))

    return entradas


def saida(resultados):
    print('MODA={}'.format(",".join([str(x) for x in resultados[0]])))
    print('MEDIA={:.2f}'.format(resultados[1]))
    print('MEDIANA={:.2f}'.format(resultados[2]))


def solucao():
    entradas_list = entradas()
    for entrada in entradas_list:
        med = media(entrada)
        mod = moda(entrada)
        medi = mediana(entrada)

        saida([mod, med, medi])


solucao()
