vel = int(input('Digite a velocidade: '))
vel2 = vel - 80
if vel >80:
    print ('Você foi multado em {} reais'.format(vel2*7))
else:
    print ('Parabéns você não foi multado!')