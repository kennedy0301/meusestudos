t1 = int(input('Didite um numero\n...'))
t2 = int(input('Agora o segundo numero\n...'))
t3 = int(input('Prometo que é o ultima. rsrs\n...'))
menor = t1
if t2 < t1 and t2 < t3:
    menor = t2
if t3 < t1 and t3 < t1:
    menor = t3

maior = t1
if t2 > t1 and t2 > t3:
    maior = t2
if t3 > t1 and t3 > t2:
    maior =t3

print('O menor é: ', menor)
print('O maior é: ', maior)








