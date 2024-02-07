import pygame   # impordib pygame
import sys  # impordib spetsiifilist funktsiooni
pygame.init()   # initsialiseerib pygame'i

# erinevate värvide valikud
sinine = [0,0,255]
lilla = [204,0,204]
oranz = [255,153,0]
must = [0,0,0]
punane = [255,0,0]

x = 640     # x-telje suurus
y = 480     # y-telje suurus
screen_size = (x,y)     # ekraani suuruse määramine
screen = pygame.display.set_mode(screen_size)
screen.fill([0,255,1])  # ekraani tausta värv

def ruudustik(screen, ruudu_suurus, x, y, joone_varv):  # funktsioon mis joonistab ruudustiku ja annab sellele vastavad parameetrid
    for x in range(x):
        for y in range(y):
            pygame.draw.rect(screen, joone_varv, (x * ruudu_suurus, y * ruudu_suurus, ruudu_suurus, ruudu_suurus), 1)

ruudu_suurus = 15   # määrab ruudu suuruse
joone_varv = must   # ruudu värvus
x = 50  # saab muuta x-telje ruudustiku arvu
y = 100     # saab muuta y-telje ruudustiku arvu

while True:     # mängutsükkel, saab ise "X"st kinni panna.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    ruudustik(screen, ruudu_suurus, x, y, joone_varv)   # kutsub välja ruudustiku funktsiooni

    pygame.display.flip()   # ekraani värskendus