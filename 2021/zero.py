# Qtd de números falados
numbers_count = int(input())
# array pra guardar esses números
numbers = []

# estrutura de repetição para pegar e tratar valores passados ao array
for i in range(0, numbers_count):
    current_number = int(input())

    # verificando se o valor é diferente de 0
    if current_number != 0:
        # Adicionando valores ao array number  
        numbers.append(current_number)
    
    else:
      # excluindo do array o último valor dito
        numbers.pop()

# imprimindo a soma dos valores no array
print(sum(numbers))
