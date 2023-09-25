# treinamento OBI - bits.py

from random import randint

bits = []
passar = ""
compare = []
temp_list = []
restricao_final = ""
qtd_bits, qtd_restricao = str(input()).split(" ")


for r in range(0, int(qtd_restricao)):
    if r == int(qtd_restricao) - 1:
        restricao_final = restricao_final + "1"
    else:
        restricao_final = restricao_final + "1, "



while True:
    for i in range(0, int(qtd_bits)):
        temp = randint(0, 1)
        temp_list.append(temp)
    if restricao_final not in temp_list:
        for bit in bits:
            passar = temp_list[:]
            if bit in temp_list:
                print(temp_list)
                compare.append(passar[:])
            elif temp_list not in bits:
                print(temp_list)
                bits.append(passar[:])
        temp_list.clear()
    else:
        continue
    if len(bits) > 1 and bits == compare:
        break

