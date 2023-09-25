# treinamento OBI - gomoku.py

pecas = []
vencedor = 0


for valores in range(0, 15):
    temp_val = str(input())    
    if "1 1 1 1 1" in temp_val:
        vencedor = 1    
    elif "2 2 2 2 2" in temp_val:
        vencedor = 2    
    else:
        pecas.append(temp_val)


if vencedor == 0:
    for linha in range(0, 15):
        for position in range(0, 15):
            if linha <= 10:
                # verticalmente (1)
                if pecas[linha][position] == "1" and pecas[linha + 1][position] == "1" and pecas[linha + 2][position] == "1" and pecas[linha + 3][position] == "1" and pecas[linha + 4][position] == "1":
                    vencedor = 1
                    break                
                # verticalmente (2)
                elif pecas[linha][position] == "2" and pecas[linha + 1][position] == "2" and pecas[linha + 2][position] == "2" and pecas[linha + 3][position] == "2" and pecas[linha + 4][position] == "2":
                    vencedor = 2
                    break
            if position <= 10:
                # diagonalmente para direita (2)
                if pecas[linha][position] == "2" and pecas[linha + 1][position + 1] == "2" and pecas[linha + 2][position + 2] == "2" and pecas[linha + 3][position + 3] == "2" and pecas[linha + 4][position + 4] == "2":
                    vencedor = 2
                    break
                # diagonalmente para direita (1)
                elif pecas[linha][position] == "1" and pecas[linha + 1][position + 1] == "1" and pecas[linha + 2][position + 2] == "1" and pecas[linha + 3][position + 3] == "1" and pecas[linha + 4][position + 4] == "1":
                    vencedor = 1
                    break
            if position >= 4:                
                # diagonalmente para esquerda (2)
                if pecas[linha][position] == "2" and pecas[linha + 1][position - 1] == "2" and pecas[linha + 2][position - 2] == "2" and pecas[linha + 3][position - 3] == "2" and pecas[linha + 4][position - 4] == "2":
                    vencedor = 2
                    break
                # diagonalmente para esquerda (1)
                elif pecas[linha][position] == "1" and pecas[linha + 1][position - 1] == "1" and pecas[linha + 2][position - 2] == "1" and pecas[linha + 3][position - 3] == "1" and pecas[linha + 4][position - 4] == "1":
                    vencedor = 1
                    break


print(vencedor)
