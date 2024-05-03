'''t1 = str(input('Digite um numero com até quadro digitos:\n...')).strip()
print('A unidade é {}, a dezena {}, a centena {} e milhar {}.'.format(t1[3], t1[2], t1[1], t1[0]))'''

n1 = int(input('Informe um numero:\n...'))
u = n1 // 1 % 10
d = n1 // 10 % 10
c = n1 // 100 % 10
m = n1 // 1000 % 10
print('A unidade é {}, a dezena {}, a centena {} e milhar {}.'.format(u, d, c, m))





#genial


