# treinamento OBI - visita.py
qtd_cidades, origem, destino = str(input()).split(" ")
distancia_total = 0
cidades_passadas = [int(origem), int(destino)]
mapa = []
ligadas_origem = []
ligadas_destino = []
proximas = []
intermediarios = []
for cidades_restantes in range(1, int(qtd_cidades)):
    c1, c2, distancia = str(input()).split(" ")
    temp = [int(c1), int(c2), int(distancia)]
    mapa.append(temp)
destino = int(destino)
origem = int(origem)
atual = origem
for city in mapa:
    if city[0] == origem and city[1] == destino or city[1] == origem and city[0] == destino:
        distancia_total = city[2]
        break
    elif city[0] == origem or city[1] == origem:
        ligadas_origem.append(city)
        mapa.remove(city)
    elif city[0] == destino or city[1] == destino:
        ligadas_destino.append(city)
        mapa.remove(city)
for cidades_restantes in mapa:
    for ligacao_origem in ligadas_origem:
        if cidades_restantes[0] == ligacao_origem[0] or cidades_restantes[0] == ligacao_origem[1]:
            proximas.append(cidades_restantes)
            mapa.remove(cidades_restantes)
        elif cidades_restantes[1] == ligacao_origem[0] or cidades_restantes[1] == ligacao_origem[1]:
            proximas.append(cidades_restantes)
            mapa.remove(cidades_restantes)    
    for ligacao_destino in ligadas_destino:
        if cidades_restantes[0] == ligacao_destino[0] or cidades_restantes[0] == ligacao_destino[1]:
            proximas.append(cidades_restantes)
            mapa.remove(cidades_restantes)
        elif cidades_restantes[1] == ligacao_destino[0] or cidades_restantes[1] == ligacao_destino[1]:
            proximas.append(cidades_restantes)
            mapa.remove(cidades_restantes)
for proximas_a in proximas:
    for ultimas_cidades in mapa:
        if proximas_a[0] == ultimas_cidades[0] or proximas_a[0] == ultimas_cidades[1]:
            intermediarios.append(ultimas_cidades)
            mapa.remove(ultimas_cidades)    
        elif proximas_a[1] == ultimas_cidades[0] or proximas_a[1] == ultimas_cidades[0]:
            intermediarios.append(ultimas_cidades)
            mapa.remove(ultimas_cidades)
