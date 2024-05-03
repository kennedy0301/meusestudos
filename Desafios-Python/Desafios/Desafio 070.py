soma = maior = menor = 0
print('-=-' * 7, 'Mercadinho do Sr.Jão', '-=-' * 7)
while True:
    nome = str(input('Qual o Nome do Produto?'))
    preco = float(input('E o preço: \nR$:  '))
    menor = preco
    if preco <= menor:
        menor = nome
    if preco >= 1000:
        maior =+ 1

    soma += preco
    t1 = str(input('Deseja continua?\n [S/N]: ').upper())
    if t1 == 'N':
        print(('-=-'*7,'FIM DE PROGRAMA',('-=-'*7)))
        break
print(f'A compra teve um valor de R$ {soma}\n{maior} produto(s) com valor maior que R$1000,00 \nO produto mais barato foi {menor} ')
