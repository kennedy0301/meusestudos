t1 = int(input('Digite o primeiro termo:\n'))
t2 = int(input('Agora a razão:\n'))
decimo = t1 + (10 - 1) * t2
for c in range(t1, decimo, t2):
    print(c, end=' -> ')
print('Acabou')
