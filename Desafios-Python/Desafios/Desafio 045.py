import random
from time import sleep
print(20 * '=-=-')
print('''Escolhas:
[0]pedra
[1]papel
[2]tesoura''')
objetos = ('pedra','papel','tesoura')
lista = random.randint(0,2)
player = int(input('Digite a sua:\n...'))
print(20 * '=-=-')
sleep(0.5)
print('Jo')
sleep(0.5)
print('Ken')
sleep(0.5)
print('Po!')
print(20 * '=-=-')
print('O computador escolheu {} e você'.format(objetos[lista]), end=' ')
print(objetos[player])
print(20 * '=-=-')
if lista == 0:
    if player == 1:
        print('You win')
    elif player == 2:
        print('you loose')
    elif player == 0:
        print('Não tem vencedor nem perdedor')
    else:
        print('Essa opção não existe')
elif lista == 1:
    if player == 2:
        print('You win')
    elif player == 0:
        print('You loose')
    elif player == 1:
        print('Não tem vencedor nem perdedor')
    else:
        print('Essa opção não existe')
elif lista == 2:
    if player == 0:
        print('You win')
    elif player == 1:
        print('You loose')
    elif player == 2:
        print('Não tem vencedor nem perdedor')
    else:
        print('Essa opção não existe')
print(20 * '=-=-')