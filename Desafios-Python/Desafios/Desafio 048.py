soma = 0
contador = 0
for t1 in range(1, 501, 2):
    if t1 % 3 == 0:
       contador +=  1
       soma += t1

print('A soma de todos  {} numeros é {}'.format(contador, soma))

