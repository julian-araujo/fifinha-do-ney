obito=0
neymar=0
positivo=0
negativo=0
i=1
while(i>0):
     n1=int (input("digite um numero: "))
     if(n1>0) and (n1<25):
        positivo=positivo+1
     if(n1>26)and(n1<50):
        negativo=negativo+1
     if(n1>51)and(n1<75):
        neymar=neymar+1
     if(n1>76)and(n1<100):
        obito=obito+1
     if(n1<0):
       i=-1
print("esse nuemro nao entre 0 e 25",positivo)
print("este numero nao entre 26 a 50",negativo)
print("este numero nao entre 51 a 75",neymar)
print("este numero nao entre 76 a 100",obito)