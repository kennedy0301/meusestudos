from datetime import date
atual = date.today().year
t2 = int(input('Digite seu ano de nascimento:\n...'))
t1 = atual - t2
print('Categoria:')
if t1 <= 9:
    print('Mirim')
elif t1 <= 14:
    print('Infantil')
elif t1 <=19:
    print('Junior')
elif t1 <= 25:
    print('Sênior')
else:
    print('Master')
