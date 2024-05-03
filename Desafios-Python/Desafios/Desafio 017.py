'''c1 = float(input('Comprimmento do cateto oposto:\n...'))
c2 = float(input('Comprimento do cateto adijacente:\n...'))
h = ((c1 ** 2) + (c2 ** 2)) ** (1/2)
print('A hipotenusa é{:.2f}'.format(h))'''

from math import hypot
c1 = float(input('Comprimmento do cateto oposto:\n...'))
c2 = float(input('Comprimento do cateto adijacente:\n...'))
h = hypot(c1, c2)
print('A hipotenusa é{:.2f}'.format(h))





