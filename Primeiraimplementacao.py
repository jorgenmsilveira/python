
"""Este programa simula um robô de serviços, num restaurante com uma mesa quadrada.
Quando o utilizador clica na área da mesa, o robô inicia o serviço, consistindo
numa ida à mesa para receber um pedido, regresso ao balcão para preparar o pedido,
entrega do pedido à mesa, e regresso ao balcão."""

from graphics import*
import time
import math
import menu

n=0

class Balcao: #Define o balcao
    def __init__(self, win, ponto1, ponto2):
        self.ponto1=ponto1
        self.ponto2=ponto2
        self.balcao=Rectangle(ponto1, ponto2)
        self.balcao.setFill('brown')
        self.balcao.draw(win)

class Mesa: #Define a mesa
    def __init__(self, win, centroMesa, raioMesa):
        self.mesa=Circle(centroMesa, raioMesa)
        self.mesa.setFill('tan')
        self.mesa.draw(win)
        self.raioMesa=raioMesa
        self.centroMesa=centroMesa

class Robot:
    def __init__(self, win, centro, raio): #Define o robot
        self.robot=Circle(centro, raio)
        self.robot.setFill('gold')
        self.robot.draw(win)
        self.raio=raio
        self.centro=centro
        
    def Move (self, win, raio, centroMesa, raioMesa): #Define o vetor de movimento (dx, dy), dividido por 1000
        self.dx= (centroMesa.getX()-self.centro.getX())/1000
        self.dy= (centroMesa.getY()-self.centro.getY()+raioMesa+15)/1000
        
        while n==0:
            self.posicao=win.getMouse() #Recebe um clique do rato
            if math.sqrt(((self.posicao.getX()-centroMesa.getX())**2)+((self.posicao.getY()-centroMesa.getY())**2))<=raioMesa: #Se o ponto em que se clicar estiver dentro da mesa, o robot exerce o movimento
                for i in range (2):
                    for i in range (1000): #Repete um movimento segundo o vetor, 1000 vezes
                        self.robot.move(self.dx, self.dy)
                        update(200)
                    time.sleep(2)
                    for i in range (1000):
                        self.robot.move(-self.dx, -self.dy)
                        update(200)
                    time.sleep(2)
            if 450<=self.posicao.getX()<=500 and 0<=self.posicao.getY()<=50: #Botao para regressar ao menu
                win.close()
                menu.menu()
                
                

class Voltar: #Define o botao
    def __init__(self, win):
        self.botao=Rectangle(Point(450, 0), Point(500, 50))
        self.botao.draw(win)
        Text(Point(475, 25), "Voltar").draw(win)


def primeira():  
    win = GraphWin("Restaurante", 750, 750)
    win.setCoords(0, 0, 500, 500)
    centroMesa= Point(200, 200)
    raioMesa=25
    balcaoObj=Balcao(win, Point(350, 440), Point(500, 500))
    mesaObj=Mesa(win, centroMesa, raioMesa)
    Voltar(win)
    robotObj=Robot(win, Point(425, 425), 10) 
    robotObj.Move(win, 12, centroMesa, raioMesa)
