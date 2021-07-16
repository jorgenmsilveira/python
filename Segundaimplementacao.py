"""Este programa simula um robô de serviços, num restaurante com doze mesas quadradas.
Quando o utilizador clica na área de uma das mesas, o robô inicia o serviço para essa mesa,
consistindo numa ida à mesa para receber um pedido, regresso ao balcão para preparar o pedido,
entrega do pedido à mesa, e regresso ao balcão. O robô tem uma bateria, pelo que tem que ir a uma Docstation
carregar, quando deteta que não vai conseguir finalizar o serviço."""

from graphics import*
import time
import menu

n=0
semiladoMesa=25
centro=Point(425, 425)
raio=10

class Balcao: 
    def __init__(self, win, ponto1, ponto2): #Define o balcao
        self.ponto1=ponto1
        self.ponto2=ponto2
        self.balcao=Rectangle(ponto1, ponto2)
        self.balcao.setFill('brown')
        self.balcao.draw(win)
        Text(Point(425, 470), "Balcao").draw(win)

class Mesas: 
    def __init__(self, win, semiladoMesa): #Define a mesa
        self.semiladoMesa=semiladoMesa
        for a in range(4): #Colunas
            for b in range(3): #Linhas
                self.mesa=Rectangle(Point(50+a*100-semiladoMesa, 100+b*100-semiladoMesa),\
                                    Point(50+a*100+semiladoMesa, 100+b*100+semiladoMesa))
                self.mesa.setFill('tan')
                self.mesa.draw(win)

class Robot: 
    def __init__(self, win, centro, raio): #Define o robot
        self.robot=Circle(centro, raio)
        self.robot.setFill('black')
        self.robot.draw(win)
        self.raio=raio
        self.centro=centro
        self.contador=contador=0 #Marca um contador, estabelecido em 0
        self.bateria=Circle(centro, raio/5)
        self.bateria.setFill('lime green')
        self.bateria.draw(win)
        
    def Carregar(self, n, lc, hc, cor): #Define o movimento de ir carregar (pelo x - lc, pelo y - hc)
        self.bateria.setFill(cor)
        for i in range(n):
            self.robot.move(lc,hc)
            self.bateria.move(lc,hc)
            update(50)
            self.contador=self.contador+1
            print(self.contador)
    
    def Servico(self, n, lm, hm, contador): #Define o movimento do serviço [pelo x - lm, pelo y - hm]
        for i in range(n):
            self.robot.move(lm, hm)
            self.bateria.move(lm, hm)
            update(50)
            self.contador=self.contador+1
            print(self.contador)
        
    def Move(self, win, raio, semiladoMesa, centro):
        while n==0:
            self.posicao=win.getMouse()
            for a in range(4):
                for b in range(3): 
                    if 100+b*100-semiladoMesa<=self.posicao.getY()<=100+b*100+semiladoMesa and\
                    50+a*100-semiladoMesa<=self.posicao.getX()<=50+a*100+semiladoMesa: #Condicao para o clique dentro da area da janela
                        if self.contador+4*(centro.getX()-self.posicao.getX()+centro.getY()-self.posicao.getY())>=3585: #Calcula se a bateria chega para o servico
                            self.Carregar(375,-1,0, 'red')#Muda de cor ao ir carregar
                            self.Carregar(40,0,1, 'red')
                            self.bateria.setFill('blue') #Muda de cor ao carregar
                            self.contador=0
                            time.sleep(2)
                            self.Carregar(40,0,-1, 'lime green') #Volta à cor original
                            self.Carregar(375,1,0, 'lime green')                                                        
                        for i in range(2):
                            self.Servico((3-b)*100-self.raio-3, 0, -1, self.contador)
                            self.Servico(100*(4-a)-semiladoMesa, -1, 0, self.contador)
                            time.sleep(2)
                            self.Servico(100*(4-a)-semiladoMesa, 1, 0, self.contador)
                            self.Servico((3-b)*100-self.raio-3, 0, 1, self.contador)
                            time.sleep(2)
            if 450<=self.posicao.getX()<=500 and 0<=self.posicao.getY()<=50: #Botao para regressar ao menu
                win.close()
                menu.menu()

class Docstation: 
    def __init__(self, win, vertice): #Define a Docstation
        self.vertice=vertice
        self.docstation=Rectangle(Point(0,500), vertice)
        self.docstation.setFill('red')
        self.docstation.draw(win)
        Text(Point(50, 485), "Docstation").draw(win)
        
class Voltar: 
    def __init__(self, win): #Define o botao
        self.botao=Rectangle(Point(450, 0), Point(500, 50))
        self.botao.draw(win)
        Text(Point(475, 25), "Voltar").draw(win)
        
def segunda():    
    win = GraphWin("Restaurante", 750, 750)
    win.setCoords(0, 0, 500, 500)
    balcaoObj=Balcao(win, Point(350, 440), Point(500, 500))
    mesaObj=Mesas(win, semiladoMesa)
    docs=Docstation(win, Point(100, 450))
    Voltar(win)
    robotObj=Robot(win, centro, raio)
    robotObj.Move(win, raio, semiladoMesa, centro)    