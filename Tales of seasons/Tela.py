import pygame, sys, os
from pygame.locals import *
from pygame import QUIT, K_UP, K_DOWN, K_LEFT, K_RIGHT, KEYDOWN,KEYUP, MOUSEMOTION, KEYUP, K_SPACE, K_x, K_w, K_d,K_s, K_a

pygame.init()
infoObject = pygame.display.Info()
tela=pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
rew=infoObject.current_w
reh=infoObject.current_h
estadomenu = True
estadoquarto = False
botao1 = pygame.image.load("C:/Users/tayla/Desktop/Season of tales/telas/menu inicial/configurar.png")
botao2 = pygame.image.load("C:/Users/tayla/Desktop/Season of tales/telas/menu inicial/iniciar.png")
botao3 = pygame.image.load("C:/Users/tayla/Desktop/Season of tales/telas/menu inicial/continuar.png")
botao4 = pygame.image.load("C:/Users/tayla/Desktop/Season of tales/telas/menu inicial/creditos.png")
cursor = pygame.image.load("C:/Users/tayla/Desktop/Season of tales/telas/menu inicial/cursor.png")
bg = pygame.image.load("C:/Users/tayla/Desktop/Season of tales/telas/menu inicial/inicial.png")
bg=pygame.transform.scale(bg, [rew, reh])
x = 870
y = 380
vely = 0
velx = 0
posx = [870, 540]
posy = [380, 450, 520, 590]
opcao = 0
selecao = 0

def menu():
    tela.blit(bg, [0, 0])
    tela.blit(botao1, [360, 490])  # Local do botão de configuração, para deixar com distancia perfeita diminuir de 70 em 70 o segundo termo
    tela.blit(botao2, [360, 350])  # botão iniciar
    tela.blit(botao3, [360, 420])  # botão continuar
    tela.blit(botao4, [360, 560])  # botão creditos
def Configuração():
    bgc = pygame.image.load("C:/Users/tayla/Desktop/Season of tales/configuração/Bg.png")
    bgc = pygame.transform.scale(bgc, (rew, reh))
    Alto = pygame.image.load("C:/Users/tayla/Desktop/Season of tales/configuração/alto.png")
    Alto = pygame.transform.scale(Alto, (300, 300))
    Normal = pygame.image.load("C:/Users/tayla/Desktop/Season of tales/configuração/normal.png")
    Normal = pygame.transform.scale(Normal, (350, 350))
    Mudo = pygame.image.load("C:/Users/tayla/Desktop/Season of tales/configuração/mudo.png")
    Mudo = pygame.transform.scale(Mudo,(300, 300))
    Salvar = pygame.image.load("C:/Users/tayla/Desktop/Season of tales/configuração/salvar.png")
    Salvar = pygame.transform.scale(Salvar, (400, 400))
    Sair = pygame.image.load("C:/Users/tayla/Desktop/Season of tales/configuração/sair.png")
    Sair = pygame.transform.scale(Sair, (400, 400))
    Grande = pygame.image.load("C:/Users/tayla/Desktop/Season of tales/configuração/tela grande.png")
    Medio = pygame.image.load("C:/Users/tayla/Desktop/Season of tales/configuração/tela media.png")
    Pequeno = pygame.image.load("C:/Users/tayla/Desktop/Season of tales/configuração/tela pequena.png")
    tela.blit(bgc, [0, 0])
    tela.blit(Alto, [800, 400])
    tela.blit(Normal, [400,380])
    tela. blit(Mudo, [50, 400])
    tela.blit(Salvar, [1000, 600])
    tela.blit(Sair, [-50, 550])
    tela.blit(Grande, [800, 200])
    tela.blit(Medio, [500, 200])
    tela.blit (Pequeno, [100, 200])

def creditos():
     bg = pygame.image.load("C:/Users/tayla/Desktop/Season of tales/ASSETS/telas/creditos.png")
     bg= pygame.transform.scale(bg, [rew, reh])
     tela.blit(bg, [0, 0])

def bgalt(bg):
    tela.fill((0, 0, 0))
    tela.blit(bg, [0, 0])
    pygame.display.update()

def quarto():
     bg = pygame.image.load("C:/Users/tayla/Desktop/Season of tales/telas/Quarto.png")
     bg = pygame.transform.scale(bg,(rew, reh))
     tela.blit(bg, [0, 0])
