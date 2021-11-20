from graphics import *
import random
import time

def Abertura():
    win=GraphWin("CARA A CARA",500,400,autoflush=False)
    win.setBackground("white")

    c = Circle(Point(-88,-75),30)
    c.setFill("white")
    c.setOutline("white")
    c.draw(win)
    c2 = Circle(Point(530,-75),30)
    c2.setFill("white")
    c2.setOutline("white")
    c2.draw(win)
    cx=3
    cy=0
    c2x=-3
    c2y=0
    j04pp=Image(Point(-100,75),"04pp.gif")
    j04pp.draw(win)
    j05pp=Image(Point(600,75),"05pp.gif")
    j05pp.draw(win)
    j04ppx=3
    j04ppy=0
    j05ppx=-3
    j05ppy=0
    j06pp=Image(Point(-382,75),"06pp.gif")
    j06pp.draw(win)
    j07pp=Image(Point(882,75),"07pp.gif")
    j07pp.draw(win)
    j06ppx=5
    j06ppy=0
    j07ppx=-5
    j07ppy=0

    while(c.getCenter().getX()<=c2.getCenter().getX()):
        c.move(cx,cy)
        c2.move(c2x,c2y)
        j04pp.move(j04ppx,j04ppy)
        j05pp.move(j05ppx,j05ppy)
        j06pp.move(j06ppx,j06ppy)
        j07pp.move(j07ppx,j07ppy)
        update(60)
    c.undraw()
    c2.undraw()
    c = Circle(Point(-88,-75),30)
    c.setFill("white")
    c.setOutline("white")
    c.draw(win)
    cx=2
    cy=0
    while(c.getCenter().getX()<=320):
        c.move(cx,cy)
        update(60)
        if c.getCenter().getX() >= 50:
            j04pp.undraw()
        if c.getCenter().getX() >= 100:
            j06pp.undraw()
        if c.getCenter().getX() >= 150:
            j07pp.undraw()
        if c.getCenter().getX() >= 240:
            j05p=Image(Point(290,81),"05p.gif")
            j05p.draw(win)
            j05pp.undraw()
        if c.getCenter().getX() >= 260:
            j05m=Image(Point(250,163),"05m.gif")
            j05m.draw(win)
            j05p.undraw()
        if c.getCenter().getX() >= 280:
            j05=Image(Point(250,250),"05.gif")
            j05.draw(win)
            j05m.undraw()
    c.undraw()        
    c = Circle(Point(250,200),500)
    c.setFill("white")
    c.setOutline("white")
    c.draw(win)
    j05.undraw()
    caixam1 = Rectangle(Point(100,190),Point(400,210))
    caixam1.setFill("pink")
    caixam1.setOutline("black")
    caixam1.setWidth(4)
    caixam1.draw(win)
    caixam2 = Rectangle(Point(100,290),Point(400,310))
    caixam2.setFill("pink")
    caixam2.setOutline("black")
    caixam2.setWidth(4)
    caixam2.draw(win)
    t1 = Text(Point(250,50),"JOGO CARA A CARA")
    t1.setSize(20)
    t1.draw(win)
    t1.setStyle("bold")
    t1.setTextColor("orange")
    linha = Line(Point(50,75),Point(450,75))
    linha.draw(win)
    t2 = Text(Point(250,100),"ESCOLHA O MODO QUE DESEJA JOGAR")
    t2.setSize(14)
    t2.setTextColor("red")
    t2.draw(win)
    tmodo1 = Text(Point(250,200),"ADVINHE DO COMPUTADOR")
    tmodo1.setSize(12)
    tmodo1.setTextColor("blue")
    tmodo1.draw(win)
    tmodo = Text(Point(250,250),"OU")
    tmodo.setSize(12)
    tmodo.setTextColor("black")
    tmodo.draw(win)
    tmodo2 = Text(Point(250,300),"DESAFIE UM AMIGO")
    tmodo2.setSize(12)
    tmodo2.setTextColor("blue")
    tmodo2.draw(win)
    j = 1
    while j != 0:
        p = win.getMouse()
        x = p.x
        y = p.y
        if x>100 and x<400 and y>190 and y<210:
            j = 0
            win.close()
            Jogo2()
        if x>100 and x<400 and y>290 and y<310:
            j = 0
            win.close()
            Jogo1()

