num = int(input('Digite um numero para calcular o fatorial: '))
fatorial = 1
for contador in range (1,num+1):
    fatorial *= contador
print (f'Fatorial de {num} é {fatorial} !')
