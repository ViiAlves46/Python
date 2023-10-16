from math import hypot

CO = float(input('Digite o cateto oposto: '))
CA = float(input('Digite o cateto adjacente: '))
#H = (CA**2+CO**2) ** (1/3) FORMULA HIPOTENUSA
H = hypot (CO, CA)

print ('O comprimento da hipotenusa é {:.2f}.'.format(H))