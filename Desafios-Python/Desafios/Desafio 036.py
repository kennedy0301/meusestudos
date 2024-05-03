t1 = int(input('Digite o valor da casa.\nR$:...'))
t2 = int(input('Seu salário.\nR$...'))
t3 = int(input('Quantos anos você pretende pagar?\nR$....'))
c1 = (t1 / 12) / t3
if c1 <= (t2/100) * 30:
    print('você pode comprar a casa com uma mensalidade de {:.2f}'.format(c1))
else:
    print('Não poderá comprar a casa...')
