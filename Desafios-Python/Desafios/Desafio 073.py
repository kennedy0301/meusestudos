times = 'Corinthinans', 'Palmeiras', 'São Paulo',\
        'Vasco', 'Avai', 'Bota fogo', 'Chapecoense'
print('-=' * 19)
print(f'Times:{times}')
print('-=' * 19)
print('\nos cinco premeiros sao :',times[0:5])
print('-=' * 14)
print(f'Os quatro ultimos são : {times[-4:]}')
print('-=' * 14)
print(f'time em ordem algabétiva{sorted(times)}')
print('-=' * 14)
print(f'O Chapecoense esta na psoção {times.index("Chapecoense" )+1}ª')