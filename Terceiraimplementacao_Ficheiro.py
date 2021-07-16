"""Este programa simula um robô de serviços, num restaurante com uma mesa de forma, tamanho e posição
aleatórios. Quando o utilizador clica na área da mesa, o robô inicia o serviço para essa mesa,
consistindo numa ida à mesa para receber um pedido, regresso ao balcão para preparar o pedido,
entrega do pedido à mesa, e regresso ao balcão. O robô tem uma bateria, pelo que tem que
ir a uma Docstation carregar, quando deteta que não vai conseguir finalizar o serviço."""

from graphics import*
import math
import time
import menu

n=0

class Ficheiro:
    def __init__(self):
        self.ficheiro=open('Ambiente.txt', 'r') #Abre o ficheiro
        self.info=self.ficheiro.read() #Lê o ficheiro
        self.linhas=self.info.split('\n') #Cria uma lista que armazena as linhas do ficheiro
        self.tamanhojanela=self.linhas[1].split(' ') #Cria uma lista com os elementos da linha de índice 1
        self.coordenadasbalcao=self.linhas[3].split(' ') #Cria uma lista com os elementos da linha de índice 3
        self.palavras=[]
        self.mesac=[]
        self.mesar=[]
        for i in range(len(self.linhas)): 
            self.palavras.append(self.linhas[i-1].split(' ')) #Lista com todas as linhas, divididas pelos respetivos elementos
            if self.palavras[i-1][0]=='Circulo': 
                self.mesac.append(self.palavras[i-1][1:]) #Adiciona toda a informacao de cada mesa circular a uma lista
            if self.palavras[i][0]=='Retangulo':
                self.mesar.append(self.palavras[i][1:]) #Adiciona toda a informacao de cada mesa retangular a uma lista
        self.ficheiro.close()
            
class Mesas:
    def __init__(self):
        self.mesaX=[] #Lista (vazia) com as coordenadas X do centro de todas as mesas
        self.mesaY=[] #Lista (vazia) com as coordenadas Y do centro de todas as mesas
        self.mesaraio=[] #Lista (vazia) com o raio de todas as mesas
        self.mesa=[] #Lista (vazia) com todas as mesas  
        self.pontoX=[] #Lista (vazia) com as coordenadas X de dois vértices opostos das mesas retangulares
        self.pontoY=[] #Lista (vazia) com as coordenadas Y de dois vértices opostos das mesas retangulares
    def Mesa(self, win):
        for a in range(len(Ficheiro().mesac)): #Preenche as listas anteriores com a informação das mesas circulares
            self.mesaX.append(float(Ficheiro().mesac[a-1][0])) 
            self.mesaY.append(float(Ficheiro().mesac[a-1][1])) 
            self.mesaraio.append(float(Ficheiro().mesac[a-1][2])) 
            self.mesa.append(Circle(Point(self.mesaX[a], self.mesaY[a]), float(self.mesaraio[a])))
        for i in range(len(Ficheiro().mesar)): #Preenche as listas anteriores com a informação das mesas retangulares
            self.pontoX.append(Ficheiro().mesar[i][0])            
            self.pontoX.append(Ficheiro().mesar[i][2])
            self.pontoY.append(Ficheiro().mesar[i][1])
            self.pontoY.append(Ficheiro().mesar[i][3])
            self.mesaX.append((float(Ficheiro().mesar[i][0])+float(Ficheiro().mesar[i][2]))/2)
            self.mesaY.append((float(Ficheiro().mesar[i][1])+float(Ficheiro().mesar[i][3]))/2)
            if abs(float(Ficheiro().mesar[i][0])-float(Ficheiro().mesar[i][2]))>=abs(float(Ficheiro().mesar[i][1])-float(Ficheiro().mesar[i][3])):
                self.mesaraio.append(abs(float(Ficheiro().mesar[i][0])-float(Ficheiro().mesar[i][2]))/2)
            elif abs(float(Ficheiro().mesar[i][1])-float(Ficheiro().mesar[i][3]))>abs(float(Ficheiro().mesar[i][0])-float(Ficheiro().mesar[i][2])):
                self.mesaraio.append(abs(float(Ficheiro().mesar[i][1])-float(Ficheiro().mesar[i][3]))/2)
            self.mesa.append(Rectangle(Point(self.pontoX[2*i], self.pontoY[2*i]), Point(self.pontoX[2*i+1], self.pontoY[2*i+1])))
        for n in range(len(self.mesa)): #Desenha todas as mesas
            self.mesa[n].setFill('tan')
            self.mesa[n].draw(win)
            
class Balcao: 
    def __init__(self, win): #Define o balcao
        self.balcao=Rectangle(Point(Ficheiro().coordenadasbalcao[1], Ficheiro().coordenadasbalcao[2]),\
                              Point(Ficheiro().coordenadasbalcao[3],Ficheiro().coordenadasbalcao[4])) #Desenha o balcao a partir dos elementos da lista coordenadasbalcao
        self.balcao.setFill('brown')
        self.balcao.draw(win)
        
class Robot:  
    def __init__(self, win, centro, raio): #Define o robot
        self.centro=centro
        self.raio=raio
        self.robot=Circle(centro, raio)
        self.robot.setFill('black')
        self.robot.draw(win)
        self.contador=contador=0
        self.bateria=Circle(centro, raio/3)
        self.bateria.setFill('lime green')
        self.bateria.draw(win)

class Docstation: 
    def __init__(self, win, vertice): #Desenha a Docstation
        self.vertice=vertice
        self.docstation=Rectangle(Point(0,100), vertice)
        self.docstation.setFill('red')
        self.docstation.draw(win)
        Text(Point(10, 97), "Docstation").draw(win)

class Voltar: 
    def __init__(self, win): #Desenha o botão para regressar ao menu
        self.botao=Rectangle(Point(90, 0), Point(100, 10))
        self.botao.draw(win)
        Text(Point(95, 5), "Voltar").draw(win)
        while n==0:
            self.posicao=win.getMouse()
            if 90<=self.posicao.getX()<=100 and 0<=self.posicao.getY()<=10:
                win.close()
                menu.menu()
            
def terceiraF():
    win=GraphWin("Restaurante", Ficheiro().tamanhojanela[0], Ficheiro().tamanhojanela[1])
    win.setCoords(0, 0, 100, 100)
    docs=Docstation(win, Point(20, 90))
    Mesocas=Mesas().Mesa(win)
    ficheiro=Ficheiro()
    Balcao(win)
    centro=Point(((float(Ficheiro().coordenadasbalcao[1]) + float(Ficheiro().coordenadasbalcao[3]))/2), float(Ficheiro().coordenadasbalcao[2])-5)
    raio=2
    robot=Robot(win, centro, raio)
    Voltar(win)    