def limpatela():
    tela.fill((0, 0, 0))
    pygame.display.flip()

def players():
    vely = 0
    velx = 0
    y=100
    x=100
    gvely = 0
    gvelx = 0
    yg=500
    xg=500
    #calcular regras
    
    amy = pygame.image.load("C:/Users/tayla/Desktop/Season of tales/Amy.png")
    amy = pygame.transform.scale(amy, [100, 100])
    greg = pygame.image.load("C:/Users/tayla/Desktop/Season of tales/Greg.png")
    greg = pygame.transform.scale(greg, [100, 100])
    
    while estadoquarto == True :
        y = y+ vely
        x =  x + velx
        yg = yg+ gvely
        xg =  xg + gvelx
        pygame.display.update()
        quarto()
        tela.blit(amy, [x, y])
        tela.blit(greg, [xg, yg])
        
        
        for d in pygame.event.get():
            if d.type == KEYDOWN:
                    if d.key == K_UP:
                        
                         vely = -20
                    elif d.key == K_DOWN:
                         vely = +20
                    elif d.key == K_LEFT:
                        velx = -20
                    elif d.key == K_RIGHT:
                        velx = +20
                    elif d.key == K_w:
                        
                         gvely = -20
                    elif d.key == K_s:
                         gvely = +20
                    elif d.key == K_a:
                        gvelx = -20
                    elif d.key == K_d:
                        gvelx = +20
                        
            if d.type == KEYUP:
                    if d.key == K_UP:
                        vely = 0
                    elif d.key == K_DOWN:
                        vely = 0
                    elif d.key == K_RIGHT:
                        velx = 0
                    elif d.key == K_LEFT:
                        velx = 0
                    elif d.key == K_w:
                        gvely = 0
                    elif d.key == K_s:
                        gvely = 0
                    elif d.key == K_d:
                        gvelx = 0
                    elif d.key == K_a:
                        gvelx = 0
        
        pygame.display.update()
        #quarto()
        
        
       
                

#cores
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
#chama o menu
pygame.display.update()
tela.fill((BLACK))
    

menu()
#laço principal do jogo
while True:
    #funções para limpar a tela e chamar os componentes do menu
    vely = 0
    ax = 200
    ay = 200 - vely
 
    #posicionamento do cursor
    
    pygame.display.update()
    
    
    #controle do cursor
    for e in pygame.event.get():
        if e.type == KEYUP:
             if e.key == K_DOWN:
                opcao = (opcao) + 1
                if opcao >= 4:
                        opcao = 0
             if opcao == 0 and e.key == K_x:
                    
                         tela.fill(BLACK)
                         pygame.display.flip()
                         pygame.draw.rect(tela, BLACK, [75, 10, 1000, 1000], 0)
                         pygame.display.update()
                         pygame.display.flip()
                         quarto()
                         pygame.display.update()
                         pygame.display.flip()
                         estadomenu = False
                         estadoquarto = True
                         players()
                         
                         pygame.display.update()
                         
                             
             elif opcao == 2 and e.key == K_x:
                 tela.fill(BLACK)
                 pygame.display.flip()
                 pygame.draw.rect(tela, BLACK, [75, 10, 1000, 1000], 0)
                 pygame.display.flip()
                 pygame.display.update()
                 Configuração()
                 pygame.display.update()
                 pygame.display.flip()
                 estadomenu = False
             elif opcao == 3 and e.key == K_x:
                 tela.fill(BLACK)
                 pygame.display.flip()
                 pygame.draw.rect(tela, BLACK, [75, 10, 1000, 1000], 0)
                 pygame.display.flip()
                 pygame.display.update()
                 creditos()
                 pygame.display.update()
                 pygame.display.flip()
                 estadomenu = False
             elif e.key == K_UP:
                opcao = (opcao) - 1
                if opcao < 0:
                    opcao = 3
             if estadomenu:
                    menu()
                    tela.blit(cursor, [posx[selecao], posy[opcao]])


        #if e.type == KEYUP:

                         
        elif e.type == QUIT:
                exit()

        if e.type == KEYDOWN:
            if e.key == K_RIGHT:
                pygame.display.update()
                vely +10
                x = x - vely
























