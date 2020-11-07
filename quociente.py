def distribuir_vagas(vagas_por_partido, votos, vagas_remanescentes):
    if vagas_remanescentes == 0:
        return vagas_por_partido

    partido_com_mais_votos = 0
    maior_num_votos = 0
    for i in range(len(vagas_por_partido)):
        if vagas_por_partido[i] == 0:
            continue
        if (votos[i]/(vagas_por_partido[i] + 1)) > maior_num_votos:
            partido_com_mais_votos = i
            maior_num_votos = (votos[i]/(vagas_por_partido[i] + 1))

    vagas_por_partido[partido_com_mais_votos] += 1
    vagas_remanescentes -= 1

    return distribuir_vagas(vagas_por_partido, votos, vagas_remanescentes)


def solucao():
    num_vagas, num_partidos = [int(x) for x in input().split(" ")]
    votos = []
    for i in range(num_partidos):
        votos.append(int(input()))

    quociente = round(sum(votos)/num_vagas)

    vagas_por_partido = []

    for part in votos:
        vagas_por_partido.append(part//quociente)

    vagas_por_partido = distribuir_vagas(
        vagas_por_partido, votos, num_vagas - sum(vagas_por_partido))

    print('{} {}'.format(sum(votos), quociente))

    for i in range(num_partidos):
        print('Partido {}: {}'.format(i+1, vagas_por_partido[i]))


solucao()
