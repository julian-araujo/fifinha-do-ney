sc=0
bh=0
rj=0
i=2
while True:
    n1=str(input("digite uma cidade ney"))
    if n1=="rj":
        rj=rj+1
    if n1=="bh":
        bh=bh+1
    if n1=="sc":
        sc=sc+1
    if n1=="fim":
       break
print("sao do rio de jeneiro",rj)
print("sao de belo horizonte",bh)
print("sao de santa catarina",sc)
