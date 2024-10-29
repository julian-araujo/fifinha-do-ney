neymar = 0
ney = 0
neylindo = 0
neyfa = 0
neycopa = 0
branco = 0
soma = soma2 = 0

print('1)neymar\n'
          '2)neymar\n'
          '3)neymito\n'
          '4)neycopa\n'
          '5)nulo\n'
          '6)Branco\n')
num = 1
while num > 0:
    num = int(input('digite um numero para votar'))
    if num > 0:
         if num==1:
            neymar+=1
         if num==2:
            ney+=1
         if num ==3:
            neyfa+=1
         if num==4:
            neyfa+=1
         if num==5:
            neycopa+=1
         if num==6:
            branco+=1
         if num>6:
            print('errado')
soma=branco/(neymar+ney+neylindo+neycopa)*100
soma2 = neycopa / (neymar + ney + neylindo + neycopa) * 100
print('neymar  recebeu',neymar)
print('neymar recebeu',ney)
print('neymar recebeu',neylindo)
print('nymar copa recebeu',neyfa)
print('Votos nulo',neycopa)
print('Votos branco',branco)
print(f'{soma:.1f}%')
print(f'{soma2:.1f}%')