t1 = str(input('Digite sua frase para saber se é ou não um palindromo:\n...')).strip().upper()
t2 = t1.split()
t3 = ''.join(t2)
t4 = t3[::-1]
'''for c in range(len(t3) - 1, -1,-1):
    t4 +=  t3[c]'''
print('{} ao Contrario é {} então '.format(t3, t4),end='')
if t3 == t4:
    print('é um palindromo.')
else:
    print('não é um palindromo.')

