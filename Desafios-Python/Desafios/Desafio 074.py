from random import  randint
n = (randint(1,10), randint(1,10), randint(1,10),
     randint(1,10), randint(1,10))
print('Valores:')
for num in n:
    print(f'{num}', end=' ')
print(f'\nO maior foi {max(n)}')
print(f'O menor foi {min(n)}')



