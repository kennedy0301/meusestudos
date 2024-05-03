t1 = float(input('Digite sua primeira nota:\n...'))
t2 = float(input('Digite o segundo numero:\n...'))
media = (t1+t2)/2
print('Sua media é {:.1f}.'.format(media))
if media > 5 and media < 6.9:
    print('Você está de recuperação.')
elif media >= 7:
    print('você passou.')
else:
    print('Você foi reprovado.')


