from datetime import date
idade = date.today().year
maior = 0
menor = 0

for c in range(1, 8):
    t1 = int(input('Digite a data de nascimento de cada um :{}°...  '.format(c)))
    atual = idade - t1
    if atual >= 18:
        maior += 1
    else:
        menor += 1
print('Maior {} menor {}'.format(maior, menor))