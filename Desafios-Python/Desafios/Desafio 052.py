t1 = int(input('Digite um número para saber se é primo ou não.\n...'))
tot = 0
for c in range(1, t1 + 1):
    if t1 % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c),end=' ')
print('\n O número {} pode ser dividido {} vezes, então'.format(t1, tot),end=' ')
if tot == 2:
    print('ele é primo.')
else:
    print('ele NÃo é primo.')

