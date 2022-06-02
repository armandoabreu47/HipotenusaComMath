import math
oposto = float(input('Digite o cateto oposto:'))
adj = float(input('Digite o cateto adjacente:'))
hi = math.hypot(oposto,adj)

print('A hipotenusa vai medir {:.2f}'.format(hi))

