t1 = int(input('Digite o numero que você queira saber a sabuada:\n...'))
print('-=-=-' * 7)
for c in range(0, 21):
    print('{:2} x {:2} = {}'.format(t1, c, (t1 * c)))
print('-=-=-'* 7)
