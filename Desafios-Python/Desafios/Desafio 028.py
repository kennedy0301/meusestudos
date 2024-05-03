import random
from time import sleep
'''t1 = int(input('Digite um numero de 1 a 5:\n...'))
a = 1
b = 2
c = 3
d = 4
e = 5
t2 = (a,b,c,d,e)
t3 = random.choice(t2)
if t1 == t3:
    print('Você pensa como um computador, Parabens!')
else:
    print('Você esta longe de ser inteligente como eu!')
print('O numero que pensei foi {}'.format(t3))''' # meu código primario, sem usar randint


print('='*70)
t1 = int(input('Estou pensando em um número de 0 a 5, adivinhe qual é:\n...'))
t2 = random.randint(0,1)
print('='*70)
print('Aguarde....')

if t1 == t2:
    print('Você pensa como um computador, Parabens!')
else:
    print('Você esta longe de ser inteligente como eu!')
print('O numero que eu pensei foi {} e não {}'.format(t2,t1))
print('='*70)


