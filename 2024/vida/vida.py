def printMatrix(matrix):
    for line in matrix:
        for column in line:
            print(column, end="")
        print("")


def changeState(matrix, state, line, column):
    if state == 0:
        matrix[line][column] = '0'
    else:
        matrix[line][column] = '1'


initial_matrix = []
change_matrix = []

dimensions, steps = [int(i) for i in input().split()]
lim = dimensions - 1


for i in range(0, dimensions):
    initial_matrix.append([])
    change_matrix.append([])
    row_value = str(input())

    for j in range(0, dimensions):
        initial_matrix[i].append(row_value[j])
        change_matrix[i].append('0')


for i in range(0, steps):

    if i % 2 == 0:
        current_matriz = initial_matrix
    else:
        current_matriz = change_matrix


    for j in range(0, dimensions):

        for k in range(0, dimensions):

            state = 0

            # Privando apenas para elementos que têm os 8 vizinhos
            if 0 < j < lim and 0 < k < lim:
                vizinhos = [
                
                    # Linha Acima
                    current_matriz[j - 1][k - 1], current_matriz[j - 1][k],
                    current_matriz[j - 1][k + 1], 
                    
                    # Mesma Linha
                    current_matriz[j][k - 1],
                    current_matriz[j][k + 1], 
                    
                    # Linha Abaixo
                    current_matriz[j + 1][k - 1],
                    current_matriz[j + 1][k], current_matriz[j + 1][k + 1]

                ]

            # Privando apenas para as extremidades da current_matriz (esquinas/quinas/pontas)
            elif (j == 0 or j == lim) and (k == 0 or k == lim):
                
                # Primeira Linha
                if j == 0:
                    # Primeira Coluna
                    if k == 0:
                        vizinhos = [
                            current_matriz[j + 1][k],
                            current_matriz[j + 1][k + 1],
                            current_matriz[j][k + 1]
                        ]

                    # Última Coluna
                    elif k == lim:
                        vizinhos = [
                            current_matriz[j][k - 1],
                            current_matriz[j + 1][k - 1],
                            current_matriz[j + 1][k]
                        ]

                # Última Linha
                elif j == lim:
                    # Primeira Coluna
                    if k == 0:
                        vizinhos = [
                            current_matriz[j][k + 1],
                            current_matriz[j - 1][k],
                            current_matriz[j - 1][k + 1]
                        ]

                    # Última Coluna            
                    elif k == lim:
                        vizinhos = [
                            current_matriz[j][k - 1],
                            current_matriz[j - 1][k],
                            current_matriz[j - 1][k - 1]
                        ]
                        
            # Privando apenas para as linhas e colunas iniciais e finais, mas sem ser extremidade (Resto)
            else:
                # Linhas iniciais e finais que não esquinas | Resto Linear
                if (j == 0 or j == lim) and 0 < k < lim:
                    if j == 0:
                        vizinhos = [
                            current_matriz[j][k - 1],
                            current_matriz[j][k + 1],
                            current_matriz[j + 1][k - 1],
                            current_matriz[j + 1][k],
                            current_matriz[j + 1][k + 1]
                        ]
                    elif j == lim:
                        vizinhos = [
                            current_matriz[j][k - 1],
                            current_matriz[j][k + 1],
                            current_matriz[j - 1][k - 1],
                            current_matriz[j - 1][k],
                            current_matriz[j - 1][k + 1]
                        ]
                
                # Colunas iniciais e finais que não esquinas | Resto Colunar
                else:
                    if k == 0:
                        vizinhos = [
                            current_matriz[j][k + 1],
                            current_matriz[j - 1][k],
                            current_matriz[j - 1][k + 1],
                            current_matriz[j + 1][k],
                            current_matriz[j + 1][k + 1]
                        ]
                    elif k == lim:
                        vizinhos = [
                            current_matriz[j][k - 1],
                            current_matriz[j - 1][k],
                            current_matriz[j - 1][k - 1],
                            current_matriz[j + 1][k],
                            current_matriz[j + 1][k - 1]
                        ]

            vizinhas_vivas = vizinhos.count('1')
            if current_matriz[j][k] == '0' and vizinhas_vivas == 3: 
                state = 1
            elif current_matriz[j][k] == '1' and (vizinhas_vivas == 2 or vizinhas_vivas == 3):
                state = 1
            else:
                state = 0

            if i % 2 == 0:
                changeState(change_matrix, state, j, k)
            else:
                changeState(initial_matrix, state, j, k)

if steps % 2 == 0:
    printMatrix(initial_matrix)
else:
    printMatrix(change_matrix)
  
