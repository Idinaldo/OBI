# treinametno OBI - casamento.py
mostrar = []
final1 = []
final2 = []
n1 = str(input())
n2 = str(input())
m1 = 0
m2 = 0

while len(n1) != len(n2):
    if len(n1) > len(n2):
        n2 = "0" + n2
    elif len(n2) > len(n1):
        n1 = "0" + n1


for i in range(0, len(n1)):
    if int(n1[i]) > int(n2[i]):
        final1.append(n1[i])
    elif int(n2[i]) > int(n1[i]):
        final2.append(n2[i])
    elif int(n1[i]) == int(n2[i]):
        final1.append(n1[i])
        final2.append(n2[i])


if len(final1) > 0:
    for numb in final1:
        if m1 == 0:
            m1 = numb
        else:
            m1 = f"{m1}" + numb
else:
    m1 = -1


if len(final2) > 0:
    for number in final2:
        if m2 == 0:
            m2 = number
        else:
            m2 = f"{m2}" + number
else:
    m2 = -1



mostrar.append(int(m1))
mostrar.append(int(m2))
mostrar.sort()
for number in mostrar:
    print(number, end=" ")



"""

5678
1234

"""