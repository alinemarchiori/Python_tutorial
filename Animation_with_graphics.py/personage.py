from graphics import *
import time

def fundo(win): 
    win.setBackground("Gray")
    # imagem = Image(Point(425, 190), "fundo.png")
    # imagem.draw(win)
    
def desenha_chao(win):
    imagem = Image(Point(100,480), "Tile.png")
    imagem.draw(win)
    imagem = Image(Point(350,480), "Tile.png")
    imagem.draw(win)
    imagem = Image(Point(600,480), "Tile.png")
    imagem.draw(win)
    imagem = Image(Point(850,480), "Tile.png")
    imagem.draw(win)

class Personagem:
    def __init__(self, janela):
        self.janela = janela
        self.imagem = Image(Point(100,340), "player-idle-1.png")
        self.centro = self.imagem.getAnchor()
        self.cont_parado = 0
        self.cont_correndo = 0
        
        
    def movimento(self, para, corre):

        while True:

            self.verifica = self.janela.checkKey()

            if self.verifica == "Right":
                self.imagem.move(15, 0)
                self.centro = self.imagem.getAnchor()
                self.imagem = Image(self.centro, corre[self.cont_correndo])
                self.imagem.draw(self.janela)
                time.sleep(.08)
                self.imagem.undraw()
                self.cont_correndo+=1
                time.sleep(.001)
                if self.cont_correndo >= 6:
                    self.cont_correndo = 0

            elif self.verifica == "Left":
                self.imagem.move(-15, 0)
                self.centro = self.imagem.getAnchor()
                self.imagem = Image(self.centro, corre[self.cont_correndo])
                self.imagem.draw(self.janela)
                time.sleep(.08)
                self.imagem.undraw()
                self.cont_correndo+=1
                time.sleep(.001)
                if self.cont_correndo >= 6:
                    self.cont_correndo = 0

            else: 
                if self.cont_parado >= 4:
                    self.cont_parado = 0
                self.imagem = Image(self.centro, para[self.cont_parado])
                self.imagem.draw(self.janela)
                time.sleep(.09)
                self.imagem.undraw()
                self.cont_parado+=1

#função principal
def main (Titulo: str, largura: int, altura:int):
    #cria janela 
    win = GraphWin(Titulo, largura, altura)
    #desenha fundo e o chão
    fundo(win)
    desenha_chao(win)
    #cria objeto, instanciando a classe
    raposa = Personagem(win)
    #listas com as sprites do personagem, cada string é o nome de uma imagem
    parado = ["player-idle-1.png", "player-idle-2.png", "player-idle-3.png", "player-idle-4.png"]
    correndo = ["player-run-1.png", "player-run-2.png", "player-run-3.png", "player-run-4.png","player-run-5.png","player-run-6.png"]
    #chamando a função para realizar o movimento do personagem
    raposa.movimento(parado, correndo)
    
    win.getMouse()
    win.close()
    
main("Animação", 850, 478)
