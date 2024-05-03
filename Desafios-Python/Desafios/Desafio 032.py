t1 = int(input('Digite o ano a ser analisado:\n...'))
if t1 % 4 == 0 and t1 % 100 != 0 or t1 % 400 == 0:
    print('O ano é Bissexto')
else:
    print('Esse ano não é bissexto')
