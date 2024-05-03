v1 = float(input('Valor 1:\n... '))
v2 = float(input('Valor 2:\n... '))
v3 = float(input('Valor 3:\n... '))
if v1 + v2 > v3 and v2 + v3 > v1 and v1 + v3 > v2:
    print('certo')
else:
    print('errado')