def Jogo2():
    win=GraphWin("CARA A CARA",1024,560,autoflush=False)
        
    #INSERIR MINIATURAS NO LAYOUT
    j01pp=Image(Point(50,80),"01pp.gif")
    j01pp.draw(win)
    j02pp=Image(Point(132,80),"02pp.gif")
    j02pp.draw(win)
    j03pp=Image(Point(214,80),"03pp.gif")
    j03pp.draw(win)
    j04pp=Image(Point(296,80),"04pp.gif")
    j04pp.draw(win)
    j05pp=Image(Point(378,80),"05pp.gif")
    j05pp.draw(win)
    j06pp=Image(Point(460,80),"06pp.gif")
    j06pp.draw(win)
    j07pp=Image(Point(542,80),"07pp.gif")
    j07pp.draw(win)
    j08pp=Image(Point(624,80),"08pp.gif")
    j08pp.draw(win)
    j09pp=Image(Point(706,80),"09pp.gif")
    j09pp.draw(win)
    j10pp=Image(Point(788,80),"10pp.gif")
    j10pp.draw(win)
    j11pp=Image(Point(50,212),"11pp.gif")
    j11pp.draw(win)
    j12pp=Image(Point(132,212),"12pp.gif")
    j12pp.draw(win)
    j13pp=Image(Point(214,212),"13pp.gif")
    j13pp.draw(win)
    j14pp=Image(Point(296,212),"14pp.gif")
    j14pp.draw(win)
    j15pp=Image(Point(378,212),"15pp.gif")
    j15pp.draw(win)
    j16pp=Image(Point(460,212),"16pp.gif")
    j16pp.draw(win)
    j17pp=Image(Point(542,212),"17pp.gif")
    j17pp.draw(win)
    j18pp=Image(Point(624,212),"18pp.gif")
    j18pp.draw(win)
    j19pp=Image(Point(706,212),"19pp.gif")
    j19pp.draw(win)
    j20pp=Image(Point(788,212),"20pp.gif")
    j20pp.draw(win)
    j21pp=Image(Point(50,344),"21pp.gif")
    j21pp.draw(win)
    j22pp=Image(Point(132,344),"22pp.gif")
    j22pp.draw(win)
    j23pp=Image(Point(214,344),"23pp.gif")
    j23pp.draw(win)
    j24pp=Image(Point(296,344),"24pp.gif")
    j24pp.draw(win)
    j25pp=Image(Point(378,344),"25pp.gif")
    j25pp.draw(win)
    j26pp=Image(Point(460,344),"26pp.gif")
    j26pp.draw(win)
    j27pp=Image(Point(542,344),"27pp.gif")
    j27pp.draw(win)
    j28pp=Image(Point(624,344),"28pp.gif")
    j28pp.draw(win)
    j29pp=Image(Point(706,344),"29pp.gif")
    j29pp.draw(win)
    j30pp=Image(Point(788,344),"30pp.gif")
    j30pp.draw(win)
    
    #CAIXA REGRAS
    caixaregras = Rectangle(Point(830,15),Point(1010,35))
    caixaregras.setFill("white")
    caixaregras.setOutline("blue2")
    caixaregras.draw(win)
    regrasdojogo1 = Text(Point(920,25),"REGRAS DO JOGO")
    regrasdojogo1.setSize(14)
    regrasdojogo1.draw(win)
    regrasdojogo2 = Text(Point(920,45),"clique acima para descobrir")
    regrasdojogo2.setSize(10)
    regrasdojogo2.draw(win)
    
    #TEXTO EM CIMA DOS PERSONAGENS
    regrasdojogo3 = Text(Point(410,7),"SELECIONE O PERSONAGEM QUE SEU AMIGO TERÁ QUE DESCOBRIR")
    regrasdojogo3.setSize(10)
    regrasdojogo3.draw(win)

    #IMAGENS DO LAYOUT DO JOGO
    caixaescolhido=Image(Point(962,306),"personagemselecionado.gif") #Point(923,242),Point(1002,370)
    caixaescolhido.draw(win)
    caixanome=Image(Point(921,112),"digitarnome.gif") #Point(840,64),Point(1002,160)
    caixanome.draw(win)
    caixatentativasrestantes=Image(Point(921,201),"tentativasrestantes.gif") #Point(840,172),Point(1002,230)
    caixatentativasrestantes.draw(win)
    caixasaida=Image(Point(667,477),"sair.gif") #Point(617,431),Point(718,523)
    caixasaida.draw(win)
    caixaperguntaanterior=Image(Point(50,477),"setaesquerda.gif") #Point(9,431),Point(91,523)
    caixaperguntaanterior.draw(win)
    caixaperguntaposterior=Image(Point(541,477),"setadireita.gif") #Point(500,431),Point(582,523)
    caixaperguntaposterior.draw(win)
    caixapergunta=Image(Point(295,477),"pergunta.gif") #Point(120,431),Point(471,523)
    caixapergunta.draw(win)
    caixamensagem=Image(Point(875,477),"mensagem.gif") #Point(747,431),Point(1002,523)
    caixamensagem.draw(win)
    
    
    #PERSONAGENS ATIVOS
    per1 = 1
    per2 = 1
    per3 = 1
    per4 = 1
    per5 = 1
    per6 = 1
    per7 = 1
    per8 = 1
    per9 = 1
    per10 = 1
    per11 = 1
    per12 = 1
    per13 = 1
    per14 = 1
    per15 = 1
    per16 = 1
    per17 = 1
    per18 = 1
    per19 = 1
    per20 = 1
    per21 = 1
    per22 = 1
    per23 = 1
    per24 = 1
    per25 = 1
    per26 = 1
    per27 = 1
    per28 = 1
    per29 = 1
    per30 = 1

    pergunta = 0

    aviso = Text(Point(295,540),"CLIQUE NA PERGUNTA PARA CONFIRMAR")
    aviso.setSize(10)
    aviso.draw(win)
    arquivo = open("Perguntas.txt", "r")
    linhas = arquivo.readlines()
    perguntaatual = Text(Point(295,477),(linhas[pergunta]))
    perguntaatual.setSize(12)
    perguntaatual.draw(win)

    textoresposta = Text(Point(880,478),"AGUARDANDO")
    textoresposta.setSize(20)
    textoresposta.draw(win)

    #VARIAVEL PARA O JOGO SEGUIR
    j2 = 1

    #VARIAVEL DO PERSONAGEM SELECIONADO
    computador = random.randrange(30)
    escolhido = computador+1
    listapersonagem = ()

    #VARIÁVEL DE SAÍDA
    saida = 0

    #VARIÁVEL DE PERSONAGENS RESTANTES
    restantes = 29

    #VARIÁVEL CONTADOR DE TENTATIVAS
    contador = 5
    textocontador = Text(Point(916,212),(contador))
    textocontador.setSize(10)
    textocontador.draw(win)

    if escolhido < 10:
        certo = "0{}pp.gif".format(escolhido)
        imagemdoescolhido = Image(Point(962,306),(certo))
        imagemdoescolhido.draw(win)
        regrasdojogo3.undraw()
        regrasdojogo3 = Text(Point(410,7),"SELECIONE O PERSONAGEM QUE DESEJA VER MAIOR")
        regrasdojogo3.setSize(10)
        regrasdojogo3.draw(win)
        caixaescolhido.undraw()
        caixaescolhido2=Image(Point(962,306),"personagemselecionado2.gif") #Point(923,242),Point(1002,370)
        caixaescolhido2.draw(win)
    if escolhido >= 10:
        certo = "{}pp.gif".format(escolhido)
        imagemdoescolhido = Image(Point(962,306),(certo))
        imagemdoescolhido.draw(win)
        regrasdojogo3.undraw()
        regrasdojogo3 = Text(Point(410,7),"SELECIONE O PERSONAGEM QUE DESEJA VER MAIOR")
        regrasdojogo3.setSize(10)
        regrasdojogo3.draw(win)
        caixaescolhido.undraw()
        caixaescolhido2=Image(Point(962,306),"personagemselecionado2.gif") #Point(923,242),Point(1002,370)
        caixaescolhido2.draw(win)

    while j2 != 0:
        b = win.getMouse()
        x = b.x
        y = b.y

        #REGRAS
        if x>830 and x<1010 and y>15 and y<35:
            Regras()
            x = 0
            y = 0

        #SAÍDA
        if x>617 and x<718 and y>431 and y<523:
            confirmacaosaida=Image(Point(512,280),"saidageral.gif") #Point(747,431),Point(1002,523)
            confirmacaosaida.draw(win)
            while saida == 0:
                saidamouse = win.getMouse()
                x = saidamouse.x
                y = saidamouse.y
                if x>251 and x<435 and y>253 and y<340:
                    win.close()
                    saida = 1
                if x>474 and x<657 and y>253 and y<340:
                    confirmacaosaida.undraw()
                    saida = 1
                    x=0
                    y=0
            saida = 0

        #SELEÇÃO DE PERSONAGENS
        if x>10 and x<89 and y>15 and y<145:
            j01=Image(Point(390,320),"01.gif")
            j01.draw(win)
            win.getMouse()
            j01.undraw()
        if x>91 and x<171 and y>15 and y<145:
            j02=Image(Point(390,320),"02.gif")
            j02.draw(win)
            win.getMouse()
            j02.undraw()
        if x>173 and x<253 and y>15 and y<145:
            j03=Image(Point(390,320),"03.gif")
            j03.draw(win)
            win.getMouse()
            j03.undraw()
        if x>257 and x<335 and y>15 and y<145:
            j04=Image(Point(390,320),"04.gif")
            j04.draw(win)
            win.getMouse()
            j04.undraw()
        if x>338 and x<417 and y>15 and y<145:
            j05=Image(Point(390,320),"05.gif")
            j05.draw(win)
            win.getMouse()
            j05.undraw()
        if x>420 and x<500 and y>15 and y<145:
            j06=Image(Point(390,320),"06.gif")
            j06.draw(win)
            win.getMouse()
            j06.undraw()
        if x>502 and x<581 and y>15 and y<145:
            j07=Image(Point(390,320),"07.gif")
            j07.draw(win)
            win.getMouse()
            j07.undraw()
        if x>584 and x<663 and y>15 and y<145:
            j08=Image(Point(390,320),"08.gif")
            j08.draw(win)
            win.getMouse()
            j08.undraw()
        if x>667 and x<745 and y>15 and y<145:
            j09=Image(Point(390,320),"09.gif")
            j09.draw(win)
            win.getMouse()
            j09.undraw()
        if x>749 and x<827 and y>15 and y<145:
            j10=Image(Point(390,320),"10.gif")
            j10.draw(win)
            win.getMouse()
            j10.undraw()
        if x>10 and x<89 and y>147 and y<276:
            j11=Image(Point(390,320),"11.gif")
            j11.draw(win)
            win.getMouse()
            j11.undraw()
        if x>91 and x<171 and y>147 and y<276:
            j12=Image(Point(390,320),"12.gif")
            j12.draw(win)
            win.getMouse()
            j12.undraw()
        if x>173 and x<253 and y>147 and y<276:
            j13=Image(Point(390,320),"13.gif")
            j13.draw(win)
            win.getMouse()
            j13.undraw()
        if x>257 and x<335 and y>147 and y<276:
            j14=Image(Point(390,320),"14.gif")
            j14.draw(win)
            win.getMouse()
            j14.undraw()
        if x>338 and x<417 and y>147 and y<276:
            j15=Image(Point(390,320),"15.gif")
            j15.draw(win)
            win.getMouse()
            j15.undraw()
        if x>420 and x<500 and y>147 and y<276:
            j16=Image(Point(390,320),"16.gif")
            j16.draw(win)
            win.getMouse()
            j16.undraw()
        if x>502 and x<581 and y>147 and y<276:
            j17=Image(Point(390,320),"17.gif")
            j17.draw(win)
            win.getMouse()
            j17.undraw()
        if x>584 and x<663 and y>147 and y<276:
            j18=Image(Point(390,320),"18.gif")
            j18.draw(win)
            win.getMouse()
            j18.undraw()
        if x>667 and x<745 and y>147 and y<276:
            j19=Image(Point(390,320),"19.gif")
            j19.draw(win)
            win.getMouse()
            j19.undraw()
        if x>749 and x<827 and y>147 and y<276:
            j20=Image(Point(390,320),"20.gif")
            j20.draw(win)
            win.getMouse()
            j20.undraw()
        if x>10 and x<89 and y>279 and y<408:
            j21=Image(Point(390,320),"21.gif")
            j21.draw(win)
            win.getMouse()
            j21.undraw()
        if x>91 and x<171 and y>279 and y<408:
            j22=Image(Point(390,320),"22.gif")
            j22.draw(win)
            win.getMouse()
            j22.undraw()
        if x>173 and x<253 and y>279 and y<408:
            j23=Image(Point(390,320),"23.gif")
            j23.draw(win)
            win.getMouse()
            j23.undraw()
        if x>257 and x<335 and y>279 and y<408:
            j24=Image(Point(390,320),"24.gif")
            j24.draw(win)
            win.getMouse()
            j24.undraw()
        if x>338 and x<417 and y>279 and y<408:
            j25=Image(Point(390,320),"25.gif")
            j25.draw(win)
            win.getMouse()
            j25.undraw()
        if x>420 and x<500 and y>279 and y<408:
            j26=Image(Point(390,320),"26.gif")
            j26.draw(win)
            win.getMouse()
            j26.undraw()
        if x>502 and x<581 and y>279 and y<408:
            j27=Image(Point(390,320),"27.gif")
            j27.draw(win)
            win.getMouse()
            j27.undraw()
        if x>584 and x<663 and y>279 and y<408:
            j28=Image(Point(390,320),"28.gif")
            j28.draw(win)
            win.getMouse()
            j28.undraw()
        if x>667 and x<745 and y>279 and y<408:
            j29=Image(Point(390,320),"29.gif")
            j29.draw(win)
            win.getMouse()
            j29.undraw()
        if x>749 and x<827 and y>279 and y<408:
            j30=Image(Point(390,320),"30.gif")
            j30.draw(win)
            win.getMouse()
            j30.undraw()

        

        #Atribuições de cada escolhido para as perguntas
        if escolhido == 1:
            listapersonagem = "Cecília","cecília","Cecilia","cecilia","CECILIA","CECÍLIA",1,4,15,16,19,21
        if escolhido == 2:
            listapersonagem = "Mariana","mariana","MARIANA",3,8,9,15,17,20,21
        if escolhido == 3:
            listapersonagem = "Paula","paula","PAULA",2,8,9,15,18,20,21
        if escolhido == 4:
            listapersonagem = "Juliana","juliana","JULIANA",2,15,19,20,21
        if escolhido == 5:
            listapersonagem = "Sabrina","sabrina","SABRINA",5,15,19,20,21
        if escolhido == 6:
            listapersonagem = "Giulia","giulia","GIULIA","julia","Julia","JULIA",1,6,15,17,20,21
        if escolhido == 7:
            listapersonagem = "Fernanda","fernanda","FERNANDA",2,15,16,18,20,21
        if escolhido == 8:
            listapersonagem = "Jorge","jorge","JORGE",5,11,12,14,19
        if escolhido == 9:
            listapersonagem = "Maria Flor","Maria","Flor","maria flor","maria","flor","MARIA FLOR",3,15,18,20
        if escolhido == 10:
            listapersonagem = "Débora","Debora","débora","debora","DEBORA","DÉBORA",5,8,9,15,16,19,20,21
        if escolhido == 11:
            listapersonagem = "Odete","odete","ODETE",1,4,15,16,17,20
        if escolhido == 12:
            listapersonagem = "Alice","alice","ALICE",5,9,10,15,19,20
        if escolhido == 13:
            listapersonagem = "Gabriela","gabriela","GABRIELA",1,2,9,10,15,16,17,20,21
        if escolhido == 14:
            listapersonagem = "Olavo","olavo","OLAVO",1,3,14,18,22
        if escolhido == 15:
            listapersonagem = "Raul","raul","RAUL",1,2,8,9,14,17
        if escolhido == 16:
            listapersonagem = "Zeca","zeca","ZECA",1,3,11,12,13,14,18,21
        if escolhido == 17:
            listapersonagem = "Roberto","roberto","ROBERTO",1,2,11,12,13,14,19,20,22
        if escolhido == 18:
            listapersonagem = "João","joão","JOÃO","Joao","joao","JOAO",1,4,8,9,14,19,22
        if escolhido == 19:
            listapersonagem = "Pedro","pedro","PEDRO",1,4,11,13,14,19,22
        if escolhido == 20:
            listapersonagem = "Bernardo","bernardo","BERNARDO",2,14,19,20,22
        if escolhido == 21:
            listapersonagem = "Alberto","alberto","ALBERTO",1,2,11,12,13,14,19,22
        if escolhido == 22:
            listapersonagem = "Alfredo","alfredo","ALFREDO",5,8,9,11,12,13,14,19,20,22
        if escolhido == 23:
            listapersonagem = "Henrique","henrique","HENRIQUE",1,7,14,19
        if escolhido == 24:
            listapersonagem = "Gilberto","gilberto","GILBERTO",1,6,11,12,13,14,18,22
        if escolhido == 25:
            listapersonagem = "Patrícia","patrícia","PATRÍCIA","Patricia","patricia","PATRICIA",1,2,8,9,10,15,19,20,21
        if escolhido == 26:
            listapersonagem = "Cláudia","cláudia","CLÁUDIA","Claudia","claudia","CLAUDIA",1,2,15,16,19,20,21
        if escolhido == 27:
            listapersonagem = "Anna","anna","ANNA","Ana","ana","ANA",5,9,10,15,19,20,21
        if escolhido == 28:
            listapersonagem = "Joaquim","joaquim","JOAQUIM",7,8,9,11,13,14,19
        if escolhido == 29:
            listapersonagem = "Chico","chico","CHICO","Francisco","francisco","FRANCISCO",4,7,14,17,20,22
        if escolhido == 30:
            listapersonagem = "Samir","samir","SAMIR",2,9,10,11,12,13,14,19

        listapersonagem1 = 1,4,15,16,19,21
        listapersonagem2 = 3,8,9,15,17,20,21
        listapersonagem3 = 2,8,9,15,18,20,21
        listapersonagem4 = 2,15,19,20,21
        listapersonagem5 = 5,15,19,20,21
        listapersonagem6 = 1,6,15,17,20,21
        listapersonagem7 = 2,15,16,18,20,21
        listapersonagem8 = 5,11,12,14,19
        listapersonagem9 = 3,15,18,20
        listapersonagem10 = 5,8,9,15,16,19,20,21
        listapersonagem11 = 1,4,15,16,17,20
        listapersonagem12 = 5,9,10,15,19,20
        listapersonagem13 = 1,2,9,10,15,16,17,20,21
        listapersonagem14 = 1,3,14,18,22
        listapersonagem15 = 1,2,8,9,14,17
        listapersonagem16 = 1,3,11,12,13,14,18,21
        listapersonagem17 = 1,2,11,12,13,14,19,20,22
        listapersonagem18 = 1,4,8,9,14,19,22
        listapersonagem19 = 1,4,11,13,14,19,22
        listapersonagem20 = 2,14,19,20,22
        listapersonagem21 = 1,2,11,12,13,14,19,22
        listapersonagem22 = 5,8,9,11,12,13,14,19,20,22
        listapersonagem23 = 1,7,14,19
        listapersonagem24 = 1,6,11,12,13,14,18,22
        listapersonagem25 = 1,2,8,9,10,15,19,20,21
        listapersonagem26 = 1,2,15,16,19,20,21
        listapersonagem27 = 5,9,10,15,19,20,21
        listapersonagem28 = 7,8,9,11,13,14,19
        listapersonagem29 = 4,7,14,17,20,22
        listapersonagem30 = 2,9,10,11,12,13,14,19

        #PERGUNTAS
        
        if x>9 and x<91 and y>431 and y<523 and pergunta > 0 and escolhido != 0 and contador !=0:
            pergunta = pergunta - 1
            x = 0
            y = 0
            perguntaatual.undraw()
            perguntaatual = Text(Point(295,477),(linhas[pergunta]))
            perguntaatual.setSize(12)
            perguntaatual.draw(win) #seta esquerda
        if x>500 and x<582 and y>431 and y<523 and pergunta < 22 and escolhido != 0 and contador !=0:
            pergunta = pergunta + 1
            x = 0
            y = 0
            perguntaatual.undraw()
            perguntaatual = Text(Point(295,477),(linhas[pergunta]))
            perguntaatual.setSize(12)
            perguntaatual.draw(win) #seta direita
        if x>120 and x<471 and y>431 and y<523 and escolhido != 0 and contador !=0 and pergunta !=0: #caixa perguntas
            textocontador.undraw()
            contador = contador - 1
            textocontador = Text(Point(916,212),(contador))
            textocontador.setSize(10)
            textocontador.draw(win)
            x = 0
            y = 0
            if pergunta in listapersonagem:
                v = "SIM"
                textoresposta.undraw()
                textoresposta = Text(Point(880,478),(v))
                textoresposta.setSize(36)
                textoresposta.draw(win)
                if pergunta in listapersonagem1:
                    oi = 0
                else:
                    j01pp.undraw()
                    if per1 == 1:
                        restantes = restantes - 1
                        per1 = 0
                if pergunta in listapersonagem2:
                    oi = 0
                else:
                    j02pp.undraw()
                    if per2 == 1:
                        restantes = restantes - 1
                        per2 = 0
                if pergunta in listapersonagem3:
                    oi = 0
                else:
                    j03pp.undraw()
                    if per3 == 1:
                        restantes = restantes - 1
                        per3 = 0
                if pergunta in listapersonagem4:
                    oi = 0
                else:
                    j04pp.undraw()
                    if per4 == 1:
                        restantes = restantes - 1
                        per4 = 0
                if pergunta in listapersonagem5:
                    oi = 0
                else:
                    j05pp.undraw()
                    if per5 == 1:
                        restantes = restantes - 1
                        per5 = 0
                if pergunta in listapersonagem6:
                    oi = 0
                else:
                    j06pp.undraw()
                    if per6 == 1:
                        restantes = restantes - 1
                        per6 = 0
                if pergunta in listapersonagem7:
                    oi = 0
                else:
                    j07pp.undraw()
                    if per7 == 1:
                        restantes = restantes - 1
                        per7 = 0
                if pergunta in listapersonagem8:
                    oi = 0
                else:
                    j08pp.undraw()
                    if per8 == 1:
                        restantes = restantes - 1
                        per8 = 0
                if pergunta in listapersonagem9:
                    oi = 0
                else:
                    j09pp.undraw()
                    if per9 == 1:
                        restantes = restantes - 1
                        per9 = 0
                if pergunta in listapersonagem10:
                    oi = 0
                else:
                    j10pp.undraw()
                    if per10 == 1:
                        restantes = restantes - 1
                        per10 = 0
                if pergunta in listapersonagem11:
                    oi = 0
                else:
                    j11pp.undraw()
                    if per11 == 1:
                        restantes = restantes - 1
                        per11 = 0
                if pergunta in listapersonagem12:
                    oi = 0
                else:
                    j12pp.undraw()
                    if per12 == 1:
                        restantes = restantes - 1
                        per12 = 0
                if pergunta in listapersonagem13:
                    oi = 0
                else:
                    j13pp.undraw()
                    if per13 == 1:
                        restantes = restantes - 1
                        per13 = 0
                if pergunta in listapersonagem14:
                    oi = 0
                else:
                    j14pp.undraw()
                    if per14 == 1:
                        restantes = restantes - 1
                        per14 = 0
                if pergunta in listapersonagem15:
                    oi = 0
                else:
                    j15pp.undraw()
                    if per15 == 1:
                        restantes = restantes - 1
                        per15 = 0
                if pergunta in listapersonagem16:
                    oi = 0
                else:
                    j16pp.undraw()
                    if per16 == 1:
                        restantes = restantes - 1
                        per16 = 0
                if pergunta in listapersonagem17:
                    oi = 0
                else:
                    j17pp.undraw()
                    if per17 == 1:
                        restantes = restantes - 1
                        per17 = 0
                if pergunta in listapersonagem18:
                    oi = 0
                else:
                    j18pp.undraw()
                    if per18 == 1:
                        restantes = restantes - 1
                        per18 = 0
                if pergunta in listapersonagem19:
                    oi = 0
                else:
                    j19pp.undraw()
                    if per19 == 1:
                        restantes = restantes - 1
                        per19 = 0
                if pergunta in listapersonagem20:
                    oi = 0
                else:
                    j20pp.undraw()
                    if per20 == 1:
                        restantes = restantes - 1
                        per20 = 0
                if pergunta in listapersonagem21:
                    oi = 0
                else:
                    j21pp.undraw()
                    if per21 == 1:
                        restantes = restantes - 1
                        per21 = 0
                if pergunta in listapersonagem22:
                    oi = 0
                else:
                    j22pp.undraw()
                    if per22 == 1:
                        restantes = restantes - 1
                        per22 = 0
                if pergunta in listapersonagem23:
                    oi = 0
                else:
                    j23pp.undraw()
                    if per23 == 1:
                        restantes = restantes - 1
                        per23 = 0
                if pergunta in listapersonagem24:
                    oi = 0
                else:
                    j24pp.undraw()
                    if per24 == 1:
                        restantes = restantes - 1
                        per24 = 0
                if pergunta in listapersonagem25:
                    oi = 0
                else:
                    j25pp.undraw()
                    if per25 == 1:
                        restantes = restantes - 1
                        per25 = 0
                if pergunta in listapersonagem26:
                    oi = 0
                else:
                    j26pp.undraw()
                    if per26 == 1:
                        restantes = restantes - 1
                        per26 = 0
                if pergunta in listapersonagem27:
                    oi = 0
                else:
                    j27pp.undraw()
                    if per27 == 1:
                        restantes = restantes - 1
                        per27 = 0
                if pergunta in listapersonagem28:
                    oi = 0
                else:
                    j28pp.undraw()
                    if per28 == 1:
                        restantes = restantes - 1
                        per28 = 0
                if pergunta in listapersonagem29:
                    oi = 0
                else:
                    j29pp.undraw()
                    if per29 == 1:
                        restantes = restantes - 1
                        per29 = 0
                if pergunta in listapersonagem30:
                    oi = 0
                else:
                    j30pp.undraw()
                    if per30 == 1:
                        restantes = restantes - 1
                        per30 = 0
            else:
                v = "NÃO"
                textoresposta.undraw()
                textoresposta = Text(Point(880,478),(v))
                textoresposta.setSize(36)
                textoresposta.draw(win)
                if pergunta in listapersonagem1:
                    j01pp.undraw()
                    if per1 == 1:
                        restantes = restantes - 1
                        per1 = 0
                if pergunta in listapersonagem2:
                    j02pp.undraw()
                    if per2 == 1:
                        restantes = restantes - 1
                        per2 = 0
                if pergunta in listapersonagem3:
                    j03pp.undraw()
                    if per3 == 1:
                        restantes = restantes - 1
                        per3 = 0
                if pergunta in listapersonagem4:
                    j04pp.undraw()
                    if per4 == 1:
                        restantes = restantes - 1
                        per4 = 0
                if pergunta in listapersonagem5:
                    j05pp.undraw()
                    if per5 == 1:
                        restantes = restantes - 1
                        per5 = 0
                if pergunta in listapersonagem6:
                    j06pp.undraw()
                    if per6 == 1:
                        restantes = restantes - 1
                        per6 = 0
                if pergunta in listapersonagem7:
                    j07pp.undraw()
                    if per7 == 1:
                        restantes = restantes - 1
                        per7 = 0
                if pergunta in listapersonagem8:
                    j08pp.undraw()
                    if per8 == 1:
                        restantes = restantes - 1
                        per8 = 0
                if pergunta in listapersonagem9:
                    j09pp.undraw()
                    if per9 == 1:
                        restantes = restantes - 1
                        per9 = 0
                if pergunta in listapersonagem10:
                    j10pp.undraw()
                    if per10 == 1:
                        restantes = restantes - 1
                        per10 = 0
                if pergunta in listapersonagem11:
                    j11pp.undraw()
                    if per11 == 1:
                        restantes = restantes - 1
                        per11 = 0
                if pergunta in listapersonagem12:
                    j12pp.undraw()
                    if per12 == 1:
                        restantes = restantes - 1
                        per12 = 0
                if pergunta in listapersonagem13:
                    j13pp.undraw()
                    if per13 == 1:
                        restantes = restantes - 1
                        per13 = 0
                if pergunta in listapersonagem14:
                    j14pp.undraw()
                    if per14 == 1:
                        restantes = restantes - 1
                        per14 = 0
                if pergunta in listapersonagem15:
                    j15pp.undraw()
                    if per15 == 1:
                        restantes = restantes - 1
                        per15 = 0
                if pergunta in listapersonagem16:
                    j16pp.undraw()
                    if per16 == 1:
                        restantes = restantes - 1
                        per16 = 0
                if pergunta in listapersonagem17:
                    j17pp.undraw()
                    if per17 == 1:
                        restantes = restantes - 1
                        per17 = 0
                if pergunta in listapersonagem18:
                    j18pp.undraw()
                    if per18 == 1:
                        restantes = restantes - 1
                        per18 = 0
                if pergunta in listapersonagem19:
                    j19pp.undraw()
                    if per19 == 1:
                        restantes = restantes - 1
                        per19 = 0
                if pergunta in listapersonagem20:
                    j20pp.undraw()
                    if per20 == 1:
                        restantes = restantes - 1
                        per20 = 0
                if pergunta in listapersonagem21:
                    j21pp.undraw()
                    if per21 == 1:
                        restantes = restantes - 1
                        per21 = 0
                if pergunta in listapersonagem22:
                    j22pp.undraw()
                    if per22 == 1:
                        restantes = restantes - 1
                        per22 = 0
                if pergunta in listapersonagem23:
                    j23pp.undraw()
                    if per23 == 1:
                        restantes = restantes - 1
                        per23 = 0
                if pergunta in listapersonagem24:
                    j24pp.undraw()
                    if per24 == 1:
                        restantes = restantes - 1
                        per24 = 0
                if pergunta in listapersonagem25:
                    j25pp.undraw()
                    if per25 == 1:
                        restantes = restantes - 1
                        per25 = 0
                if pergunta in listapersonagem26:
                    j26pp.undraw()
                    if per26 == 1:
                        restantes = restantes - 1
                        per26 = 0
                if pergunta in listapersonagem27:
                    j27pp.undraw()
                    if per27 == 1:
                        restantes = restantes - 1
                        per27 = 0
                if pergunta in listapersonagem28:
                    j28pp.undraw()
                    if per28 == 1:
                        restantes = restantes - 1
                        per28 = 0
                if pergunta in listapersonagem29:
                    j29pp.undraw()
                    if per29 == 1:
                        restantes = restantes - 1
                        per29 = 0
                if pergunta in listapersonagem30:
                    j30pp.undraw()
                    if per30 == 1:
                        restantes = restantes - 1
                        per30 = 0
        
                        
        if restantes == 0:
            contador = 0
            caixamensagem.undraw()
            caixamensagem=Image(Point(875,477),"parabens.gif") #Point(747,431),Point(1002,523)
            caixamensagem.draw(win)
            caixaescolhido2.undraw()
            win.getMouse()
            win.close()
            Abertura()
        
        if restantes != 0 and contador == 0:
            camponome = Entry(Point(921,132), 10)
            camponome.setSize(20)
            camponome.setFill("white")
            camponome.draw(win)
            textoresposta.undraw()
            textoresposta = Text(Point(880,478),"DIGITE O NOME")
            textoresposta.draw(win)
            k = "a"
            while k != "Return":
                k = win.getKey()
                camponomes = camponome.getText()
            
            if camponomes in listapersonagem:
                contador = 0
                caixamensagem.undraw()
                caixamensagem=Image(Point(875,477),"parabens.gif") #Point(747,431),Point(1002,523)
                caixamensagem.draw(win)
                caixaescolhido2.undraw()
                win.getMouse()
                win.close()
                Abertura()
            
            else:
                caixamensagem.undraw()
                caixamensagem=Image(Point(875,477),"perdeu.gif") #Point(747,431),Point(1002,523)
                caixamensagem.draw(win)
                caixaescolhido2.undraw()
                win.getMouse()
                win.close()
                Abertura()

    win.getMouse()
    win.close()

