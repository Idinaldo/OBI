# treinamento OBI - plano.py

qtd_vagas = int(input())
qtd_clientes = int(input())
vagas = [0]
delete = []
qtd_ocupadas = 0

for pos in range(1, qtd_vagas + 1):
    vagas.append(pos)

for i in range(0, qtd_clientes):
     v = int(input())
     if v in vagas:
          if vagas.index(v) == vagas[-1]:
              delete.append(v)
              qtd_ocupadas += 1
          else:
              delete.append(v)
              qtd_ocupadas += 1
     else:
          continue
    
     for vaga in delete:
         vagas.remove(vaga)
     delete.clear()
     

print(qtd_ocupadas)
