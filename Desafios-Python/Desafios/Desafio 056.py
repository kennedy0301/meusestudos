somaidade = 0
mediaidade = 0
maioridadehomem = 0
homemmaisvelho = ''
totmulher20 = 0


for p in range(1, 5):
    print('       PESSOA {}°  '.format(p))
    nome = str(input('Nome:  ')).strip()
    idade = int(input('Idade  '))
    sexo = str(input('Sexo [M/F]')).strip()
    somaidade += idade
    if p == 1:
        maioridadehomem = idade
        homemmaisvelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        homemmaisvelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1


mediaidade += somaidade / 4
print('A média da idade é {}'.format(mediaidade))
print('O homem mais velho é {}'.format(homemmaisvelho))
print('Tem {} mulheres com menos 20 anos'.format(totmulher20))