def Jogo1():
    win=GraphWin("CARA A CARA",1024,560,autoflush=False)
        
    #INSERIR MINIATURAS NO LAYOUT
    j01pp=Image(Point(50,80),"01pp.gif")
    j01pp.draw(win)
    j02pp=Image(Point(132,80),"02pp.gif")
    j02pp.draw(win)
    j03pp=Image(Point(214,80),"03pp.gif")
    j03pp.draw(win)
    j04pp=Image(Point(296,80),"04pp.gif")
    j04pp.draw(win)
    j05pp=Image(Point(378,80),"05pp.gif")
    j05pp.draw(win)
    j06pp=Image(Point(460,80),"06pp.gif")
    j06pp.draw(win)
    j07pp=Image(Point(542,80),"07pp.gif")
    j07pp.draw(win)
    j08pp=Image(Point(624,80),"08pp.gif")
    j08pp.draw(win)
    j09pp=Image(Point(706,80),"09pp.gif")
    j09pp.draw(win)
    j10pp=Image(Point(788,80),"10pp.gif")
    j10pp.draw(win)
    j11pp=Image(Point(50,212),"11pp.gif")
    j11pp.draw(win)
    j12pp=Image(Point(132,212),"12pp.gif")
    j12pp.draw(win)
    j13pp=Image(Point(214,212),"13pp.gif")
    j13pp.draw(win)
    j14pp=Image(Point(296,212),"14pp.gif")
    j14pp.draw(win)
    j15pp=Image(Point(378,212),"15pp.gif")
    j15pp.draw(win)
    j16pp=Image(Point(460,212),"16pp.gif")
    j16pp.draw(win)
    j17pp=Image(Point(542,212),"17pp.gif")
    j17pp.draw(win)
    j18pp=Image(Point(624,212),"18pp.gif")
    j18pp.draw(win)
    j19pp=Image(Point(706,212),"19pp.gif")
    j19pp.draw(win)
    j20pp=Image(Point(788,212),"20pp.gif")
    j20pp.draw(win)
    j21pp=Image(Point(50,344),"21pp.gif")
    j21pp.draw(win)
    j22pp=Image(Point(132,344),"22pp.gif")
    j22pp.draw(win)
    j23pp=Image(Point(214,344),"23pp.gif")
    j23pp.draw(win)
    j24pp=Image(Point(296,344),"24pp.gif")
    j24pp.draw(win)
    j25pp=Image(Point(378,344),"25pp.gif")
    j25pp.draw(win)
    j26pp=Image(Point(460,344),"26pp.gif")
    j26pp.draw(win)
    j27pp=Image(Point(542,344),"27pp.gif")
    j27pp.draw(win)
    j28pp=Image(Point(624,344),"28pp.gif")
    j28pp.draw(win)
    j29pp=Image(Point(706,344),"29pp.gif")
    j29pp.draw(win)
    j30pp=Image(Point(788,344),"30pp.gif")
    j30pp.draw(win)
    
    #CAIXA REGRAS
    caixaregras = Rectangle(Point(830,15),Point(1010,35))
    caixaregras.setFill("white")
    caixaregras.setOutline("blue2")
    caixaregras.draw(win)
    regrasdojogo1 = Text(Point(920,25),"REGRAS DO JOGO")
    regrasdojogo1.setSize(14)
    regrasdojogo1.draw(win)
    regrasdojogo2 = Text(Point(920,45),"clique acima para descobrir")
    regrasdojogo2.setSize(10)
    regrasdojogo2.draw(win)
    
    #TEXTO EM CIMA DOS PERSONAGENS
    regrasdojogo3 = Text(Point(410,7),"SELECIONE O PERSONAGEM QUE SEU AMIGO TERÁ QUE DESCOBRIR")
    regrasdojogo3.setSize(10)
    regrasdojogo3.draw(win)

    #IMAGENS DO LAYOUT DO JOGO
    caixaescolhido=Image(Point(962,306),"personagemselecionado.gif") #Point(923,242),Point(1002,370)
    caixaescolhido.draw(win)
    caixanome=Image(Point(921,112),"digitarnome.gif") #Point(840,64),Point(1002,160)
    caixanome.draw(win)
    caixatentativasrestantes=Image(Point(921,201),"tentativasrestantes.gif") #Point(840,172),Point(1002,230)
    caixatentativasrestantes.draw(win)
    caixasaida=Image(Point(667,477),"sair.gif") #Point(617,431),Point(718,523)
    caixasaida.draw(win)
    caixaperguntaanterior=Image(Point(50,477),"setaesquerda.gif") #Point(9,431),Point(91,523)
    caixaperguntaanterior.draw(win)
    caixaperguntaposterior=Image(Point(541,477),"setadireita.gif") #Point(500,431),Point(582,523)
    caixaperguntaposterior.draw(win)
    caixapergunta=Image(Point(295,477),"pergunta.gif") #Point(120,431),Point(471,523)
    caixapergunta.draw(win)
    caixamensagem=Image(Point(875,477),"mensagem.gif") #Point(747,431),Point(1002,523)
    caixamensagem.draw(win)
    
    
    #PERSONAGENS ATIVOS
    per1 = 1
    per2 = 1
    per3 = 1
    per4 = 1
    per5 = 1
    per6 = 1
    per7 = 1
    per8 = 1
    per9 = 1
    per10 = 1
    per11 = 1
    per12 = 1
    per13 = 1
    per14 = 1
    per15 = 1
    per16 = 1
    per17 = 1
    per18 = 1
    per19 = 1
    per20 = 1
    per21 = 1
    per22 = 1
    per23 = 1
    per24 = 1
    per25 = 1
    per26 = 1
    per27 = 1
    per28 = 1
    per29 = 1
    per30 = 1

    pergunta = 0

    aviso = Text(Point(295,540),"CLIQUE NA PERGUNTA PARA CONFIRMAR")
    aviso.setSize(10)
    aviso.draw(win)
    arquivo = open("Perguntas.txt", "r")
    linhas = arquivo.readlines()
    perguntaatual = Text(Point(295,477),(linhas[pergunta]))
    perguntaatual.setSize(12)
    perguntaatual.draw(win)

    textoresposta = Text(Point(880,478),"AGUARDANDO")
    textoresposta.setSize(20)
    textoresposta.draw(win)

    #VARIAVEL PARA O JOGO SEGUIR
    j2 = 1

    #VARIAVEL DO PERSONAGEM SELECIONADO
    escolhido = 0
    listapersonagem = ()

    #VARIÁVEL DE SAÍDA
    saida = 0

    #VARIÁVEL DE PERSONAGENS RESTANTES
    restantes = 29

    #VARIÁVEL CONTADOR DE TENTATIVAS
    contador = 5
    textocontador = Text(Point(916,212),(contador))
    textocontador.setSize(10)
    textocontador.draw(win)

    while j2 != 0:
        b = win.getMouse()
        x = b.x
        y = b.y

        #REGRAS
        if x>830 and x<1010 and y>15 and y<35:
            Regras()
            x = 0
            y = 0

        #SAÍDA
        if x>617 and x<718 and y>431 and y<523:
            confirmacaosaida=Image(Point(512,280),"saidageral.gif") #Point(747,431),Point(1002,523)
            confirmacaosaida.draw(win)
            while saida == 0:
                saidamouse = win.getMouse()
                x = saidamouse.x
                y = saidamouse.y
                if x>251 and x<435 and y>253 and y<340:
                    win.close()
                    saida = 1
                if x>474 and x<657 and y>253 and y<340:
                    confirmacaosaida.undraw()
                    saida = 1
                    x=0
                    y=0
            saida = 0
        
               
        #SELEÇÃO DE PERSONAGENS
        if x>10 and x<89 and y>15 and y<145:
            j01=Image(Point(390,320),"01.gif")
            j01.draw(win)
            if escolhido != 0:
                win.getMouse()
                j01.undraw()
            if escolhido == 0:
                h = 1
                caixaconfirma = Rectangle(Point(600,180),Point(790,220))
                caixaconfirma.setFill("white")
                caixaconfirma.setOutline("blue2")
                caixaconfirma.draw(win)
                caixaconfirmasim = Rectangle(Point(600,230),Point(690,270))
                caixaconfirmasim.setFill("green2")
                caixaconfirmasim.setOutline("green2")
                caixaconfirmasim.draw(win)
                caixaconfirmanao = Rectangle(Point(700,230),Point(790,270))
                caixaconfirmanao.setFill("red2")
                caixaconfirmanao.setOutline("red2")
                caixaconfirmanao.draw(win)
                confirmar = Text(Point(700,200),"CONFIRMA?")
                confirmar.setSize(20)
                confirmar.draw(win)
                confirmarsim = Text(Point(645,250),"SIM")
                confirmarsim.setSize(20)
                confirmarsim.draw(win)
                confirmarnao = Text(Point(745,250),"NAO")
                confirmarnao.setSize(20)
                confirmarnao.draw(win)
                while h != 0:
                    p = win.getMouse()
                    x = p.x
                    y = p.y
                    if x>600 and x<690 and y>230 and y<270:
                        h = 0
                        escolhido = 1
                        j01pp=Image(Point(962,306),"01pp.gif")
                        j01pp.draw(win)
                        caixaconfirma.undraw()
                        caixaconfirmasim.undraw()
                        caixaconfirmanao.undraw()
                        confirmar.undraw()
                        confirmarsim.undraw()
                        confirmarnao.undraw()
                        x = 0
                        y = 0
                        j01.undraw()
                        regrasdojogo3.undraw()
                        regrasdojogo3 = Text(Point(410,7),"SELECIONE O PERSONAGEM QUE DESEJA VER MAIOR")
                        regrasdojogo3.setSize(10)
                        regrasdojogo3.draw(win)
                        caixaescolhido.undraw()
                        caixaescolhido2=Image(Point(962,306),"personagemselecionado2.gif") #Point(923,242),Point(1002,370)
                        caixaescolhido2.draw(win)

                    if x>700 and x<790 and y>230 and y<270:
                        h = 0
                        escolhido = 0
                        caixaconfirma.undraw()
                        caixaconfirmasim.undraw()
                        caixaconfirmanao.undraw()
                        confirmar.undraw()
                        confirmarsim.undraw()
                        confirmarnao.undraw()
                        x = 0
                        y = 0
                        j01.undraw()    #1                                                        
        if x>91 and x<171 and y>15 and y<145:
            j02=Image(Point(390,320),"02.gif")
            j02.draw(win)
            if escolhido != 0:
                win.getMouse()
                j02.undraw()
            if escolhido == 0:
                h = 1
                caixaconfirma = Rectangle(Point(600,180),Point(790,220))
                caixaconfirma.setFill("white")
                caixaconfirma.setOutline("blue2")
                caixaconfirma.draw(win)
                caixaconfirmasim = Rectangle(Point(600,230),Point(690,270))
                caixaconfirmasim.setFill("green2")
                caixaconfirmasim.setOutline("green2")
                caixaconfirmasim.draw(win)
                caixaconfirmanao = Rectangle(Point(700,230),Point(790,270))
                caixaconfirmanao.setFill("red2")
                caixaconfirmanao.setOutline("red2")
                caixaconfirmanao.draw(win)
                confirmar = Text(Point(700,200),"CONFIRMA?")
                confirmar.setSize(20)
                confirmar.draw(win)
                confirmarsim = Text(Point(645,250),"SIM")
                confirmarsim.setSize(20)
                confirmarsim.draw(win)
                confirmarnao = Text(Point(745,250),"NAO")
                confirmarnao.setSize(20)
                confirmarnao.draw(win)
                while h != 0:
                    p = win.getMouse()
                    x = p.x
                    y = p.y
                    if x>600 and x<690 and y>230 and y<270:
                        h = 0
                        escolhido = 2
                        j02pp=Image(Point(962,306),"02pp.gif")
                        j02pp.draw(win)
                        caixaconfirma.undraw()
                        caixaconfirmasim.undraw()
                        caixaconfirmanao.undraw()
                        confirmar.undraw()
                        confirmarsim.undraw()
                        confirmarnao.undraw()
                        x = 0
                        y = 0
                        j02.undraw()
                        regrasdojogo3.undraw()
                        regrasdojogo3 = Text(Point(410,7),"SELECIONE O PERSONAGEM QUE DESEJA VER MAIOR")
                        regrasdojogo3.setSize(10)
                        regrasdojogo3.draw(win)
                        caixaescolhido.undraw()
                        caixaescolhido2=Image(Point(962,306),"personagemselecionado2.gif") #Point(923,242),Point(1002,370)
                        caixaescolhido2.draw(win)

                    if x>700 and x<790 and y>230 and y<270:
                        h = 0
                        escolhido = 0
                        caixaconfirma.undraw()
                        caixaconfirmasim.undraw()
                        caixaconfirmanao.undraw()
                        confirmar.undraw()
                        confirmarsim.undraw()
                        confirmarnao.undraw()
                        x = 0
                        y = 0
                        j02.undraw()   #2
        if x>173 and x<253 and y>15 and y<145:
            j03=Image(Point(390,320),"03.gif")
            j03.draw(win)
            if escolhido != 0:
                win.getMouse()
                j03.undraw()
            if escolhido == 0:
                h = 1
                caixaconfirma = Rectangle(Point(600,180),Point(790,220))
                caixaconfirma.setFill("white")
                caixaconfirma.setOutline("blue2")
                caixaconfirma.draw(win)
                caixaconfirmasim = Rectangle(Point(600,230),Point(690,270))
                caixaconfirmasim.setFill("green2")
                caixaconfirmasim.setOutline("green2")
                caixaconfirmasim.draw(win)
                caixaconfirmanao = Rectangle(Point(700,230),Point(790,270))
                caixaconfirmanao.setFill("red2")
                caixaconfirmanao.setOutline("red2")
                caixaconfirmanao.draw(win)
                confirmar = Text(Point(700,200),"CONFIRMA?")
                confirmar.setSize(20)
                confirmar.draw(win)
                confirmarsim = Text(Point(645,250),"SIM")
                confirmarsim.setSize(20)
                confirmarsim.draw(win)
                confirmarnao = Text(Point(745,250),"NAO")
                confirmarnao.setSize(20)
                confirmarnao.draw(win)
                while h != 0:
                    p = win.getMouse()
                    x = p.x
                    y = p.y
                    if x>600 and x<690 and y>230 and y<270:
                        h = 0
                        escolhido = 3
                        j03pp=Image(Point(962,306),"03pp.gif")
                        j03pp.draw(win)
                        caixaconfirma.undraw()
                        caixaconfirmasim.undraw()
                        caixaconfirmanao.undraw()
                        confirmar.undraw()
                        confirmarsim.undraw()
                        confirmarnao.undraw()
                        x = 0
                        y = 0
                        j03.undraw()
                        regrasdojogo3.undraw()
                        regrasdojogo3 = Text(Point(410,7),"SELECIONE O PERSONAGEM QUE DESEJA VER MAIOR")
                        regrasdojogo3.setSize(10)
                        regrasdojogo3.draw(win)
                        caixaescolhido.undraw()
                        caixaescolhido2=Image(Point(962,306),"personagemselecionado2.gif") #Point(923,242),Point(1002,370)
                        caixaescolhido2.draw(win)

                    if x>700 and x<790 and y>230 and y<270:
                        h = 0
                        escolhido = 0
                        caixaconfirma.undraw()
                        caixaconfirmasim.undraw()
                        caixaconfirmanao.undraw()
                        confirmar.undraw()
                        confirmarsim.undraw()
                        confirmarnao.undraw()
                        x = 0
                        y = 0
                        j03.undraw()  #3
        if x>257 and x<335 and y>15 and y<145:
            j04=Image(Point(390,320),"04.gif")
            j04.draw(win)
            if escolhido != 0:
                win.getMouse()
                j04.undraw()
            if escolhido == 0:
                h = 1
                caixaconfirma = Rectangle(Point(600,180),Point(790,220))
                caixaconfirma.setFill("white")
                caixaconfirma.setOutline("blue2")
                caixaconfirma.draw(win)
                caixaconfirmasim = Rectangle(Point(600,230),Point(690,270))
                caixaconfirmasim.setFill("green2")
                caixaconfirmasim.setOutline("green2")
                caixaconfirmasim.draw(win)
                caixaconfirmanao = Rectangle(Point(700,230),Point(790,270))
                caixaconfirmanao.setFill("red2")
                caixaconfirmanao.setOutline("red2")
                caixaconfirmanao.draw(win)
                confirmar = Text(Point(700,200),"CONFIRMA?")
                confirmar.setSize(20)
                confirmar.draw(win)
                confirmarsim = Text(Point(645,250),"SIM")
                confirmarsim.setSize(20)
                confirmarsim.draw(win)
                confirmarnao = Text(Point(745,250),"NAO")
                confirmarnao.setSize(20)
                confirmarnao.draw(win)
                while h != 0:
                    p = win.getMouse()
                    x = p.x
                    y = p.y
                    if x>600 and x<690 and y>230 and y<270:
                        h = 0
                        escolhido = 4
                        j04pp=Image(Point(962,306),"04pp.gif")
                        j04pp.draw(win)
                        caixaconfirma.undraw()
                        caixaconfirmasim.undraw()
                        caixaconfirmanao.undraw()
                        confirmar.undraw()
                        confirmarsim.undraw()
                        confirmarnao.undraw()
                        x = 0
                        y = 0
                        j04.undraw()
                        regrasdojogo3.undraw()
                        regrasdojogo3 = Text(Point(410,7),"SELECIONE O PERSONAGEM QUE DESEJA VER MAIOR")
                        regrasdojogo3.setSize(10)
                        regrasdojogo3.draw(win)
                        caixaescolhido.undraw()
                        caixaescolhido2=Image(Point(962,306),"personagemselecionado2.gif") #Point(923,242),Point(1002,370)
                        caixaescolhido2.draw(win)

                    if x>700 and x<790 and y>230 and y<270:
                        h = 0
                        escolhido = 0
                        caixaconfirma.undraw()
                        caixaconfirmasim.undraw()
                        caixaconfirmanao.undraw()
                        confirmar.undraw()
                        confirmarsim.undraw()
                        confirmarnao.undraw()
                        x = 0
                        y = 0
                        j04.undraw()  #4
        if x>338 and x<417 and y>15 and y<145:
            j05=Image(Point(390,320),"05.gif")
            j05.draw(win)
            if escolhido != 0:
                win.getMouse()
                j05.undraw()
            if escolhido == 0:
                h = 1
                caixaconfirma = Rectangle(Point(600,180),Point(790,220))
                caixaconfirma.setFill("white")
                caixaconfirma.setOutline("blue2")
                caixaconfirma.draw(win)
                caixaconfirmasim = Rectangle(Point(600,230),Point(690,270))
                caixaconfirmasim.setFill("green2")
                caixaconfirmasim.setOutline("green2")
                caixaconfirmasim.draw(win)
                caixaconfirmanao = Rectangle(Point(700,230),Point(790,270))
                caixaconfirmanao.setFill("red2")
                caixaconfirmanao.setOutline("red2")
                caixaconfirmanao.draw(win)
                confirmar = Text(Point(700,200),"CONFIRMA?")
                confirmar.setSize(20)
                confirmar.draw(win)
                confirmarsim = Text(Point(645,250),"SIM")
                confirmarsim.setSize(20)
                confirmarsim.draw(win)
                confirmarnao = Text(Point(745,250),"NAO")
                confirmarnao.setSize(20)
                confirmarnao.draw(win)
                while h != 0:
                    p = win.getMouse()
                    x = p.x
                    y = p.y
                    if x>600 and x<690 and y>230 and y<270:
                        h = 0
                        escolhido = 5
                        j05pp=Image(Point(962,306),"05pp.gif")
                        j05pp.draw(win)
                        caixaconfirma.undraw()
                        caixaconfirmasim.undraw()
                        caixaconfirmanao.undraw()
                        confirmar.undraw()
                        confirmarsim.undraw()
                        confirmarnao.undraw()
                        x = 0
                        y = 0
                        j05.undraw()
                        regrasdojogo3.undraw()
                        regrasdojogo3 = Text(Point(410,7),"SELECIONE O PERSONAGEM QUE DESEJA VER MAIOR")
                        regrasdojogo3.setSize(10)
                        regrasdojogo3.draw(win)
                        caixaescolhido.undraw()
                        caixaescolhido2=Image(Point(962,306),"personagemselecionado2.gif") #Point(923,242),Point(1002,370)
                        caixaescolhido2.draw(win)

                    if x>700 and x<790 and y>230 and y<270:
                        h = 0
                        escolhido = 0
                        caixaconfirma.undraw()
                        caixaconfirmasim.undraw()
                        caixaconfirmanao.undraw()
                        confirmar.undraw()
                        confirmarsim.undraw()
                        confirmarnao.undraw()
                        x = 0
                        y = 0
                        j05.undraw()  #5
        if x>420 and x<500 and y>15 and y<145:
            j06=Image(Point(390,320),"06.gif")
            j06.draw(win)
            if escolhido != 0:
                win.getMouse()
                j06.undraw()
            if escolhido == 0:
                h = 1
                caixaconfirma = Rectangle(Point(600,180),Point(790,220))
                caixaconfirma.setFill("white")
                caixaconfirma.setOutline("blue2")
                caixaconfirma.draw(win)
                caixaconfirmasim = Rectangle(Point(600,230),Point(690,270))
                caixaconfirmasim.setFill("green2")
                caixaconfirmasim.setOutline("green2")
                caixaconfirmasim.draw(win)
                caixaconfirmanao = Rectangle(Point(700,230),Point(790,270))
                caixaconfirmanao.setFill("red2")
                caixaconfirmanao.setOutline("red2")
                caixaconfirmanao.draw(win)
                confirmar = Text(Point(700,200),"CONFIRMA?")
                confirmar.setSize(20)
                confirmar.draw(win)
                confirmarsim = Text(Point(645,250),"SIM")
                confirmarsim.setSize(20)
                confirmarsim.draw(win)
                confirmarnao = Text(Point(745,250),"NAO")
                confirmarnao.setSize(20)
                confirmarnao.draw(win)
                while h != 0:
                    p = win.getMouse()
                    x = p.x
                    y = p.y
                    if x>600 and x<690 and y>230 and y<270:
                        h = 0
                        escolhido = 6
                        j06pp=Image(Point(962,306),"06pp.gif")
                        j06pp.draw(win)
                        caixaconfirma.undraw()
                        caixaconfirmasim.undraw()
                        caixaconfirmanao.undraw()
                        confirmar.undraw()
                        confirmarsim.undraw()
                        confirmarnao.undraw()
                        x = 0
                        y = 0
                        j06.undraw()
                        regrasdojogo3.undraw()
                        regrasdojogo3 = Text(Point(410,7),"SELECIONE O PERSONAGEM QUE DESEJA VER MAIOR")
                        regrasdojogo3.setSize(10)
                        regrasdojogo3.draw(win)
                        caixaescolhido.undraw()
                        caixaescolhido2=Image(Point(962,306),"personagemselecionado2.gif") #Point(923,242),Point(1002,370)
                        caixaescolhido2.draw(win)

                    if x>700 and x<790 and y>230 and y<270:
                        h = 0
                        escolhido = 0
                        caixaconfirma.undraw()
                        caixaconfirmasim.undraw()
                        caixaconfirmanao.undraw()
                        confirmar.undraw()
                        confirmarsim.undraw()
                        confirmarnao.undraw()
                        x = 0
                        y = 0
                        j06.undraw()  #6
        if x>502 and x<581 and y>15 and y<145:
            j07=Image(Point(390,320),"07.gif")
            j07.draw(win)
            if escolhido != 0:
                win.getMouse()
                j07.undraw()
            if escolhido == 0:
                h = 1
                caixaconfirma = Rectangle(Point(600,180),Point(790,220))
                caixaconfirma.setFill("white")
                caixaconfirma.setOutline("blue2")
                caixaconfirma.draw(win)
                caixaconfirmasim = Rectangle(Point(600,230),Point(690,270))
                caixaconfirmasim.setFill("green2")
                caixaconfirmasim.setOutline("green2")
                caixaconfirmasim.draw(win)
                caixaconfirmanao = Rectangle(Point(700,230),Point(790,270))
                caixaconfirmanao.setFill("red2")
                caixaconfirmanao.setOutline("red2")
                caixaconfirmanao.draw(win)
                confirmar = Text(Point(700,200),"CONFIRMA?")
                confirmar.setSize(20)
                confirmar.draw(win)
                confirmarsim = Text(Point(645,250),"SIM")
                confirmarsim.setSize(20)
                confirmarsim.draw(win)
                confirmarnao = Text(Point(745,250),"NAO")
                confirmarnao.setSize(20)
                confirmarnao.draw(win)
                while h != 0:
                    p = win.getMouse()
                    x = p.x
                    y = p.y
                    if x>600 and x<690 and y>230 and y<270:
                        h = 0
                        escolhido = 7
                        j07pp=Image(Point(962,306),"07pp.gif")
                        j07pp.draw(win)
                        caixaconfirma.undraw()
                        caixaconfirmasim.undraw()
                        caixaconfirmanao.undraw()
                        confirmar.undraw()
                        confirmarsim.undraw()
                        confirmarnao.undraw()
                        x = 0
                        y = 0
                        j07.undraw()
                        regrasdojogo3.undraw()
                        regrasdojogo3 = Text(Point(410,7),"SELECIONE O PERSONAGEM QUE DESEJA VER MAIOR")
                        regrasdojogo3.setSize(10)
                        regrasdojogo3.draw(win)
                        caixaescolhido.undraw()
                        caixaescolhido2=Image(Point(962,306),"personagemselecionado2.gif") #Point(923,242),Point(1002,370)
                        caixaescolhido2.draw(win)

                    if x>700 and x<790 and y>230 and y<270:
                        h = 0
                        escolhido = 0
                        caixaconfirma.undraw()
                        caixaconfirmasim.undraw()
                        caixaconfirmanao.undraw()
                        confirmar.undraw()
                        confirmarsim.undraw()
                        confirmarnao.undraw()
                        x = 0
                        y = 0
                        j07.undraw()  #7
        if x>584 and x<663 and y>15 and y<145:
            j08=Image(Point(390,320),"08.gif")
            j08.draw(win)
            if escolhido != 0:
                win.getMouse()
                j08.undraw()
            if escolhido == 0:
                h = 1
                caixaconfirma = Rectangle(Point(600,180),Point(790,220))
                caixaconfirma.setFill("white")
                caixaconfirma.setOutline("blue2")
                caixaconfirma.draw(win)
                caixaconfirmasim = Rectangle(Point(600,230),Point(690,270))
                caixaconfirmasim.setFill("green2")
                caixaconfirmasim.setOutline("green2")
                caixaconfirmasim.draw(win)
                caixaconfirmanao = Rectangle(Point(700,230),Point(790,270))
                caixaconfirmanao.setFill("red2")
                caixaconfirmanao.setOutline("red2")
                caixaconfirmanao.draw(win)
                confirmar = Text(Point(700,200),"CONFIRMA?")
                confirmar.setSize(20)
                confirmar.draw(win)
                confirmarsim = Text(Point(645,250),"SIM")
                confirmarsim.setSize(20)
                confirmarsim.draw(win)
                confirmarnao = Text(Point(745,250),"NAO")
                confirmarnao.setSize(20)
                confirmarnao.draw(win)
                while h != 0:
                    p = win.getMouse()
                    x = p.x
                    y = p.y
                    if x>600 and x<690 and y>230 and y<270:
                        h = 0
                        escolhido = 8
                        j08pp=Image(Point(962,306),"08pp.gif")
                        j08pp.draw(win)
                        caixaconfirma.undraw()
                        caixaconfirmasim.undraw()
                        caixaconfirmanao.undraw()
                        confirmar.undraw()
                        confirmarsim.undraw()
                        confirmarnao.undraw()
                        x = 0
                        y = 0
                        j08.undraw()
                        regrasdojogo3.undraw()
                        regrasdojogo3 = Text(Point(410,7),"SELECIONE O PERSONAGEM QUE DESEJA VER MAIOR")
                        regrasdojogo3.setSize(10)
                        regrasdojogo3.draw(win)
                        caixaescolhido.undraw()
                        caixaescolhido2=Image(Point(962,306),"personagemselecionado2.gif") #Point(923,242),Point(1002,370)
                        caixaescolhido2.draw(win)

                    if x>700 and x<790 and y>230 and y<270:
                        h = 0
                        escolhido = 0
                        caixaconfirma.undraw()
                        caixaconfirmasim.undraw()
                        caixaconfirmanao.undraw()
                        confirmar.undraw()
                        confirmarsim.undraw()
                        confirmarnao.undraw()
                        x = 0
                        y = 0
                        j08.undraw()  #8
        if x>667 and x<745 and y>15 and y<145:
            j09=Image(Point(390,320),"09.gif")
            j09.draw(win)
            if escolhido != 0:
                win.getMouse()
                j09.undraw()
            if escolhido == 0:
                h = 1
                caixaconfirma = Rectangle(Point(600,180),Point(790,220))
                caixaconfirma.setFill("white")
                caixaconfirma.setOutline("blue2")
                caixaconfirma.draw(win)
                caixaconfirmasim = Rectangle(Point(600,230),Point(690,270))
                caixaconfirmasim.setFill("green2")
                caixaconfirmasim.setOutline("green2")
                caixaconfirmasim.draw(win)
                caixaconfirmanao = Rectangle(Point(700,230),Point(790,270))
                caixaconfirmanao.setFill("red2")
                caixaconfirmanao.setOutline("red2")
                caixaconfirmanao.draw(win)
                confirmar = Text(Point(700,200),"CONFIRMA?")
                confirmar.setSize(20)
                confirmar.draw(win)
                confirmarsim = Text(Point(645,250),"SIM")
                confirmarsim.setSize(20)
                confirmarsim.draw(win)
                confirmarnao = Text(Point(745,250),"NAO")
                confirmarnao.setSize(20)
                confirmarnao.draw(win)
                while h != 0:
                    p = win.getMouse()
                    x = p.x
                    y = p.y
                    if x>600 and x<690 and y>230 and y<270:
                        h = 0
                        escolhido = 9
                        j09pp=Image(Point(962,306),"09pp.gif")
                        j09pp.draw(win)
                        caixaconfirma.undraw()
                        caixaconfirmasim.undraw()
                        caixaconfirmanao.undraw()
                        confirmar.undraw()
                        confirmarsim.undraw()
                        confirmarnao.undraw()
                        x = 0
                        y = 0
                        j09.undraw()
                        regrasdojogo3.undraw()
                        regrasdojogo3 = Text(Point(410,7),"SELECIONE O PERSONAGEM QUE DESEJA VER MAIOR")
                        regrasdojogo3.setSize(10)
                        regrasdojogo3.draw(win)
                        caixaescolhido.undraw()
                        caixaescolhido2=Image(Point(962,306),"personagemselecionado2.gif") #Point(923,242),Point(1002,370)
                        caixaescolhido2.draw(win)

                    if x>700 and x<790 and y>230 and y<270:
                        h = 0
                        escolhido = 0
                        caixaconfirma.undraw()
                        caixaconfirmasim.undraw()
                        caixaconfirmanao.undraw()
                        confirmar.undraw()
                        confirmarsim.undraw()
                        confirmarnao.undraw()
                        x = 0
                        y = 0
                        j09.undraw()  #9
        if x>749 and x<827 and y>15 and y<145:
            j10=Image(Point(390,320),"10.gif")
            j10.draw(win)
            if escolhido != 0:
                win.getMouse()
                j10.undraw()
            if escolhido == 0:
                h = 1
                caixaconfirma = Rectangle(Point(600,180),Point(790,220))
                caixaconfirma.setFill("white")
                caixaconfirma.setOutline("blue2")
                caixaconfirma.draw(win)
                caixaconfirmasim = Rectangle(Point(600,230),Point(690,270))
                caixaconfirmasim.setFill("green2")
                caixaconfirmasim.setOutline("green2")
                caixaconfirmasim.draw(win)
                caixaconfirmanao = Rectangle(Point(700,230),Point(790,270))
                caixaconfirmanao.setFill("red2")
                caixaconfirmanao.setOutline("red2")
                caixaconfirmanao.draw(win)
                confirmar = Text(Point(700,200),"CONFIRMA?")
                confirmar.setSize(20)
                confirmar.draw(win)
                confirmarsim = Text(Point(645,250),"SIM")
                confirmarsim.setSize(20)
                confirmarsim.draw(win)
                confirmarnao = Text(Point(745,250),"NAO")
                confirmarnao.setSize(20)
                confirmarnao.draw(win)
                while h != 0:
                    p = win.getMouse()
                    x = p.x
                    y = p.y
                    if x>600 and x<690 and y>230 and y<270:
                        h = 0
                        escolhido = 10
                        j10pp=Image(Point(962,306),"10pp.gif")
                        j10pp.draw(win)
                        caixaconfirma.undraw()
                        caixaconfirmasim.undraw()
                        caixaconfirmanao.undraw()
                        confirmar.undraw()
                        confirmarsim.undraw()
                        confirmarnao.undraw()
                        x = 0
                        y = 0
                        j10.undraw()
                        regrasdojogo3.undraw()
                        regrasdojogo3 = Text(Point(410,7),"SELECIONE O PERSONAGEM QUE DESEJA VER MAIOR")
                        regrasdojogo3.setSize(10)
                        regrasdojogo3.draw(win)
                        caixaescolhido.undraw()
                        caixaescolhido2=Image(Point(962,306),"personagemselecionado2.gif") #Point(923,242),Point(1002,370)
                        caixaescolhido2.draw(win)

                    if x>700 and x<790 and y>230 and y<270:
                        h = 0
                        escolhido = 0
                        caixaconfirma.undraw()
                        caixaconfirmasim.undraw()
                        caixaconfirmanao.undraw()
                        confirmar.undraw()
                        confirmarsim.undraw()
                        confirmarnao.undraw()
                        x = 0
                        y = 0
                        j10.undraw()  #10
        if x>10 and x<89 and y>147 and y<276:
            j11=Image(Point(390,320),"11.gif")
            j11.draw(win)
            if escolhido != 0:
                win.getMouse()
                j11.undraw()
            if escolhido == 0:
                h = 1
                caixaconfirma = Rectangle(Point(600,180),Point(790,220))
                caixaconfirma.setFill("white")
                caixaconfirma.setOutline("blue2")
                caixaconfirma.draw(win)
                caixaconfirmasim = Rectangle(Point(600,230),Point(690,270))
                caixaconfirmasim.setFill("green2")
                caixaconfirmasim.setOutline("green2")
                caixaconfirmasim.draw(win)
                caixaconfirmanao = Rectangle(Point(700,230),Point(790,270))
                caixaconfirmanao.setFill("red2")
                caixaconfirmanao.setOutline("red2")
                caixaconfirmanao.draw(win)
                confirmar = Text(Point(700,200),"CONFIRMA?")
                confirmar.setSize(20)
                confirmar.draw(win)
                confirmarsim = Text(Point(645,250),"SIM")
                confirmarsim.setSize(20)
                confirmarsim.draw(win)
                confirmarnao = Text(Point(745,250),"NAO")
                confirmarnao.setSize(20)
                confirmarnao.draw(win)
                while h != 0:
                    p = win.getMouse()
                    x = p.x
                    y = p.y
                    if x>600 and x<690 and y>230 and y<270:
                        h = 0
                        escolhido = 11
                        j11pp=Image(Point(962,306),"11pp.gif")
                        j11pp.draw(win)
                        caixaconfirma.undraw()
                        caixaconfirmasim.undraw()
                        caixaconfirmanao.undraw()
                        confirmar.undraw()
                        confirmarsim.undraw()
                        confirmarnao.undraw()
                        x = 0
                        y = 0
                        j11.undraw()
                        regrasdojogo3.undraw()
                        regrasdojogo3 = Text(Point(410,7),"SELECIONE O PERSONAGEM QUE DESEJA VER MAIOR")
                        regrasdojogo3.setSize(10)
                        regrasdojogo3.draw(win)
                        caixaescolhido.undraw()
                        caixaescolhido2=Image(Point(962,306),"personagemselecionado2.gif") #Point(923,242),Point(1002,370)
                        caixaescolhido2.draw(win)

                    if x>700 and x<790 and y>230 and y<270:
                        h = 0
                        escolhido = 0
                        caixaconfirma.undraw()
                        caixaconfirmasim.undraw()
                        caixaconfirmanao.undraw()
                        confirmar.undraw()
                        confirmarsim.undraw()
                        confirmarnao.undraw()
                        x = 0
                        y = 0
                        j11.undraw()   #11
        if x>91 and x<171 and y>147 and y<276:
            j12=Image(Point(390,320),"12.gif")
            j12.draw(win)
            if escolhido != 0:
                win.getMouse()
                j12.undraw()
            if escolhido == 0:
                h = 1
                caixaconfirma = Rectangle(Point(600,180),Point(790,220))
                caixaconfirma.setFill("white")
                caixaconfirma.setOutline("blue2")
                caixaconfirma.draw(win)
                caixaconfirmasim = Rectangle(Point(600,230),Point(690,270))
                caixaconfirmasim.setFill("green2")
                caixaconfirmasim.setOutline("green2")
                caixaconfirmasim.draw(win)
                caixaconfirmanao = Rectangle(Point(700,230),Point(790,270))
                caixaconfirmanao.setFill("red2")
                caixaconfirmanao.setOutline("red2")
                caixaconfirmanao.draw(win)
                confirmar = Text(Point(700,200),"CONFIRMA?")
                confirmar.setSize(20)
                confirmar.draw(win)
                confirmarsim = Text(Point(645,250),"SIM")
                confirmarsim.setSize(20)
                confirmarsim.draw(win)
                confirmarnao = Text(Point(745,250),"NAO")
                confirmarnao.setSize(20)
                confirmarnao.draw(win)
                while h != 0:
                    p = win.getMouse()
                    x = p.x
                    y = p.y
                    if x>600 and x<690 and y>230 and y<270:
                        h = 0
                        escolhido = 12
                        j12pp=Image(Point(962,306),"12pp.gif")
                        j12pp.draw(win)
                        caixaconfirma.undraw()
                        caixaconfirmasim.undraw()
                        caixaconfirmanao.undraw()
                        confirmar.undraw()
                        confirmarsim.undraw()
                        confirmarnao.undraw()
                        x = 0
                        y = 0
                        j12.undraw()
                        regrasdojogo3.undraw()
                        regrasdojogo3 = Text(Point(410,7),"SELECIONE O PERSONAGEM QUE DESEJA VER MAIOR")
                        regrasdojogo3.setSize(10)
                        regrasdojogo3.draw(win)
                        caixaescolhido.undraw()
                        caixaescolhido2=Image(Point(962,306),"personagemselecionado2.gif") #Point(923,242),Point(1002,370)
                        caixaescolhido2.draw(win)

                    if x>700 and x<790 and y>230 and y<270:
                        h = 0
                        escolhido = 0
                        caixaconfirma.undraw()
                        caixaconfirmasim.undraw()
                        caixaconfirmanao.undraw()
                        confirmar.undraw()
                        confirmarsim.undraw()
                        confirmarnao.undraw()
                        x = 0
                        y = 0
                        j12.undraw()  #12
        if x>173 and x<253 and y>147 and y<276:
            j13=Image(Point(390,320),"13.gif")
            j13.draw(win)
            if escolhido != 0:
                win.getMouse()
                j13.undraw()
            if escolhido == 0:
                h = 1
                caixaconfirma = Rectangle(Point(600,180),Point(790,220))
                caixaconfirma.setFill("white")
                caixaconfirma.setOutline("blue2")
                caixaconfirma.draw(win)
                caixaconfirmasim = Rectangle(Point(600,230),Point(690,270))
                caixaconfirmasim.setFill("green2")
                caixaconfirmasim.setOutline("green2")
                caixaconfirmasim.draw(win)
                caixaconfirmanao = Rectangle(Point(700,230),Point(790,270))
                caixaconfirmanao.setFill("red2")
                caixaconfirmanao.setOutline("red2")
                caixaconfirmanao.draw(win)
                confirmar = Text(Point(700,200),"CONFIRMA?")
                confirmar.setSize(20)
                confirmar.draw(win)
                confirmarsim = Text(Point(645,250),"SIM")
                confirmarsim.setSize(20)
                confirmarsim.draw(win)
                confirmarnao = Text(Point(745,250),"NAO")
                confirmarnao.setSize(20)
                confirmarnao.draw(win)
                while h != 0:
                    p = win.getMouse()
                    x = p.x
                    y = p.y
                    if x>600 and x<690 and y>230 and y<270:
                        h = 0
                        escolhido = 13
                        j13pp=Image(Point(962,306),"13pp.gif")
                        j13pp.draw(win)
                        caixaconfirma.undraw()
                        caixaconfirmasim.undraw()
                        caixaconfirmanao.undraw()
                        confirmar.undraw()
                        confirmarsim.undraw()
                        confirmarnao.undraw()
                        x = 0
                        y = 0
                        j13.undraw()
                        regrasdojogo3.undraw()
                        regrasdojogo3 = Text(Point(410,7),"SELECIONE O PERSONAGEM QUE DESEJA VER MAIOR")
                        regrasdojogo3.setSize(10)
                        regrasdojogo3.draw(win)
                        caixaescolhido.undraw()
                        caixaescolhido2=Image(Point(962,306),"personagemselecionado2.gif") #Point(923,242),Point(1002,370)
                        caixaescolhido2.draw(win)

                    if x>700 and x<790 and y>230 and y<270:
                        h = 0
                        escolhido = 0
                        caixaconfirma.undraw()
                        caixaconfirmasim.undraw()
                        caixaconfirmanao.undraw()
                        confirmar.undraw()
                        confirmarsim.undraw()
                        confirmarnao.undraw()
                        x = 0
                        y = 0
                        j13.undraw() #13
        if x>257 and x<335 and y>147 and y<276:
            j14=Image(Point(390,320),"14.gif")
            j14.draw(win)
            if escolhido != 0:
                win.getMouse()
                j14.undraw()
            if escolhido == 0:
                h = 1
                caixaconfirma = Rectangle(Point(600,180),Point(790,220))
                caixaconfirma.setFill("white")
                caixaconfirma.setOutline("blue2")
                caixaconfirma.draw(win)
                caixaconfirmasim = Rectangle(Point(600,230),Point(690,270))
                caixaconfirmasim.setFill("green2")
                caixaconfirmasim.setOutline("green2")
                caixaconfirmasim.draw(win)
                caixaconfirmanao = Rectangle(Point(700,230),Point(790,270))
                caixaconfirmanao.setFill("red2")
                caixaconfirmanao.setOutline("red2")
                caixaconfirmanao.draw(win)
                confirmar = Text(Point(700,200),"CONFIRMA?")
                confirmar.setSize(20)
                confirmar.draw(win)
                confirmarsim = Text(Point(645,250),"SIM")
                confirmarsim.setSize(20)
                confirmarsim.draw(win)
                confirmarnao = Text(Point(745,250),"NAO")
                confirmarnao.setSize(20)
                confirmarnao.draw(win)
                while h != 0:
                    p = win.getMouse()
                    x = p.x
                    y = p.y
                    if x>600 and x<690 and y>230 and y<270:
                        h = 0
                        escolhido = 14
                        j14pp=Image(Point(962,306),"14pp.gif")
                        j14pp.draw(win)
                        caixaconfirma.undraw()
                        caixaconfirmasim.undraw()
                        caixaconfirmanao.undraw()
                        confirmar.undraw()
                        confirmarsim.undraw()
                        confirmarnao.undraw()
                        x = 0
                        y = 0
                        j14.undraw()
                        regrasdojogo3.undraw()
                        regrasdojogo3 = Text(Point(410,7),"SELECIONE O PERSONAGEM QUE DESEJA VER MAIOR")
                        regrasdojogo3.setSize(10)
                        regrasdojogo3.draw(win)
                        caixaescolhido.undraw()
                        caixaescolhido2=Image(Point(962,306),"personagemselecionado2.gif") #Point(923,242),Point(1002,370)
                        caixaescolhido2.draw(win)

                    if x>700 and x<790 and y>230 and y<270:
                        h = 0
                        escolhido = 0
                        caixaconfirma.undraw()
                        caixaconfirmasim.undraw()
                        caixaconfirmanao.undraw()
                        confirmar.undraw()
                        confirmarsim.undraw()
                        confirmarnao.undraw()
                        x = 0
                        y = 0
                        j14.undraw() #14
        if x>338 and x<417 and y>147 and y<276:
            j15=Image(Point(390,320),"15.gif")
            j15.draw(win)
            if escolhido != 0:
                win.getMouse()
                j15.undraw()
            if escolhido == 0:
                h = 1
                caixaconfirma = Rectangle(Point(600,180),Point(790,220))
                caixaconfirma.setFill("white")
                caixaconfirma.setOutline("blue2")
                caixaconfirma.draw(win)
                caixaconfirmasim = Rectangle(Point(600,230),Point(690,270))
                caixaconfirmasim.setFill("green2")
                caixaconfirmasim.setOutline("green2")
                caixaconfirmasim.draw(win)
                caixaconfirmanao = Rectangle(Point(700,230),Point(790,270))
                caixaconfirmanao.setFill("red2")
                caixaconfirmanao.setOutline("red2")
                caixaconfirmanao.draw(win)
                confirmar = Text(Point(700,200),"CONFIRMA?")
                confirmar.setSize(20)
                confirmar.draw(win)
                confirmarsim = Text(Point(645,250),"SIM")
                confirmarsim.setSize(20)
                confirmarsim.draw(win)
                confirmarnao = Text(Point(745,250),"NAO")
                confirmarnao.setSize(20)
                confirmarnao.draw(win)
                while h != 0:
                    p = win.getMouse()
                    x = p.x
                    y = p.y
                    if x>600 and x<690 and y>230 and y<270:
                        h = 0
                        escolhido = 15
                        j15pp=Image(Point(962,306),"15pp.gif")
                        j15pp.draw(win)
                        caixaconfirma.undraw()
                        caixaconfirmasim.undraw()
                        caixaconfirmanao.undraw()
                        confirmar.undraw()
                        confirmarsim.undraw()
                        confirmarnao.undraw()
                        x = 0
                        y = 0
                        j15.undraw()
                        regrasdojogo3.undraw()
                        regrasdojogo3 = Text(Point(410,7),"SELECIONE O PERSONAGEM QUE DESEJA VER MAIOR")
                        regrasdojogo3.setSize(10)
                        regrasdojogo3.draw(win)
                        caixaescolhido.undraw()
                        caixaescolhido2=Image(Point(962,306),"personagemselecionado2.gif") #Point(923,242),Point(1002,370)
                        caixaescolhido2.draw(win)

                    if x>700 and x<790 and y>230 and y<270:
                        h = 0
                        escolhido = 0
                        caixaconfirma.undraw()
                        caixaconfirmasim.undraw()
                        caixaconfirmanao.undraw()
                        confirmar.undraw()
                        confirmarsim.undraw()
                        confirmarnao.undraw()
                        x = 0
                        y = 0
                        j15.undraw() #15
        if x>420 and x<500 and y>147 and y<276:
            j16=Image(Point(390,320),"16.gif")
            j16.draw(win)
            if escolhido != 0:
                win.getMouse()
                j16.undraw()
            if escolhido == 0:
                h = 1
                caixaconfirma = Rectangle(Point(600,180),Point(790,220))
                caixaconfirma.setFill("white")
                caixaconfirma.setOutline("blue2")
                caixaconfirma.draw(win)
                caixaconfirmasim = Rectangle(Point(600,230),Point(690,270))
                caixaconfirmasim.setFill("green2")
                caixaconfirmasim.setOutline("green2")
                caixaconfirmasim.draw(win)
                caixaconfirmanao = Rectangle(Point(700,230),Point(790,270))
                caixaconfirmanao.setFill("red2")
                caixaconfirmanao.setOutline("red2")
                caixaconfirmanao.draw(win)
                confirmar = Text(Point(700,200),"CONFIRMA?")
                confirmar.setSize(20)
                confirmar.draw(win)
                confirmarsim = Text(Point(645,250),"SIM")
                confirmarsim.setSize(20)
                confirmarsim.draw(win)
                confirmarnao = Text(Point(745,250),"NAO")
                confirmarnao.setSize(20)
                confirmarnao.draw(win)
                while h != 0:
                    p = win.getMouse()
                    x = p.x
                    y = p.y
                    if x>600 and x<690 and y>230 and y<270:
                        h = 0
                        escolhido = 16
                        j16pp=Image(Point(962,306),"16pp.gif")
                        j16pp.draw(win)
                        caixaconfirma.undraw()
                        caixaconfirmasim.undraw()
                        caixaconfirmanao.undraw()
                        confirmar.undraw()
                        confirmarsim.undraw()
                        confirmarnao.undraw()
                        x = 0
                        y = 0
                        j16.undraw()
                        regrasdojogo3.undraw()
                        regrasdojogo3 = Text(Point(410,7),"SELECIONE O PERSONAGEM QUE DESEJA VER MAIOR")
                        regrasdojogo3.setSize(10)
                        regrasdojogo3.draw(win)
                        caixaescolhido.undraw()
                        caixaescolhido2=Image(Point(962,306),"personagemselecionado2.gif") #Point(923,242),Point(1002,370)
                        caixaescolhido2.draw(win)

                    if x>700 and x<790 and y>230 and y<270:
                        h = 0
                        escolhido = 0
                        caixaconfirma.undraw()
                        caixaconfirmasim.undraw()
                        caixaconfirmanao.undraw()
                        confirmar.undraw()
                        confirmarsim.undraw()
                        confirmarnao.undraw()
                        x = 0
                        y = 0
                        j16.undraw() #16
        if x>502 and x<581 and y>147 and y<276:
            j17=Image(Point(390,320),"17.gif")
            j17.draw(win)
            if escolhido != 0:
                win.getMouse()
                j17.undraw()
            if escolhido == 0:
                h = 1
                caixaconfirma = Rectangle(Point(600,180),Point(790,220))
                caixaconfirma.setFill("white")
                caixaconfirma.setOutline("blue2")
                caixaconfirma.draw(win)
                caixaconfirmasim = Rectangle(Point(600,230),Point(690,270))
                caixaconfirmasim.setFill("green2")
                caixaconfirmasim.setOutline("green2")
                caixaconfirmasim.draw(win)
                caixaconfirmanao = Rectangle(Point(700,230),Point(790,270))
                caixaconfirmanao.setFill("red2")
                caixaconfirmanao.setOutline("red2")
                caixaconfirmanao.draw(win)
                confirmar = Text(Point(700,200),"CONFIRMA?")
                confirmar.setSize(20)
                confirmar.draw(win)
                confirmarsim = Text(Point(645,250),"SIM")
                confirmarsim.setSize(20)
                confirmarsim.draw(win)
                confirmarnao = Text(Point(745,250),"NAO")
                confirmarnao.setSize(20)
                confirmarnao.draw(win)
                while h != 0:
                    p = win.getMouse()
                    x = p.x
                    y = p.y
                    if x>600 and x<690 and y>230 and y<270:
                        h = 0
                        escolhido = 17
                        j17pp=Image(Point(962,306),"17pp.gif")
                        j17pp.draw(win)
                        caixaconfirma.undraw()
                        caixaconfirmasim.undraw()
                        caixaconfirmanao.undraw()
                        confirmar.undraw()
                        confirmarsim.undraw()
                        confirmarnao.undraw()
                        x = 0
                        y = 0
                        j17.undraw()
                        regrasdojogo3.undraw()
                        regrasdojogo3 = Text(Point(410,7),"SELECIONE O PERSONAGEM QUE DESEJA VER MAIOR")
                        regrasdojogo3.setSize(10)
                        regrasdojogo3.draw(win)
                        caixaescolhido.undraw()
                        caixaescolhido2=Image(Point(962,306),"personagemselecionado2.gif") #Point(923,242),Point(1002,370)
                        caixaescolhido2.draw(win)

                    if x>700 and x<790 and y>230 and y<270:
                        h = 0
                        escolhido = 0
                        caixaconfirma.undraw()
                        caixaconfirmasim.undraw()
                        caixaconfirmanao.undraw()
                        confirmar.undraw()
                        confirmarsim.undraw()
                        confirmarnao.undraw()
                        x = 0
                        y = 0
                        j17.undraw() #17
        if x>584 and x<663 and y>147 and y<276:
            j18=Image(Point(390,320),"18.gif")
            j18.draw(win)
            if escolhido != 0:
                win.getMouse()
                j18.undraw()
            if escolhido == 0:
                h = 1
                caixaconfirma = Rectangle(Point(600,180),Point(790,220))
                caixaconfirma.setFill("white")
                caixaconfirma.setOutline("blue2")
                caixaconfirma.draw(win)
                caixaconfirmasim = Rectangle(Point(600,230),Point(690,270))
                caixaconfirmasim.setFill("green2")
                caixaconfirmasim.setOutline("green2")
                caixaconfirmasim.draw(win)
                caixaconfirmanao = Rectangle(Point(700,230),Point(790,270))
                caixaconfirmanao.setFill("red2")
                caixaconfirmanao.setOutline("red2")
                caixaconfirmanao.draw(win)
                confirmar = Text(Point(700,200),"CONFIRMA?")
                confirmar.setSize(20)
                confirmar.draw(win)
                confirmarsim = Text(Point(645,250),"SIM")
                confirmarsim.setSize(20)
                confirmarsim.draw(win)
                confirmarnao = Text(Point(745,250),"NAO")
                confirmarnao.setSize(20)
                confirmarnao.draw(win)
                while h != 0:
                    p = win.getMouse()
                    x = p.x
                    y = p.y
                    if x>600 and x<690 and y>230 and y<270:
                        h = 0
                        escolhido = 18
                        j18pp=Image(Point(962,306),"18pp.gif")
                        j18pp.draw(win)
                        caixaconfirma.undraw()
                        caixaconfirmasim.undraw()
                        caixaconfirmanao.undraw()
                        confirmar.undraw()
                        confirmarsim.undraw()
                        confirmarnao.undraw()
                        x = 0
                        y = 0
                        j18.undraw()
                        regrasdojogo3.undraw()
                        regrasdojogo3 = Text(Point(410,7),"SELECIONE O PERSONAGEM QUE DESEJA VER MAIOR")
                        regrasdojogo3.setSize(10)
                        regrasdojogo3.draw(win)
                        caixaescolhido.undraw()
                        caixaescolhido2=Image(Point(962,306),"personagemselecionado2.gif") #Point(923,242),Point(1002,370)
                        caixaescolhido2.draw(win)

                    if x>700 and x<790 and y>230 and y<270:
                        h = 0
                        escolhido = 0
                        caixaconfirma.undraw()
                        caixaconfirmasim.undraw()
                        caixaconfirmanao.undraw()
                        confirmar.undraw()
                        confirmarsim.undraw()
                        confirmarnao.undraw()
                        x = 0
                        y = 0
                        j18.undraw() #18
        if x>667 and x<745 and y>147 and y<276:
            j19=Image(Point(390,320),"19.gif")
            j19.draw(win)
            if escolhido != 0:
                win.getMouse()
                j19.undraw()
            if escolhido == 0:
                h = 1
                caixaconfirma = Rectangle(Point(600,180),Point(790,220))
                caixaconfirma.setFill("white")
                caixaconfirma.setOutline("blue2")
                caixaconfirma.draw(win)
                caixaconfirmasim = Rectangle(Point(600,230),Point(690,270))
                caixaconfirmasim.setFill("green2")
                caixaconfirmasim.setOutline("green2")
                caixaconfirmasim.draw(win)
                caixaconfirmanao = Rectangle(Point(700,230),Point(790,270))
                caixaconfirmanao.setFill("red2")
                caixaconfirmanao.setOutline("red2")
                caixaconfirmanao.draw(win)
                confirmar = Text(Point(700,200),"CONFIRMA?")
                confirmar.setSize(20)
                confirmar.draw(win)
                confirmarsim = Text(Point(645,250),"SIM")
                confirmarsim.setSize(20)
                confirmarsim.draw(win)
                confirmarnao = Text(Point(745,250),"NAO")
                confirmarnao.setSize(20)
                confirmarnao.draw(win)
                while h != 0:
                    p = win.getMouse()
                    x = p.x
                    y = p.y
                    if x>600 and x<690 and y>230 and y<270:
                        h = 0
                        escolhido = 19
                        j19pp=Image(Point(962,306),"19pp.gif")
                        j19pp.draw(win)
                        caixaconfirma.undraw()
                        caixaconfirmasim.undraw()
                        caixaconfirmanao.undraw()
                        confirmar.undraw()
                        confirmarsim.undraw()
                        confirmarnao.undraw()
                        x = 0
                        y = 0
                        j19.undraw()
                        regrasdojogo3.undraw()
                        regrasdojogo3 = Text(Point(410,7),"SELECIONE O PERSONAGEM QUE DESEJA VER MAIOR")
                        regrasdojogo3.setSize(10)
                        regrasdojogo3.draw(win)
                        caixaescolhido.undraw()
                        caixaescolhido2=Image(Point(962,306),"personagemselecionado2.gif") #Point(923,242),Point(1002,370)
                        caixaescolhido2.draw(win)

                    if x>700 and x<790 and y>230 and y<270:
                        h = 0
                        escolhido = 0
                        caixaconfirma.undraw()
                        caixaconfirmasim.undraw()
                        caixaconfirmanao.undraw()
                        confirmar.undraw()
                        confirmarsim.undraw()
                        confirmarnao.undraw()
                        x = 0
                        y = 0
                        j19.undraw() #19
        if x>749 and x<827 and y>147 and y<276:
            j20=Image(Point(390,320),"20.gif")
            j20.draw(win)
            if escolhido != 0:
                win.getMouse()
                j20.undraw()
            if escolhido == 0:
                h = 1
                caixaconfirma = Rectangle(Point(600,180),Point(790,220))
                caixaconfirma.setFill("white")
                caixaconfirma.setOutline("blue2")
                caixaconfirma.draw(win)
                caixaconfirmasim = Rectangle(Point(600,230),Point(690,270))
                caixaconfirmasim.setFill("green2")
                caixaconfirmasim.setOutline("green2")
                caixaconfirmasim.draw(win)
                caixaconfirmanao = Rectangle(Point(700,230),Point(790,270))
                caixaconfirmanao.setFill("red2")
                caixaconfirmanao.setOutline("red2")
                caixaconfirmanao.draw(win)
                confirmar = Text(Point(700,200),"CONFIRMA?")
                confirmar.setSize(20)
                confirmar.draw(win)
                confirmarsim = Text(Point(645,250),"SIM")
                confirmarsim.setSize(20)
                confirmarsim.draw(win)
                confirmarnao = Text(Point(745,250),"NAO")
                confirmarnao.setSize(20)
                confirmarnao.draw(win)
                while h != 0:
                    p = win.getMouse()
                    x = p.x
                    y = p.y
                    if x>600 and x<690 and y>230 and y<270:
                        h = 0
                        escolhido = 20
                        j20pp=Image(Point(962,306),"20pp.gif")
                        j20pp.draw(win)
                        caixaconfirma.undraw()
                        caixaconfirmasim.undraw()
                        caixaconfirmanao.undraw()
                        confirmar.undraw()
                        confirmarsim.undraw()
                        confirmarnao.undraw()
                        x = 0
                        y = 0
                        j20.undraw()
                        regrasdojogo3.undraw()
                        regrasdojogo3 = Text(Point(410,7),"SELECIONE O PERSONAGEM QUE DESEJA VER MAIOR")
                        regrasdojogo3.setSize(10)
                        regrasdojogo3.draw(win)
                        caixaescolhido.undraw()
                        caixaescolhido2=Image(Point(962,306),"personagemselecionado2.gif") #Point(923,242),Point(1002,370)
                        caixaescolhido2.draw(win)

                    if x>700 and x<790 and y>230 and y<270:
                        h = 0
                        escolhido = 0
                        caixaconfirma.undraw()
                        caixaconfirmasim.undraw()
                        caixaconfirmanao.undraw()
                        confirmar.undraw()
                        confirmarsim.undraw()
                        confirmarnao.undraw()
                        x = 0
                        y = 0
                        j20.undraw() #20
        if x>10 and x<89 and y>279 and y<408:
            j21=Image(Point(390,320),"21.gif")
            j21.draw(win)
            if escolhido != 0:
                win.getMouse()
                j21.undraw()
            if escolhido == 0:
                h = 1
                caixaconfirma = Rectangle(Point(600,180),Point(790,220))
                caixaconfirma.setFill("white")
                caixaconfirma.setOutline("blue2")
                caixaconfirma.draw(win)
                caixaconfirmasim = Rectangle(Point(600,230),Point(690,270))
                caixaconfirmasim.setFill("green2")
                caixaconfirmasim.setOutline("green2")
                caixaconfirmasim.draw(win)
                caixaconfirmanao = Rectangle(Point(700,230),Point(790,270))
                caixaconfirmanao.setFill("red2")
                caixaconfirmanao.setOutline("red2")
                caixaconfirmanao.draw(win)
                confirmar = Text(Point(700,200),"CONFIRMA?")
                confirmar.setSize(20)
                confirmar.draw(win)
                confirmarsim = Text(Point(645,250),"SIM")
                confirmarsim.setSize(20)
                confirmarsim.draw(win)
                confirmarnao = Text(Point(745,250),"NAO")
                confirmarnao.setSize(20)
                confirmarnao.draw(win)
                while h != 0:
                    p = win.getMouse()
                    x = p.x
                    y = p.y
                    if x>600 and x<690 and y>230 and y<270:
                        h = 0
                        escolhido = 21
                        j21pp=Image(Point(962,306),"21pp.gif")
                        j21pp.draw(win)
                        caixaconfirma.undraw()
                        caixaconfirmasim.undraw()
                        caixaconfirmanao.undraw()
                        confirmar.undraw()
                        confirmarsim.undraw()
                        confirmarnao.undraw()
                        x = 0
                        y = 0
                        j21.undraw()
                        regrasdojogo3.undraw()
                        regrasdojogo3 = Text(Point(410,7),"SELECIONE O PERSONAGEM QUE DESEJA VER MAIOR")
                        regrasdojogo3.setSize(10)
                        regrasdojogo3.draw(win)
                        caixaescolhido.undraw()
                        caixaescolhido2=Image(Point(962,306),"personagemselecionado2.gif") #Point(923,242),Point(1002,370)
                        caixaescolhido2.draw(win)

                    if x>700 and x<790 and y>230 and y<270:
                        h = 0
                        escolhido = 0
                        caixaconfirma.undraw()
                        caixaconfirmasim.undraw()
                        caixaconfirmanao.undraw()
                        confirmar.undraw()
                        confirmarsim.undraw()
                        confirmarnao.undraw()
                        x = 0
                        y = 0
                        j21.undraw()   #21
        if x>91 and x<171 and y>279 and y<408:
            j22=Image(Point(390,320),"22.gif")
            j22.draw(win)
            if escolhido != 0:
                win.getMouse()
                j22.undraw()
            if escolhido == 0:
                h = 1
                caixaconfirma = Rectangle(Point(600,180),Point(790,220))
                caixaconfirma.setFill("white")
                caixaconfirma.setOutline("blue2")
                caixaconfirma.draw(win)
                caixaconfirmasim = Rectangle(Point(600,230),Point(690,270))
                caixaconfirmasim.setFill("green2")
                caixaconfirmasim.setOutline("green2")
                caixaconfirmasim.draw(win)
                caixaconfirmanao = Rectangle(Point(700,230),Point(790,270))
                caixaconfirmanao.setFill("red2")
                caixaconfirmanao.setOutline("red2")
                caixaconfirmanao.draw(win)
                confirmar = Text(Point(700,200),"CONFIRMA?")
                confirmar.setSize(20)
                confirmar.draw(win)
                confirmarsim = Text(Point(645,250),"SIM")
                confirmarsim.setSize(20)
                confirmarsim.draw(win)
                confirmarnao = Text(Point(745,250),"NAO")
                confirmarnao.setSize(20)
                confirmarnao.draw(win)
                while h != 0:
                    p = win.getMouse()
                    x = p.x
                    y = p.y
                    if x>600 and x<690 and y>230 and y<270:
                        h = 0
                        escolhido = 22
                        j22pp=Image(Point(962,306),"22pp.gif")
                        j22pp.draw(win)
                        caixaconfirma.undraw()
                        caixaconfirmasim.undraw()
                        caixaconfirmanao.undraw()
                        confirmar.undraw()
                        confirmarsim.undraw()
                        confirmarnao.undraw()
                        x = 0
                        y = 0
                        j22.undraw()
                        regrasdojogo3.undraw()
                        regrasdojogo3 = Text(Point(410,7),"SELECIONE O PERSONAGEM QUE DESEJA VER MAIOR")
                        regrasdojogo3.setSize(10)
                        regrasdojogo3.draw(win)
                        caixaescolhido.undraw()
                        caixaescolhido2=Image(Point(962,306),"personagemselecionado2.gif") #Point(923,242),Point(1002,370)
                        caixaescolhido2.draw(win)

                    if x>700 and x<790 and y>230 and y<270:
                        h = 0
                        escolhido = 0
                        caixaconfirma.undraw()
                        caixaconfirmasim.undraw()
                        caixaconfirmanao.undraw()
                        confirmar.undraw()
                        confirmarsim.undraw()
                        confirmarnao.undraw()
                        x = 0
                        y = 0
                        j22.undraw()  #22
        if x>173 and x<253 and y>279 and y<408:
            j23=Image(Point(390,320),"23.gif")
            j23.draw(win)
            if escolhido != 0:
                win.getMouse()
                j23.undraw()
            if escolhido == 0:
                h = 1
                caixaconfirma = Rectangle(Point(600,180),Point(790,220))
                caixaconfirma.setFill("white")
                caixaconfirma.setOutline("blue2")
                caixaconfirma.draw(win)
                caixaconfirmasim = Rectangle(Point(600,230),Point(690,270))
                caixaconfirmasim.setFill("green2")
                caixaconfirmasim.setOutline("green2")
                caixaconfirmasim.draw(win)
                caixaconfirmanao = Rectangle(Point(700,230),Point(790,270))
                caixaconfirmanao.setFill("red2")
                caixaconfirmanao.setOutline("red2")
                caixaconfirmanao.draw(win)
                confirmar = Text(Point(700,200),"CONFIRMA?")
                confirmar.setSize(20)
                confirmar.draw(win)
                confirmarsim = Text(Point(645,250),"SIM")
                confirmarsim.setSize(20)
                confirmarsim.draw(win)
                confirmarnao = Text(Point(745,250),"NAO")
                confirmarnao.setSize(20)
                confirmarnao.draw(win)
                while h != 0:
                    p = win.getMouse()
                    x = p.x
                    y = p.y
                    if x>600 and x<690 and y>230 and y<270:
                        h = 0
                        escolhido = 23
                        j23pp=Image(Point(962,306),"23pp.gif")
                        j23pp.draw(win)
                        caixaconfirma.undraw()
                        caixaconfirmasim.undraw()
                        caixaconfirmanao.undraw()
                        confirmar.undraw()
                        confirmarsim.undraw()
                        confirmarnao.undraw()
                        x = 0
                        y = 0
                        j23.undraw()
                        regrasdojogo3.undraw()
                        regrasdojogo3 = Text(Point(410,7),"SELECIONE O PERSONAGEM QUE DESEJA VER MAIOR")
                        regrasdojogo3.setSize(10)
                        regrasdojogo3.draw(win)
                        caixaescolhido.undraw()
                        caixaescolhido2=Image(Point(962,306),"personagemselecionado2.gif") #Point(923,242),Point(1002,370)
                        caixaescolhido2.draw(win)

                    if x>700 and x<790 and y>230 and y<270:
                        h = 0
                        escolhido = 0
                        caixaconfirma.undraw()
                        caixaconfirmasim.undraw()
                        caixaconfirmanao.undraw()
                        confirmar.undraw()
                        confirmarsim.undraw()
                        confirmarnao.undraw()
                        x = 0
                        y = 0
                        j23.undraw() #23
        if x>257 and x<335 and y>279 and y<408:
            j24=Image(Point(390,320),"24.gif")
            j24.draw(win)
            if escolhido != 0:
                win.getMouse()
                j24.undraw()
            if escolhido == 0:
                h = 1
                caixaconfirma = Rectangle(Point(600,180),Point(790,220))
                caixaconfirma.setFill("white")
                caixaconfirma.setOutline("blue2")
                caixaconfirma.draw(win)
                caixaconfirmasim = Rectangle(Point(600,230),Point(690,270))
                caixaconfirmasim.setFill("green2")
                caixaconfirmasim.setOutline("green2")
                caixaconfirmasim.draw(win)
                caixaconfirmanao = Rectangle(Point(700,230),Point(790,270))
                caixaconfirmanao.setFill("red2")
                caixaconfirmanao.setOutline("red2")
                caixaconfirmanao.draw(win)
                confirmar = Text(Point(700,200),"CONFIRMA?")
                confirmar.setSize(20)
                confirmar.draw(win)
                confirmarsim = Text(Point(645,250),"SIM")
                confirmarsim.setSize(20)
                confirmarsim.draw(win)
                confirmarnao = Text(Point(745,250),"NAO")
                confirmarnao.setSize(20)
                confirmarnao.draw(win)
                while h != 0:
                    p = win.getMouse()
                    x = p.x
                    y = p.y
                    if x>600 and x<690 and y>230 and y<270:
                        h = 0
                        escolhido = 24
                        j24pp=Image(Point(962,306),"24pp.gif")
                        j24pp.draw(win)
                        caixaconfirma.undraw()
                        caixaconfirmasim.undraw()
                        caixaconfirmanao.undraw()
                        confirmar.undraw()
                        confirmarsim.undraw()
                        confirmarnao.undraw()
                        x = 0
                        y = 0
                        j24.undraw()
                        regrasdojogo3.undraw()
                        regrasdojogo3 = Text(Point(410,7),"SELECIONE O PERSONAGEM QUE DESEJA VER MAIOR")
                        regrasdojogo3.setSize(10)
                        regrasdojogo3.draw(win)
                        caixaescolhido.undraw()
                        caixaescolhido2=Image(Point(962,306),"personagemselecionado2.gif") #Point(923,242),Point(1002,370)
                        caixaescolhido2.draw(win)

                    if x>700 and x<790 and y>230 and y<270:
                        h = 0
                        escolhido = 0
                        caixaconfirma.undraw()
                        caixaconfirmasim.undraw()
                        caixaconfirmanao.undraw()
                        confirmar.undraw()
                        confirmarsim.undraw()
                        confirmarnao.undraw()
                        x = 0
                        y = 0
                        j24.undraw() #24
        if x>338 and x<417 and y>279 and y<408:
            j25=Image(Point(390,320),"25.gif")
            j25.draw(win)
            if escolhido != 0:
                win.getMouse()
                j25.undraw()
            if escolhido == 0:
                h = 1
                caixaconfirma = Rectangle(Point(600,180),Point(790,220))
                caixaconfirma.setFill("white")
                caixaconfirma.setOutline("blue2")
                caixaconfirma.draw(win)
                caixaconfirmasim = Rectangle(Point(600,230),Point(690,270))
                caixaconfirmasim.setFill("green2")
                caixaconfirmasim.setOutline("green2")
                caixaconfirmasim.draw(win)
                caixaconfirmanao = Rectangle(Point(700,230),Point(790,270))
                caixaconfirmanao.setFill("red2")
                caixaconfirmanao.setOutline("red2")
                caixaconfirmanao.draw(win)
                confirmar = Text(Point(700,200),"CONFIRMA?")
                confirmar.setSize(20)
                confirmar.draw(win)
                confirmarsim = Text(Point(645,250),"SIM")
                confirmarsim.setSize(20)
                confirmarsim.draw(win)
                confirmarnao = Text(Point(745,250),"NAO")
                confirmarnao.setSize(20)
                confirmarnao.draw(win)
                while h != 0:
                    p = win.getMouse()
                    x = p.x
                    y = p.y
                    if x>600 and x<690 and y>230 and y<270:
                        h = 0
                        escolhido = 25
                        j25pp=Image(Point(962,306),"25pp.gif")
                        j25pp.draw(win)
                        caixaconfirma.undraw()
                        caixaconfirmasim.undraw()
                        caixaconfirmanao.undraw()
                        confirmar.undraw()
                        confirmarsim.undraw()
                        confirmarnao.undraw()
                        x = 0
                        y = 0
                        j25.undraw()
                        regrasdojogo3.undraw()
                        regrasdojogo3 = Text(Point(410,7),"SELECIONE O PERSONAGEM QUE DESEJA VER MAIOR")
                        regrasdojogo3.setSize(10)
                        regrasdojogo3.draw(win)
                        caixaescolhido.undraw()
                        caixaescolhido2=Image(Point(962,306),"personagemselecionado2.gif") #Point(923,242),Point(1002,370)
                        caixaescolhido2.draw(win)

                    if x>700 and x<790 and y>230 and y<270:
                        h = 0
                        escolhido = 0
                        caixaconfirma.undraw()
                        caixaconfirmasim.undraw()
                        caixaconfirmanao.undraw()
                        confirmar.undraw()
                        confirmarsim.undraw()
                        confirmarnao.undraw()
                        x = 0
                        y = 0
                        j25.undraw() #25
        if x>420 and x<500 and y>279 and y<408:
            j26=Image(Point(390,320),"26.gif")
            j26.draw(win)
            if escolhido != 0:
                win.getMouse()
                j26.undraw()
            if escolhido == 0:
                h = 1
                caixaconfirma = Rectangle(Point(600,180),Point(790,220))
                caixaconfirma.setFill("white")
                caixaconfirma.setOutline("blue2")
                caixaconfirma.draw(win)
                caixaconfirmasim = Rectangle(Point(600,230),Point(690,270))
                caixaconfirmasim.setFill("green2")
                caixaconfirmasim.setOutline("green2")
                caixaconfirmasim.draw(win)
                caixaconfirmanao = Rectangle(Point(700,230),Point(790,270))
                caixaconfirmanao.setFill("red2")
                caixaconfirmanao.setOutline("red2")
                caixaconfirmanao.draw(win)
                confirmar = Text(Point(700,200),"CONFIRMA?")
                confirmar.setSize(20)
                confirmar.draw(win)
                confirmarsim = Text(Point(645,250),"SIM")
                confirmarsim.setSize(20)
                confirmarsim.draw(win)
                confirmarnao = Text(Point(745,250),"NAO")
                confirmarnao.setSize(20)
                confirmarnao.draw(win)
                while h != 0:
                    p = win.getMouse()
                    x = p.x
                    y = p.y
                    if x>600 and x<690 and y>230 and y<270:
                        h = 0
                        escolhido = 26
                        j26pp=Image(Point(962,306),"26pp.gif")
                        j26pp.draw(win)
                        caixaconfirma.undraw()
                        caixaconfirmasim.undraw()
                        caixaconfirmanao.undraw()
                        confirmar.undraw()
                        confirmarsim.undraw()
                        confirmarnao.undraw()
                        x = 0
                        y = 0
                        j26.undraw()
                        regrasdojogo3.undraw()
                        regrasdojogo3 = Text(Point(410,7),"SELECIONE O PERSONAGEM QUE DESEJA VER MAIOR")
                        regrasdojogo3.setSize(10)
                        regrasdojogo3.draw(win)
                        caixaescolhido.undraw()
                        caixaescolhido2=Image(Point(962,306),"personagemselecionado2.gif") #Point(923,242),Point(1002,370)
                        caixaescolhido2.draw(win)

                    if x>700 and x<790 and y>230 and y<270:
                        h = 0
                        escolhido = 0
                        caixaconfirma.undraw()
                        caixaconfirmasim.undraw()
                        caixaconfirmanao.undraw()
                        confirmar.undraw()
                        confirmarsim.undraw()
                        confirmarnao.undraw()
                        x = 0
                        y = 0
                        j26.undraw() #26
        if x>502 and x<581 and y>279 and y<408:
            j27=Image(Point(390,320),"27.gif")
            j27.draw(win)
            if escolhido != 0:
                win.getMouse()
                j27.undraw()
            if escolhido == 0:
                h = 1
                caixaconfirma = Rectangle(Point(600,180),Point(790,220))
                caixaconfirma.setFill("white")
                caixaconfirma.setOutline("blue2")
                caixaconfirma.draw(win)
                caixaconfirmasim = Rectangle(Point(600,230),Point(690,270))
                caixaconfirmasim.setFill("green2")
                caixaconfirmasim.setOutline("green2")
                caixaconfirmasim.draw(win)
                caixaconfirmanao = Rectangle(Point(700,230),Point(790,270))
                caixaconfirmanao.setFill("red2")
                caixaconfirmanao.setOutline("red2")
                caixaconfirmanao.draw(win)
                confirmar = Text(Point(700,200),"CONFIRMA?")
                confirmar.setSize(20)
                confirmar.draw(win)
                confirmarsim = Text(Point(645,250),"SIM")
                confirmarsim.setSize(20)
                confirmarsim.draw(win)
                confirmarnao = Text(Point(745,250),"NAO")
                confirmarnao.setSize(20)
                confirmarnao.draw(win)
                while h != 0:
                    p = win.getMouse()
                    x = p.x
                    y = p.y
                    if x>600 and x<690 and y>230 and y<270:
                        h = 0
                        escolhido = 27
                        j27pp=Image(Point(962,306),"27pp.gif")
                        j27pp.draw(win)
                        caixaconfirma.undraw()
                        caixaconfirmasim.undraw()
                        caixaconfirmanao.undraw()
                        confirmar.undraw()
                        confirmarsim.undraw()
                        confirmarnao.undraw()
                        x = 0
                        y = 0
                        j27.undraw()
                        regrasdojogo3.undraw()
                        regrasdojogo3 = Text(Point(410,7),"SELECIONE O PERSONAGEM QUE DESEJA VER MAIOR")
                        regrasdojogo3.setSize(10)
                        regrasdojogo3.draw(win)
                        caixaescolhido.undraw()
                        caixaescolhido2=Image(Point(962,306),"personagemselecionado2.gif") #Point(923,242),Point(1002,370)
                        caixaescolhido2.draw(win)

                    if x>700 and x<790 and y>230 and y<270:
                        h = 0
                        escolhido = 0
                        caixaconfirma.undraw()
                        caixaconfirmasim.undraw()
                        caixaconfirmanao.undraw()
                        confirmar.undraw()
                        confirmarsim.undraw()
                        confirmarnao.undraw()
                        x = 0
                        y = 0
                        j27.undraw() #27
        if x>584 and x<663 and y>279 and y<408:
            j28=Image(Point(390,320),"28.gif")
            j28.draw(win)
            if escolhido != 0:
                win.getMouse()
                j28.undraw()
            if escolhido == 0:
                h = 1
                caixaconfirma = Rectangle(Point(600,180),Point(790,220))
                caixaconfirma.setFill("white")
                caixaconfirma.setOutline("blue2")
                caixaconfirma.draw(win)
                caixaconfirmasim = Rectangle(Point(600,230),Point(690,270))
                caixaconfirmasim.setFill("green2")
                caixaconfirmasim.setOutline("green2")
                caixaconfirmasim.draw(win)
                caixaconfirmanao = Rectangle(Point(700,230),Point(790,270))
                caixaconfirmanao.setFill("red2")
                caixaconfirmanao.setOutline("red2")
                caixaconfirmanao.draw(win)
                confirmar = Text(Point(700,200),"CONFIRMA?")
                confirmar.setSize(20)
                confirmar.draw(win)
                confirmarsim = Text(Point(645,250),"SIM")
                confirmarsim.setSize(20)
                confirmarsim.draw(win)
                confirmarnao = Text(Point(745,250),"NAO")
                confirmarnao.setSize(20)
                confirmarnao.draw(win)
                while h != 0:
                    p = win.getMouse()
                    x = p.x
                    y = p.y
                    if x>600 and x<690 and y>230 and y<270:
                        h = 0
                        escolhido = 28
                        j28pp=Image(Point(962,306),"28pp.gif")
                        j28pp.draw(win)
                        caixaconfirma.undraw()
                        caixaconfirmasim.undraw()
                        caixaconfirmanao.undraw()
                        confirmar.undraw()
                        confirmarsim.undraw()
                        confirmarnao.undraw()
                        x = 0
                        y = 0
                        j28.undraw()
                        regrasdojogo3.undraw()
                        regrasdojogo3 = Text(Point(410,7),"SELECIONE O PERSONAGEM QUE DESEJA VER MAIOR")
                        regrasdojogo3.setSize(10)
                        regrasdojogo3.draw(win)
                        caixaescolhido.undraw()
                        caixaescolhido2=Image(Point(962,306),"personagemselecionado2.gif") #Point(923,242),Point(1002,370)
                        caixaescolhido2.draw(win)

                    if x>700 and x<790 and y>230 and y<270:
                        h = 0
                        escolhido = 0
                        caixaconfirma.undraw()
                        caixaconfirmasim.undraw()
                        caixaconfirmanao.undraw()
                        confirmar.undraw()
                        confirmarsim.undraw()
                        confirmarnao.undraw()
                        x = 0
                        y = 0
                        j28.undraw() #28
        if x>667 and x<745 and y>279 and y<408:
            j29=Image(Point(390,320),"29.gif")
            j29.draw(win)
            if escolhido != 0:
                win.getMouse()
                j29.undraw()
            if escolhido == 0:
                h = 1
                caixaconfirma = Rectangle(Point(600,180),Point(790,220))
                caixaconfirma.setFill("white")
                caixaconfirma.setOutline("blue2")
                caixaconfirma.draw(win)
                caixaconfirmasim = Rectangle(Point(600,230),Point(690,270))
                caixaconfirmasim.setFill("green2")
                caixaconfirmasim.setOutline("green2")
                caixaconfirmasim.draw(win)
                caixaconfirmanao = Rectangle(Point(700,230),Point(790,270))
                caixaconfirmanao.setFill("red2")
                caixaconfirmanao.setOutline("red2")
                caixaconfirmanao.draw(win)
                confirmar = Text(Point(700,200),"CONFIRMA?")
                confirmar.setSize(20)
                confirmar.draw(win)
                confirmarsim = Text(Point(645,250),"SIM")
                confirmarsim.setSize(20)
                confirmarsim.draw(win)
                confirmarnao = Text(Point(745,250),"NAO")
                confirmarnao.setSize(20)
                confirmarnao.draw(win)
                while h != 0:
                    p = win.getMouse()
                    x = p.x
                    y = p.y
                    if x>600 and x<690 and y>230 and y<270:
                        h = 0
                        escolhido = 29
                        j29pp=Image(Point(962,306),"29pp.gif")
                        j29pp.draw(win)
                        caixaconfirma.undraw()
                        caixaconfirmasim.undraw()
                        caixaconfirmanao.undraw()
                        confirmar.undraw()
                        confirmarsim.undraw()
                        confirmarnao.undraw()
                        x = 0
                        y = 0
                        j29.undraw()
                        regrasdojogo3.undraw()
                        regrasdojogo3 = Text(Point(410,7),"SELECIONE O PERSONAGEM QUE DESEJA VER MAIOR")
                        regrasdojogo3.setSize(10)
                        regrasdojogo3.draw(win)
                        caixaescolhido.undraw()
                        caixaescolhido2=Image(Point(962,306),"personagemselecionado2.gif") #Point(923,242),Point(1002,370)
                        caixaescolhido2.draw(win)

                    if x>700 and x<790 and y>230 and y<270:
                        h = 0
                        escolhido = 0
                        caixaconfirma.undraw()
                        caixaconfirmasim.undraw()
                        caixaconfirmanao.undraw()
                        confirmar.undraw()
                        confirmarsim.undraw()
                        confirmarnao.undraw()
                        x = 0
                        y = 0
                        j29.undraw() #29
        if x>749 and x<827 and y>279 and y<408:
            j30=Image(Point(390,320),"30.gif")
            j30.draw(win)
            if escolhido != 0:
                win.getMouse()
                j30.undraw()
            if escolhido == 0:
                h = 1
                caixaconfirma = Rectangle(Point(600,180),Point(790,220))
                caixaconfirma.setFill("white")
                caixaconfirma.setOutline("blue2")
                caixaconfirma.draw(win)
                caixaconfirmasim = Rectangle(Point(600,230),Point(690,270))
                caixaconfirmasim.setFill("green2")
                caixaconfirmasim.setOutline("green2")
                caixaconfirmasim.draw(win)
                caixaconfirmanao = Rectangle(Point(700,230),Point(790,270))
                caixaconfirmanao.setFill("red2")
                caixaconfirmanao.setOutline("red2")
                caixaconfirmanao.draw(win)
                confirmar = Text(Point(700,200),"CONFIRMA?")
                confirmar.setSize(20)
                confirmar.draw(win)
                confirmarsim = Text(Point(645,250),"SIM")
                confirmarsim.setSize(20)
                confirmarsim.draw(win)
                confirmarnao = Text(Point(745,250),"NAO")
                confirmarnao.setSize(20)
                confirmarnao.draw(win)
                while h != 0:
                    p = win.getMouse()
                    x = p.x
                    y = p.y
                    if x>600 and x<690 and y>230 and y<270:
                        h = 0
                        escolhido = 30
                        j30pp=Image(Point(962,306),"30pp.gif")
                        j30pp.draw(win)
                        caixaconfirma.undraw()
                        caixaconfirmasim.undraw()
                        caixaconfirmanao.undraw()
                        confirmar.undraw()
                        confirmarsim.undraw()
                        confirmarnao.undraw()
                        x = 0
                        y = 0
                        j30.undraw()
                        regrasdojogo3.undraw()
                        regrasdojogo3 = Text(Point(410,7),"SELECIONE O PERSONAGEM QUE DESEJA VER MAIOR")
                        regrasdojogo3.setSize(10)
                        regrasdojogo3.draw(win)
                        caixaescolhido.undraw()
                        caixaescolhido2=Image(Point(962,306),"personagemselecionado2.gif") #Point(923,242),Point(1002,370)
                        caixaescolhido2.draw(win)

                    if x>700 and x<790 and y>230 and y<270:
                        h = 0
                        escolhido = 0
                        caixaconfirma.undraw()
                        caixaconfirmasim.undraw()
                        caixaconfirmanao.undraw()
                        confirmar.undraw()
                        confirmarsim.undraw()
                        confirmarnao.undraw()
                        x = 0
                        y = 0
                        j30.undraw() #30
        

        #Atribuições de cada escolhido para as perguntas
        if escolhido == 1:
            listapersonagem = "Cecília","cecília","Cecilia","cecilia","CECILIA","CECÍLIA",1,4,15,16,19,21
        if escolhido == 2:
            listapersonagem = "Mariana","mariana","MARIANA",3,8,9,15,17,20,21
        if escolhido == 3:
            listapersonagem = "Paula","paula","PAULA",2,8,9,15,18,20,21
        if escolhido == 4:
            listapersonagem = "Juliana","juliana","JULIANA",2,15,19,20,21
        if escolhido == 5:
            listapersonagem = "Sabrina","sabrina","SABRINA",5,15,19,20,21
        if escolhido == 6:
            listapersonagem = "Giulia","giulia","GIULIA","julia","Julia","JULIA",1,6,15,17,20,21
        if escolhido == 7:
            listapersonagem = "Fernanda","fernanda","FERNANDA",2,15,16,18,20,21
        if escolhido == 8:
            listapersonagem = "Jorge","jorge","JORGE",5,11,12,14,19
        if escolhido == 9:
            listapersonagem = "Maria Flor","Maria","Flor","maria flor","maria","flor","MARIA FLOR",3,15,18,20
        if escolhido == 10:
            listapersonagem = "Débora","Debora","débora","debora","DEBORA","DÉBORA",5,8,9,15,16,19,20,21
        if escolhido == 11:
            listapersonagem = "Odete","odete","ODETE",1,4,15,16,17,20
        if escolhido == 12:
            listapersonagem = "Alice","alice","ALICE",5,9,10,15,19,20
        if escolhido == 13:
            listapersonagem = "Gabriela","gabriela","GABRIELA",1,2,9,10,15,16,17,20,21
        if escolhido == 14:
            listapersonagem = "Olavo","olavo","OLAVO",1,3,14,18,22
        if escolhido == 15:
            listapersonagem = "Raul","raul","RAUL",1,2,8,9,14,17
        if escolhido == 16:
            listapersonagem = "Zeca","zeca","ZECA",1,3,11,12,13,14,18,21
        if escolhido == 17:
            listapersonagem = "Roberto","roberto","ROBERTO",1,2,11,12,13,14,19,20,22
        if escolhido == 18:
            listapersonagem = "João","joão","JOÃO","Joao","joao","JOAO",1,4,8,9,14,19,22
        if escolhido == 19:
            listapersonagem = "Pedro","pedro","PEDRO",1,4,11,13,14,19,22
        if escolhido == 20:
            listapersonagem = "Bernardo","bernardo","BERNARDO",2,14,19,20,22
        if escolhido == 21:
            listapersonagem = "Alberto","alberto","ALBERTO",1,2,11,12,13,14,19,22
        if escolhido == 22:
            listapersonagem = "Alfredo","alfredo","ALFREDO",5,8,9,11,12,13,14,19,20,22
        if escolhido == 23:
            listapersonagem = "Henrique","henrique","HENRIQUE",1,7,14,19
        if escolhido == 24:
            listapersonagem = "Gilberto","gilberto","GILBERTO",1,6,11,12,13,14,18,22
        if escolhido == 25:
            listapersonagem = "Patrícia","patrícia","PATRÍCIA","Patricia","patricia","PATRICIA",1,2,8,9,10,15,19,20,21
        if escolhido == 26:
            listapersonagem = "Cláudia","cláudia","CLÁUDIA","Claudia","claudia","CLAUDIA",1,2,15,16,19,20,21
        if escolhido == 27:
            listapersonagem = "Anna","anna","ANNA","Ana","ana","ANA",5,9,10,15,19,20,21
        if escolhido == 28:
            listapersonagem = "Joaquim","joaquim","JOAQUIM",7,8,9,11,13,14,19
        if escolhido == 29:
            listapersonagem = "Chico","chico","CHICO","Francisco","francisco","FRANCISCO",4,7,14,17,20,22
        if escolhido == 30:
            listapersonagem = "Samir","samir","SAMIR",2,9,10,11,12,13,14,19

        listapersonagem1 = 1,4,15,16,19,21
        listapersonagem2 = 3,8,9,15,17,20,21
        listapersonagem3 = 2,8,9,15,18,20,21
        listapersonagem4 = 2,15,19,20,21
        listapersonagem5 = 5,15,19,20,21
        listapersonagem6 = 1,6,15,17,20,21
        listapersonagem7 = 2,15,16,18,20,21
        listapersonagem8 = 5,11,12,14,19
        listapersonagem9 = 3,15,18,20
        listapersonagem10 = 5,8,9,15,16,19,20,21
        listapersonagem11 = 1,4,15,16,17,20
        listapersonagem12 = 5,9,10,15,19,20
        listapersonagem13 = 1,2,9,10,15,16,17,20,21
        listapersonagem14 = 1,3,14,18,22
        listapersonagem15 = 1,2,8,9,14,17
        listapersonagem16 = 1,3,11,12,13,14,18,21
        listapersonagem17 = 1,2,11,12,13,14,19,20,22
        listapersonagem18 = 1,4,8,9,14,19,22
        listapersonagem19 = 1,4,11,13,14,19,22
        listapersonagem20 = 2,14,19,20,22
        listapersonagem21 = 1,2,11,12,13,14,19,22
        listapersonagem22 = 5,8,9,11,12,13,14,19,20,22
        listapersonagem23 = 1,7,14,19
        listapersonagem24 = 1,6,11,12,13,14,18,22
        listapersonagem25 = 1,2,8,9,10,15,19,20,21
        listapersonagem26 = 1,2,15,16,19,20,21
        listapersonagem27 = 5,9,10,15,19,20,21
        listapersonagem28 = 7,8,9,11,13,14,19
        listapersonagem29 = 4,7,14,17,20,22
        listapersonagem30 = 2,9,10,11,12,13,14,19

        #PERGUNTAS
        
        if x>9 and x<91 and y>431 and y<523 and pergunta > 0 and escolhido != 0 and contador !=0:
            pergunta = pergunta - 1
            x = 0
            y = 0
            perguntaatual.undraw()
            perguntaatual = Text(Point(295,477),(linhas[pergunta]))
            perguntaatual.setSize(12)
            perguntaatual.draw(win) #seta esquerda
        if x>500 and x<582 and y>431 and y<523 and pergunta < 22 and escolhido != 0 and contador !=0:
            pergunta = pergunta + 1
            x = 0
            y = 0
            perguntaatual.undraw()
            perguntaatual = Text(Point(295,477),(linhas[pergunta]))
            perguntaatual.setSize(12)
            perguntaatual.draw(win) #seta direita
        if x>120 and x<471 and y>431 and y<523 and escolhido != 0 and contador !=0 and pergunta !=0: #caixa perguntas
            textocontador.undraw()
            contador = contador - 1
            textocontador = Text(Point(916,212),(contador))
            textocontador.setSize(10)
            textocontador.draw(win)
            x = 0
            y = 0
            if pergunta in listapersonagem:
                v = "SIM"
                textoresposta.undraw()
                textoresposta = Text(Point(880,478),(v))
                textoresposta.setSize(36)
                textoresposta.draw(win)
                if pergunta in listapersonagem1:
                    oi = 0
                else:
                    j01pp.undraw()
                    if per1 == 1:
                        restantes = restantes - 1
                        per1 = 0
                if pergunta in listapersonagem2:
                    oi = 0
                else:
                    j02pp.undraw()
                    if per2 == 1:
                        restantes = restantes - 1
                        per2 = 0
                if pergunta in listapersonagem3:
                    oi = 0
                else:
                    j03pp.undraw()
                    if per3 == 1:
                        restantes = restantes - 1
                        per3 = 0
                if pergunta in listapersonagem4:
                    oi = 0
                else:
                    j04pp.undraw()
                    if per4 == 1:
                        restantes = restantes - 1
                        per4 = 0
                if pergunta in listapersonagem5:
                    oi = 0
                else:
                    j05pp.undraw()
                    if per5 == 1:
                        restantes = restantes - 1
                        per5 = 0
                if pergunta in listapersonagem6:
                    oi = 0
                else:
                    j06pp.undraw()
                    if per6 == 1:
                        restantes = restantes - 1
                        per6 = 0
                if pergunta in listapersonagem7:
                    oi = 0
                else:
                    j07pp.undraw()
                    if per7 == 1:
                        restantes = restantes - 1
                        per7 = 0
                if pergunta in listapersonagem8:
                    oi = 0
                else:
                    j08pp.undraw()
                    if per8 == 1:
                        restantes = restantes - 1
                        per8 = 0
                if pergunta in listapersonagem9:
                    oi = 0
                else:
                    j09pp.undraw()
                    if per9 == 1:
                        restantes = restantes - 1
                        per9 = 0
                if pergunta in listapersonagem10:
                    oi = 0
                else:
                    j10pp.undraw()
                    if per10 == 1:
                        restantes = restantes - 1
                        per10 = 0
                if pergunta in listapersonagem11:
                    oi = 0
                else:
                    j11pp.undraw()
                    if per11 == 1:
                        restantes = restantes - 1
                        per11 = 0
                if pergunta in listapersonagem12:
                    oi = 0
                else:
                    j12pp.undraw()
                    if per12 == 1:
                        restantes = restantes - 1
                        per12 = 0
                if pergunta in listapersonagem13:
                    oi = 0
                else:
                    j13pp.undraw()
                    if per13 == 1:
                        restantes = restantes - 1
                        per13 = 0
                if pergunta in listapersonagem14:
                    oi = 0
                else:
                    j14pp.undraw()
                    if per14 == 1:
                        restantes = restantes - 1
                        per14 = 0
                if pergunta in listapersonagem15:
                    oi = 0
                else:
                    j15pp.undraw()
                    if per15 == 1:
                        restantes = restantes - 1
                        per15 = 0
                if pergunta in listapersonagem16:
                    oi = 0
                else:
                    j16pp.undraw()
                    if per16 == 1:
                        restantes = restantes - 1
                        per16 = 0
                if pergunta in listapersonagem17:
                    oi = 0
                else:
                    j17pp.undraw()
                    if per17 == 1:
                        restantes = restantes - 1
                        per17 = 0
                if pergunta in listapersonagem18:
                    oi = 0
                else:
                    j18pp.undraw()
                    if per18 == 1:
                        restantes = restantes - 1
                        per18 = 0
                if pergunta in listapersonagem19:
                    oi = 0
                else:
                    j19pp.undraw()
                    if per19 == 1:
                        restantes = restantes - 1
                        per19 = 0
                if pergunta in listapersonagem20:
                    oi = 0
                else:
                    j20pp.undraw()
                    if per20 == 1:
                        restantes = restantes - 1
                        per20 = 0
                if pergunta in listapersonagem21:
                    oi = 0
                else:
                    j21pp.undraw()
                    if per21 == 1:
                        restantes = restantes - 1
                        per21 = 0
                if pergunta in listapersonagem22:
                    oi = 0
                else:
                    j22pp.undraw()
                    if per22 == 1:
                        restantes = restantes - 1
                        per22 = 0
                if pergunta in listapersonagem23:
                    oi = 0
                else:
                    j23pp.undraw()
                    if per23 == 1:
                        restantes = restantes - 1
                        per23 = 0
                if pergunta in listapersonagem24:
                    oi = 0
                else:
                    j24pp.undraw()
                    if per24 == 1:
                        restantes = restantes - 1
                        per24 = 0
                if pergunta in listapersonagem25:
                    oi = 0
                else:
                    j25pp.undraw()
                    if per25 == 1:
                        restantes = restantes - 1
                        per25 = 0
                if pergunta in listapersonagem26:
                    oi = 0
                else:
                    j26pp.undraw()
                    if per26 == 1:
                        restantes = restantes - 1
                        per26 = 0
                if pergunta in listapersonagem27:
                    oi = 0
                else:
                    j27pp.undraw()
                    if per27 == 1:
                        restantes = restantes - 1
                        per27 = 0
                if pergunta in listapersonagem28:
                    oi = 0
                else:
                    j28pp.undraw()
                    if per28 == 1:
                        restantes = restantes - 1
                        per28 = 0
                if pergunta in listapersonagem29:
                    oi = 0
                else:
                    j29pp.undraw()
                    if per29 == 1:
                        restantes = restantes - 1
                        per29 = 0
                if pergunta in listapersonagem30:
                    oi = 0
                else:
                    j30pp.undraw()
                    if per30 == 1:
                        restantes = restantes - 1
                        per30 = 0
            else:
                v = "NÃO"
                textoresposta.undraw()
                textoresposta = Text(Point(880,478),(v))
                textoresposta.setSize(36)
                textoresposta.draw(win)
                if pergunta in listapersonagem1:
                    j01pp.undraw()
                    if per1 == 1:
                        restantes = restantes - 1
                        per1 = 0
                if pergunta in listapersonagem2:
                    j02pp.undraw()
                    if per2 == 1:
                        restantes = restantes - 1
                        per2 = 0
                if pergunta in listapersonagem3:
                    j03pp.undraw()
                    if per3 == 1:
                        restantes = restantes - 1
                        per3 = 0
                if pergunta in listapersonagem4:
                    j04pp.undraw()
                    if per4 == 1:
                        restantes = restantes - 1
                        per4 = 0
                if pergunta in listapersonagem5:
                    j05pp.undraw()
                    if per5 == 1:
                        restantes = restantes - 1
                        per5 = 0
                if pergunta in listapersonagem6:
                    j06pp.undraw()
                    if per6 == 1:
                        restantes = restantes - 1
                        per6 = 0
                if pergunta in listapersonagem7:
                    j07pp.undraw()
                    if per7 == 1:
                        restantes = restantes - 1
                        per7 = 0
                if pergunta in listapersonagem8:
                    j08pp.undraw()
                    if per8 == 1:
                        restantes = restantes - 1
                        per8 = 0
                if pergunta in listapersonagem9:
                    j09pp.undraw()
                    if per9 == 1:
                        restantes = restantes - 1
                        per9 = 0
                if pergunta in listapersonagem10:
                    j10pp.undraw()
                    if per10 == 1:
                        restantes = restantes - 1
                        per10 = 0
                if pergunta in listapersonagem11:
                    j11pp.undraw()
                    if per11 == 1:
                        restantes = restantes - 1
                        per11 = 0
                if pergunta in listapersonagem12:
                    j12pp.undraw()
                    if per12 == 1:
                        restantes = restantes - 1
                        per12 = 0
                if pergunta in listapersonagem13:
                    j13pp.undraw()
                    if per13 == 1:
                        restantes = restantes - 1
                        per13 = 0
                if pergunta in listapersonagem14:
                    j14pp.undraw()
                    if per14 == 1:
                        restantes = restantes - 1
                        per14 = 0
                if pergunta in listapersonagem15:
                    j15pp.undraw()
                    if per15 == 1:
                        restantes = restantes - 1
                        per15 = 0
                if pergunta in listapersonagem16:
                    j16pp.undraw()
                    if per16 == 1:
                        restantes = restantes - 1
                        per16 = 0
                if pergunta in listapersonagem17:
                    j17pp.undraw()
                    if per17 == 1:
                        restantes = restantes - 1
                        per17 = 0
                if pergunta in listapersonagem18:
                    j18pp.undraw()
                    if per18 == 1:
                        restantes = restantes - 1
                        per18 = 0
                if pergunta in listapersonagem19:
                    j19pp.undraw()
                    if per19 == 1:
                        restantes = restantes - 1
                        per19 = 0
                if pergunta in listapersonagem20:
                    j20pp.undraw()
                    if per20 == 1:
                        restantes = restantes - 1
                        per20 = 0
                if pergunta in listapersonagem21:
                    j21pp.undraw()
                    if per21 == 1:
                        restantes = restantes - 1
                        per21 = 0
                if pergunta in listapersonagem22:
                    j22pp.undraw()
                    if per22 == 1:
                        restantes = restantes - 1
                        per22 = 0
                if pergunta in listapersonagem23:
                    j23pp.undraw()
                    if per23 == 1:
                        restantes = restantes - 1
                        per23 = 0
                if pergunta in listapersonagem24:
                    j24pp.undraw()
                    if per24 == 1:
                        restantes = restantes - 1
                        per24 = 0
                if pergunta in listapersonagem25:
                    j25pp.undraw()
                    if per25 == 1:
                        restantes = restantes - 1
                        per25 = 0
                if pergunta in listapersonagem26:
                    j26pp.undraw()
                    if per26 == 1:
                        restantes = restantes - 1
                        per26 = 0
                if pergunta in listapersonagem27:
                    j27pp.undraw()
                    if per27 == 1:
                        restantes = restantes - 1
                        per27 = 0
                if pergunta in listapersonagem28:
                    j28pp.undraw()
                    if per28 == 1:
                        restantes = restantes - 1
                        per28 = 0
                if pergunta in listapersonagem29:
                    j29pp.undraw()
                    if per29 == 1:
                        restantes = restantes - 1
                        per29 = 0
                if pergunta in listapersonagem30:
                    j30pp.undraw()
                    if per30 == 1:
                        restantes = restantes - 1
                        per30 = 0
        
                        
        if restantes == 0:
            contador = 0
            caixamensagem.undraw()
            caixamensagem=Image(Point(875,477),"parabens.gif") #Point(747,431),Point(1002,523)
            caixamensagem.draw(win)
            caixaescolhido2.undraw()
            win.getMouse()
            win.close()
            Abertura()
        
        if restantes != 0 and contador == 0:
            camponome = Entry(Point(921,132), 10)
            camponome.setSize(20)
            camponome.setFill("white")
            camponome.draw(win)
            textoresposta.undraw()
            textoresposta = Text(Point(880,478),"DIGITE O NOME")
            textoresposta.draw(win)

            k = "a"
            while k != "Return":
                k = win.getKey()
                camponomes = camponome.getText()
            
            if camponomes in listapersonagem:
                contador = 0
                caixamensagem.undraw()
                caixamensagem=Image(Point(875,477),"parabens.gif") #Point(747,431),Point(1002,523)
                caixamensagem.draw(win)
                caixaescolhido2.undraw()
                win.getMouse()
                win.close()
                Abertura()
            
            else:
                caixamensagem.undraw()
                caixamensagem=Image(Point(875,477),"perdeu.gif") #Point(747,431),Point(1002,523)
                caixamensagem.draw(win)
                caixaescolhido2.undraw()
                win.getMouse()
                win.close()
                Abertura()

    win.getMouse()
    win.close()

