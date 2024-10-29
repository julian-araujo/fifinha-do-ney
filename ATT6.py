#Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. 
#Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.
n=999
n1=0
n2=0
n3=0
for i in range(0,5):
  neymar=int(input("mostre a altura: "))
  neymar2=int(input("insira um numero: "))
  if(neymar<n):
    n=neymar
    n1=neymar2
  if(neymar>n2):
    n2=neymar
    n3=neymar2
print("altura do maior e igual: ",n2)
print("numero do maior e igual: ",n3)
print("altura do menor e igual: ",n)
print("numero do menor e igual: ",n1)