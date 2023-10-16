s1 = str(input('Digite uma palavra: '))
s2 = str(input('Digite uma palavra: '))

if (sorted(s1) == sorted(s2)):
        print( "isso é um anagrama")
else:
        print("isso não é um anagrama")