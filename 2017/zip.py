# treinamento OBI - zip.py

cartas = []
pont_lia = 0
pont_carol = 0


for i in range(0, 4):
    val_carta = int(input())
    cartas.append(val_carta)


if cartas[0] == cartas[1]:
    pont_lia = (cartas[0] + cartas[1]) * 2

elif cartas[0] == cartas[1] - 1 or cartas[1] == cartas[0] - 1:
    pont_lia = (cartas[0] + cartas[1]) * 3

else:
    pont_lia = cartas[0] + cartas[1]


if cartas[2] == cartas[3]:
    pont_carol = (cartas[2] + cartas[3]) * 2

elif cartas[2] == cartas[3] - 1 or cartas[3] == cartas[2] - 1:
    pont_carol = (cartas[2] + cartas[3]) * 3

else:
    pont_carol = cartas[2] + cartas[3]


if pont_lia > pont_carol:
    print("Lia")

elif pont_carol > pont_lia:
    print("Carolina")

else:
    print("empate")
