#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.
n=0
i=str(input("informe se voce é neymar ou neymara: "))
h=float(input("informe a altura do neymara ou da neymar: "))
if i=="neymar":
    n=(72.7*h)-58
    print(n)
if i=="neymara":
    n=(62.1*h)-44.7
    print (n)