def Regras():
    janelaregras=GraphWin("CARA A CARA",300,300,autoflush=False)
    janelaregras.setBackground("pink")
    fecharregras = Rectangle(Point(10,230),Point(290,280))
    fecharregras.setFill("white")
    fecharregras.setOutline("white")
    fecharregras.draw(janelaregras)
    regrasdojogo = Text(Point(150,50),"REGRAS DO JOGO")
    regrasdojogo.setSize(14)
    regrasdojogo.draw(janelaregras)
    regrasdojogo1 = Text(Point(150,100),"REGRA 1: Escolha seu personagem\n escondido do seu amigo.")
    regrasdojogo1.setSize(10)
    regrasdojogo1.draw(janelaregras)
    regrasdojogo2 = Text(Point(150,150),"REGRA 2: Peça para ele virar\n de costas enquanto você escolhe.")
    regrasdojogo2.setSize(10)
    regrasdojogo2.draw(janelaregras)
    regrasdojogo3 = Text(Point(150,200),"REGRA 3: Pode fazer até 5 perguntas\n após isso, terá que advinhar o nome.")
    regrasdojogo3.setSize(10)
    regrasdojogo3.draw(janelaregras)
    regrasdojogo4 = Text(Point(150,250),"CLIQUE AQUI PARA FECHAR")
    regrasdojogo4.setSize(14)
    regrasdojogo4.draw(janelaregras)
    regrasfechar = 1
    while regrasfechar != 0:
        t = janelaregras.getMouse()
        x = t.x
        y = t.y
        if x>10 and x<290 and y>230 and y<280:
            regrasfechar = 0
    janelaregras.close()


Abertura()