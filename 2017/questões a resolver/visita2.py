# treinamento OBI - visita2.py

qtd_cidades, origem, destino = str(input()).split(" ")
atual = origem
distancia = 0
mapa = []


for n in range(1, int(qtd_cidades)):
    c1, c2, dt = str(input()).split(" ")
    mapa.append(c1)
    mapa.append(c2)
    mapa.append(int(dt))

contador = 0
while atual != destino:
    for cidade in range(0, len(mapa), 3):
    #    print(mapa[cidade], mapa[cidade + 1])
        contador += 1
        if mapa[cidade] == atual and mapa[cidade + 1] == destino:
            distancia += mapa[cidade + 2]
            break
        elif mapa[cidade] == atual and mapa[cidade + 1] != destino:
        #    print(mapa.count(mapa[cidade + 1]))
            if mapa.count(mapa[cidade + 1]) >= 2:
                atual = mapa[cidade + 1]
                distancia += mapa[cidade + 2]

print(distancia)

"""
<4 2 4>
1 2 10
2 3 11
3 4 12



16 15 7

3 5 8 xxx --

12 3 3 xx --

5 1 5 xx ---

2 1 5 xx --

4 1 10 xx --

6 1 3 xx --

7 1 7 xx --

12 8 3 xx --

12 9 3 xx --

12 10 3 xx --

12 11 3 xx --

3 13 6 xx --

13 14 6 xx --

15 13 7 xx

15 16 10 xx

"""




"""

mapa = [
(3, 5, 8), (12, 3, 3), (5, 1, 5),

(2, 1, 5,), (4, 1 ,10), (6, 1, 3),

(7, 1, 7), (12, 8, 3), (12, 9, 3),

(12, 10, 3), (12, 11, 3), (3, 13, 6),

(13, 14, 6), (15, 13, 7), (15, 16, 10)
]

mapa_final = [
(15, 13, 7),
(3, 13, 6),
(3, 5, 8),
(5, 1, 5),
(7, 1, 7)]

15 -7-> 13 -6-> 3 -8-> 5 -5-> 1 -7-> 7 = 33
"""