neymarcaro=0
baratin=999
valordapizza=0
pedido=0
media=str("média")
pequena=str("pequena")
grande=str("grande")
calabresa=str("calabresa")
mussarela=str("mussarela")
tomate=str("tomate")
cebola=str("cebola")
bacon=str("bacon")
sim=str("sim")
nao=str("nao")
while True:
    print("qual pizza voce vai querer  uma pizza pequena 20, média 30 ou grande 40")
    pizza=str(input("coloque: "))
    if pizza == pequena:
        valordapizza=valordapizza+20
    if pizza == media:
        valordapizza=valordapizza+30
    if pizza == grande:
        valordapizza+valordapizza+40
    neymar=str(input(" quer colocar algum ingrediente a mais sim/nao: "))
    if neymar == sim:
        print("Cada um dos ingredientes a mais vale 5$, como calabresa, mussarela, tomate, cebola e bacon")
        while True:
            mais=str(input("coloque o outro ingrediente que você quer: "))
            if mais == calabresa or mussarela or tomate or cebola or bacon:
                valordapizza=valordapizza+5
            desejacontinuar=str(input("quer continuar? sim/nao: "))
            if desejacontinuar == nao:
                break
    beber=str(input("quer beber algo? sim/nao: "))
    if beber == sim:
        valordapizza=valordapizza+8
    print("Seu pedido deu: ",valordapizza)
    pedidonovo=str(input("queria fazer um novo pedido sim/nao: "))
    if valordapizza > neymarcaro:
            caro=valordapizza
    if valordapizza < baratin:
            barato=valordapizza
    if pedidonovo == sim:
        valordapizza=0
        pedido+=1
    else:
        print("Pedido caro: ", neymarcaro)
        print("Pedido barato: ",baratin)
        break
