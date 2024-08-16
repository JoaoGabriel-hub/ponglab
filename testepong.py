from PPlay.window import *
from PPlay.sprite import *
from PPlay.keyboard import *
from PPlay.collision import *
from PPlay.gameimage import *
import random

#JANELA
janela = Window(650, 650)
janela.set_title("joao gabriel")
janela.set_background_color((65,105,225))
fundo = GameImage("campo.png")

#BOLA
bola = Sprite("bolabasq.png", 1)
bola.set_position((janela.width/2 - bola.width/2), (janela.height/2 - bola.height/2))
velx = 400
vely = 400

#BARRA
pad1 = Sprite("barra.png")
pad1.set_position(5, janela.height/2 - pad1.height/2)
pad2 = Sprite("barra.png")
pad2.set_position(janela.width - pad2.width - 5, janela.height/2 - pad2.height/2)
velpad = 400

#TECLADO
key = keyboard.Keyboard()

#PONTUAÇÂO
pt1 = pt2 = 0
cont = 0
contD = 0

tempoini = 0

while True:
    janela.set_background_color((65, 105, 225))

    tempoini += janela.delta_time()
    if tempoini >= 1:
        bola.x += velx * janela.delta_time()
        bola.y += vely * janela.delta_time()

    #PONTOS
    if bola.x + bola.width > janela.height:
        pt1 += 1
        bola.set_position((janela.width/2 - bola.width/2), (janela.height/2 - bola.height/2))
        tempoini = 0
    if bola.x < 0:
        pt2 += 1
        bola.set_position((janela.width / 2 - bola.width / 2), (janela.height / 2 - bola.height / 2))
        tempoini = 0

    if bola.y + bola.height >= janela.height or bola.y <= 0:
        vely = vely * -1

    if bola.collided(pad1) and velx < 0:
        velx *= -1
        bola.x -= 1
        cont += 1
    if bola.collided(pad2) and velx > 0:
        velx *= -1
        bola.x -= 1
        cont += 1

    #CONTROLE
    if pad1.y > 0:
        if key.key_pressed("w"):
            pad1.move_y(-velpad * janela.delta_time())

    if pad1.y + pad1.height < janela.height:
        if key.key_pressed("s"):
            pad1.move_y(velpad * janela.delta_time())

    if pad2.y > 0:
        if key.key_pressed("up"):
            pad2.move_y(-velpad * janela.delta_time())

    if pad2.y + pad2.height < janela.height:
        if key.key_pressed("down"):
            pad2.move_y(velpad * janela.delta_time())

    if (bola.y > (janela.height*(1/2)) or bola.y > pad2.y) and velx > 0 and pad2.y < (janela.height - pad2.height):
        pad2.move_y(velpad*janela.delta_time())
    if (bola.y < janela.height*(1/2) or bola.y < pad2.y) and velx > 0 and pad2.y > 0:
        pad2.move_y(-velpad*janela.delta_time())

    xpad1 = pad1.x
    ypad1 = pad1.y
    xpad2 = pad2.x
    ypad2 = pad2.y

    #PLACAR E OBJETOS
    fundo.draw()
    janela.draw_text(str(pt1), x=(janela.width/4)*1, y=10, size=35, color="white", bold=True, italic=False)
    janela.draw_text(str(pt2), x=(janela.width /4)*3, y=10, size=35, color="white", bold=True, italic=False)
    bola.draw()
    pad1.draw()
    pad2.draw()
    janela.update()
