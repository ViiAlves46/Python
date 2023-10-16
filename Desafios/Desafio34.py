km = int(input('Quantos kms: '))
if km <= 200:
    print('Sua viagem custará: {}'.format(km*0.50))
else:
    print('Sua viagem custará: {}'.format(km*0.45))