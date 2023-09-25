# treinamento OBI - sapo.py

qtd_colunas, qtd_linhas = [int(a) for a in input().split()]
qtd_pedras = int(input())
temp_lago =[]
pedras = []
lago = []


for linha in range(1, qtd_linhas + 1):
    for coluna in range(1, qtd_colunas + 1):
        pos = coluna, linha
        temp_lago.append(pos)
    lago.append(temp_lago.copy())
    temp_lago.clear()



for i in range(0, qtd_pedras):
    col, lin = [int(b) for b in input().split()]
    pos_pedra = [col, lin]
    pedras.append(pos_pedra)

print(pedras)

for pedra in range(0, len(pedras) + 1):
    for pos in range(0, len(pedra) + 1):
        print(pos)

sapo = [int(c) for c in input().split()]
namorada = [int(d) for d in input().split()]


"""for pedra in pedras:
    if pedra == "p":
        if pedra[]
"""
