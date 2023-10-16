import random
sort = random.randint(0 , 5)
resp = sort
chute=0

while resp != chute:
    chute = int(input('Digite um numero de 0 a 5: '))
    if chute > resp:
        print('O número que você é maior!')
    elif chute < resp:
        print('O número que você digitou é menor!')
    else:
        print('Você acertou o número era: ', resp)
