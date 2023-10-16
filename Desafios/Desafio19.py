import math

var = float(input('Digite o valor do angulo: '))
s = math.sin(math.radians(var))
c = math.cos(math.radians(var))
t = math.tan(math.radians(var))

print ('O angulo {:.0f}º de seno é {:.3f}, do cosseno {:.3f} e da tangente {:.3f}.'.format(var,s,c,t))