"""Este programa simula um robô de serviços, num restaurante com uma mesa de forma, tamanho e posição
aleatórios. Quando o utilizador clica na área da mesa, o robô inicia o serviço para essa mesa,
consistindo numa ida à mesa para receber um pedido, regresso ao balcão para preparar o pedido,
entrega do pedido à mesa, e regresso ao balcão. O robô tem uma bateria, pelo que tem que
ir a uma Docstation carregar, quando deteta que não vai conseguir finalizar o serviço."""

from graphics import*
import random
import time
import math
import menu

n=0

class Balcao:
    def __init__(self, win, ponto1, ponto2):  #Define o balcao
        self.ponto1=ponto1
        self.ponto2=ponto2
        self.balcao=Rectangle(ponto1, ponto2)
        self.balcao.setFill('brown')
        self.balcao.draw(win)

class Mesa: 
    def __init__(self): #Define a mesa
        self.centroX=[] #Lista com as coordenadas X do centro da mesa
        self.centroY=[] #Lista com as coordenadas Y do centro da mesa
        self.semilado=[] #Lista com ao tamanho do raio/semilado da mesa
        
    def desenhar(self, win):   
        self.forma=random.randint(0,1) #Os valores 0 e 1 determinam se a mesa é circular ou retangular, respetivamente
        self.centroX.append(random.randint(30, 350)) #O X do centro varia entre 30 e 350
        self.centroY.append(random.randint(30, 350)) #O Y do centro varia entre 30 e 350
        for i in range (2):
            self.semilado.append(random.randint(18, 40)) 
        if self.forma==0: #Caso seja circular
            self.mesa=Circle(Point(self.centroX[0], self.centroY[0]), self.semilado[1])
            self.mesa.setFill('tan')
            self.mesa.draw(win)
        elif self.forma==1: #Caso seja retangular
            self.mesa=Rectangle(Point(self.centroX[0]-self.semilado[0], self.centroY[0]-self.semilado[1]),\
                                Point(self.centroX[0]+self.semilado[0], self.centroY[0]+self.semilado[1]))
            self.mesa.setFill('tan')
            self.mesa.draw(win)
 
class Robot: 
    def __init__(self, win, centro, Robotraio): #Define o robot
        self.centro=centro
        self.Robotraio=Robotraio
        self.robot=Circle(centro, Robotraio)
        self.robot.setFill('black')
        self.robot.draw(win)
        self.contador=contador=0 #Marca um contador, estabelecido a 0
        self.bateria=Circle(centro, Robotraio/3)
        self.bateria.setFill('lime green')
        self.bateria.draw(win)
        
    def Carregar(self, lc, hc, cor, contador): #Define o movimento de ir carregar (pelo x - lc, pelo y - hc)
        self.bateria.setFill(cor)
        for i in range(1000):
            self.robot.move(lc,hc)
            self.bateria.move(lc,hc)
            update(200)
            self.contador=self.contador+math.fabs(lc)+math.fabs(hc)
    
    def Servico(self, lm, hm, contador): #Define o movimento do serviço [pelo x - lm, pelo y - hm]
        for i in range(1000):
            self.robot.move(lm, hm)
            self.bateria.move(lm, hm)
            update(200)
        self.contador=self.contador+math.fabs(lm*1000)+math.fabs(hm*1000)
    
    def Deslocacao(self, Mesa): #Movimento
        if self.contador+4*(math.sqrt((self.dx*1000)**2+(self.dy*1000)**2))>=3585:
            self.Carregar(-375/1000, 0, 'red', self.contador) #Muda de cor ao ir carregar
            self.Carregar(0, 40/1000, 'red', self.contador)
            self.bateria.setFill('blue') #Muda de cor ao carregar
            self.contador=0
            time.sleep(2)
            self.Carregar(0, -40/1000, 'lime green', self.contador) #Volta à cor original
            self.Carregar(375/1000, 0, 'lime green', self.contador)  
        for i in range (2):
            self.Servico(self.dx, self.dy, self.contador)
            time.sleep(2)
            self.Servico(-self.dx, -self.dy, self.contador)
            time.sleep(2)
        
    def Move (self, win, Mesa): #Define os vetores de movimento
        mesa=Mesa
        self.dx=(mesa.centroX[0]-self.centro.getX())/1000
        self.dy=(mesa.centroY[0]-self.centro.getY()+mesa.semilado[1]+15)/1000
        
        while n==0:
            self.posicao=win.getMouse()
            if mesa.forma==1: #Caso seja retangular
               if mesa.centroX[0]-mesa.semilado[0]<=self.posicao.getX()<=mesa.centroX[0]+mesa.semilado[0] and\
                   mesa.centroY[0]-mesa.semilado[1]<=self.posicao.getY()<=mesa.centroY[0]+mesa.semilado[1]: #Percurso do robot
                    self.Deslocacao(Mesa)
            if mesa.forma==0: #Caso seja circular
                if math.sqrt((self.posicao.getX()-int(mesa.centroX[0]))**2+(self.posicao.getY()-int(mesa.centroY[0]))**2)<=int(mesa.semilado[1]):
                    self.Deslocacao(Mesa)
            if 450<=self.posicao.getX()<=500 and 0<=self.posicao.getY()<=50: #Voltar ao menu
                win.close()
                menu.menu()
                
class Docstation: 
    def __init__(self, win, vertice): #Desenhar a Docstation
        self.vertice=vertice
        self.docstation=Rectangle(Point(0,500), vertice)
        self.docstation.setFill('red')
        self.docstation.draw(win)
        Text(Point(50, 485), "Docstation").draw(win)

class Voltar: 
    def __init__(self, win): #Desenhar o botao para voltar ao menu
        self.botao=Rectangle(Point(450, 0), Point(500, 50))
        self.botao.draw(win)
        Text(Point(475, 25), "Voltar").draw(win)


def terceiraA():  
    win = GraphWin("Restaurante", 750, 750)
    win.setCoords(0, 0, 500, 500)
    balcaoObj=Balcao(win, Point(350, 440), Point(500, 500))
    docs=Docstation(win, Point(100, 450))
    mesaObj=Mesa()
    mesaObj.desenhar(win)
    Voltar(win)
    robotObj=Robot(win, Point(425, 425), 10) 
    robotObj.Move(win,mesaObj)   