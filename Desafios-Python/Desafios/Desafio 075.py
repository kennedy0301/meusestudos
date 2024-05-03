n = (int(input('Digite um numero:')),
     int(input('Digite ou Numero:')),
     int(input('Agora outro:')),
     int(input('O Ultimo:')))
print(f"Os numeros digitados foram{n}")
print(f'O número 9 aparece {n.count(9)} vezes')
print('O numero 3 esta na ', end='')

if 3 in n:
     print(f'{n.index(3) + 1} posição')
else:
     print(f'Não tem Posição, pois não foi digitado')


