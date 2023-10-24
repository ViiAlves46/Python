dia = int(input("digite o dia de se nascimento: "))
mes = int(input("digite o mes do seu nascimento: "))

if (dia >= 21 and mes == 3) or (dia <= 20 and  mes == 4):
   print ('aries')
if (dia >= 21 and mes == 4) or (dia <= 20 and mes == 5):
   print ('touro')
if (dia >= 21 and mes == 5) or (dia <= 20 and mes == 6):
   print ('gemeos')
if (dia >= 21 and mes == 6) or (dia <= 21 and mes == 7):
   print ('cancer')
if (dia >= 22 and mes == 7) or (dia <= 22 and mes == 8):
   print ('leao')
if (dia >= 22 and mes == 8) or (dia <= 22 and mes == 9):
   print ('virgem')
if (dia >= 22 and mes == 9) or (dia <= 22 and mes == 10):
   print ('libra')
if (dia >= 23 and mes == 10) or (dia <= 21 and mes == 11):
   print ('escorpiao')
if (dia >= 22 and mes == 11) or (dia <= 21 and mes == 12):
   print ('sagitario')
if (dia >= 22 and mes == 12) or (dia <= 20 and mes == 1):
  print ('capricornio')
if (dia >= 21 and mes == 1) or (dia <= 18 and mes == 2):
  print ('aquario')
if (dia >= 19 and mes == 2) or (dia <= 19 and mes == 3):
  print ('peixes')
else:
  print ("mes ou dia invalido")
