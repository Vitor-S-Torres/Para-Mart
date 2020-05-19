def area_interativa(a1,a2,a3,b1,b2,b3,c1,c2,c3):
    area=[[a1,a2,a3],[b1,b2,b3],[c1,c2,c3]]
    return area

def girar(area,direcao):        
    areacp=area_interativa(0,0,0,0,0,0,0,0,0)
    if direcao=="direita":
        areacp[0][0]=area[2][0]
        areacp[1][0]=area[2][1]
        areacp[2][0]=area[2][2]
        areacp[0][2]=area[0][0]
        areacp[1][2]=area[0][1]
        areacp[2][2]=area[0][2]
        areacp[0][1]=area[1][0]
        areacp[2][1]=area[1][2]
    elif direcao=="esquerda":
        areacp[0][0]=area[0][2]
        areacp[1][0]=area[0][1]
        areacp[2][0]=area[0][0]
        areacp[0][2]=area[2][2]
        areacp[1][2]=area[2][1]
        areacp[2][2]=area[2][0]
        areacp[0][1]=area[1][2]
        areacp[2][1]=area[1][0]
    areacp[1][1]=area[1][1]    
    area=areacp
    return area

def interagir(a1,a2,a3,b1,b2,b3,c1,c2,c3):
    area=area_interativa(a1,a2,a3,b1,b2,b3,c1,c2,c3)
    print(area)
    #area=girar(area,"direita")
    #gira 360°
    area=girar(area,"esquerda")
    print(area)
    area=girar(area,"esquerda")
    print(area)
    area=girar(area,"esquerda")
    print(area)
    area=girar(area,"esquerda")
    print(area)
    escolha=int(input("qual área quer interagir?"))
    if escolha==1:
        print(area[0][0])
    elif escolha==2:
        print(area[0][1])
    elif escolha==3:
        print(area[0][2])
    elif escolha==4:
        print(area[1][0])
    elif escolha==5:
        print(area[1][1])
    elif escolha==6:
        print(area[1][2])
    elif escolha==7:
        print(area[2][0])
    elif escolha==8:
        print(area[2][1])
    elif escolha==9:
        print(area[2][2])

interagir("1","2","3","4","5","6","7","8","9")
