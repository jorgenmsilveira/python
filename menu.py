"""Este programa gera um menu de introdução às várias implementações da simulação de um restaurante """

from graphics import *
import Primeiraimplementacao
import Segundaimplementacao
import Terceiraimplementacao_Ficheiro
import Terceiraimplementacao_Aleatorio

n=0

def menu():
    window=GraphWin("Menu", 750, 750)
    window.setCoords (0, 0, 500, 500)
    x=100
    y=71
    imp1=Rectangle(Point(x, 6*y ), Point((x+300), 5*y))
    imp2=Rectangle(Point(x, 4*y ), Point((x+300), 3*y))
    imp31=Rectangle(Point(x, 2*y ), Point((x+149), y))
    imp32=Rectangle(Point(x+151, 2*y ), Point((x+300), y))
    imp1.draw(window)
    imp2.draw(window)
    imp31.draw(window)
    imp32.draw(window)
    Text(Point(250, 475), "MENU").draw(window)
    Text(Point(250, 385), "Primeira Implementação").draw(window)
    Text(Point(250, 245), "Segunda Implementação").draw(window)
    Text(Point(175, 105), "Terceira Implementação").draw(window)
    Text(Point(175, 90), "Ficheiro").draw(window)
    Text(Point(325, 105), "Terceira Implementação").draw(window)
    Text(Point(325, 90), "Aleatorio").draw(window)
    fechar=Rectangle(Point(0, 470), Point(80, 500))
    fechar.draw(window)
    Text(Point(40, 485),"Fechar").draw(window)
    while n==0:
        clique=window.getMouse()
        if 100<=clique.getX()<=400 and 355<=clique.getY()<=426: #Primeiro botão
            window.close()
            Primeiraimplementacao.primeira()
        elif 100<=clique.getX()<=400 and 213<=clique.getY()<=284: #Segundo botão
            window.close()
            Segundaimplementacao.segunda()
        elif 100<=clique.getX()<=251 and 71<=clique.getY()<=142: #Terceiro botão
            window.close()
            Terceiraimplementacao_Ficheiro.terceiraF()
        elif 251<clique.getX()<=400 and 71<=clique.getY()<=142: #Quarto botão
            window.close()
            Terceiraimplementacao_Aleatorio.terceiraA()
        elif 0<=clique.getX()<=80 and 470<=clique.getY()<=500: #Quinto botão
            window.close()

menu()