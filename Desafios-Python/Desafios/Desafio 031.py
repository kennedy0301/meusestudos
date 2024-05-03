'''t1 = float(input('Digite os quilometros a serem percorridos:\nKM...'))

if t1 >= 200:
    print('Você ira pagar R$ {:.2f}'.format(t1 * 0.45))
else:
    print('Você ira pagar R$ {:.2f}'.format(t1 * 0.50))'''



t1 = float(input('Digite os quilometros a serem percorridos:\nKM...'))
preco = t1 * 0.50 if t1 <=200 else t1 * 0.45
print('E p presso a pagar é {:.2f}'.format(preco))


#Simplificaado



