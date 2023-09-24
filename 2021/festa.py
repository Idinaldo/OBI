# treinamento OBI - festa.py

suditos = [0]
delete = 0
qtd_suditos = int(input())
qtd_turnos = int(input())


for pos in range(1, qtd_suditos + 1):
    suditos.append(pos)

print(suditos)
for turno in range(0, qtd_turnos):
    t = int(input())
    print(suditos)
    for mult in range(1, len(suditos) + 1):
        for sudito in range(1, len(suditos)):        
            if suditos.index(sudito) == t * mult:
                delete = suditos.index(sudito)
                del suditos[delete]

    """ for sud in delete:
        suditos.remove(sud)"""


if len(suditos) >= 10000:
    while len(suditos) >= 10000:
        suditos.pop()

for s in suditos:
    print(s, end="\n")



"""

suditos0 = [1, 2, 3, 4, 5, 6]
suditos1 = [1, 3, 5]
suditos2 = [1, 5]
suditos3 = [1]
6
3
2
2
2

1

"""
