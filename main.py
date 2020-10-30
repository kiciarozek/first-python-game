import pygame
import random


# initializowanie game
pygame.init()

# tworzenie okna gry
screensize = 800, 600
screen = pygame.display.set_mode(screensize)

# tlo gry
background = pygame.image.load("game/tlo.jpg")

# kolor tła (RGB)
color = 0, 0, 0

# tytuł i ikona
pygame.display.set_caption("gierka")
icon = pygame.image.load('game/ikona.png')
pygame.display.set_icon(icon)

# gracz
playerImg = pygame.image.load("game/statek.png")
playerX = 370
playerY = 480
playerX_change = 0

# wróg
enemyImg = pygame.image.load("game/kosmita.png")
enemyX = random.randint(0,800)
enemyY = random.randint(50,150)
enemyX_change = 0.5
enemyY_change = 40

# pocisk
# ready - pocisk jest gotowy do strzału
# fire - pocisk jest wystrzelony i widoczny
bulletImg = pygame.image.load("game/pocisk.png")
bulletX = 0
bulletY = 480
bulletY_change = 2
bullet_state = "ready"

def Enemy(x, y):
    screen.blit(enemyImg, (x, y))

def Player(x,y):
    screen.blit(playerImg, (x, y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg,(x + 16,y + 10))

# pętla gry
running = True
while running:
    screen.fill((color))
    # wyswietlanie tla
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change -= 0.7
            if event.key == pygame.K_RIGHT:
                playerX_change += 0.7
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = playerX
                    fire_bullet(playerX,bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    # sprzawdzanie czy dotyka ściany i zablokowanie przechodzenia przez nie
    playerX += playerX_change

    if playerX < 0:
        playerX = 0
    elif playerX > 736:
        playerX = 736

    # poruszanie się wroga
    enemyX += enemyX_change

    if enemyX < 0:
        enemyX_change = 0.5
        enemyY += enemyY_change
    elif enemyX > 736:
        enemyX_change = -0.5
        enemyY += enemyY_change

    #poruszanie się pocisku
    if bulletY <= -16:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change

    Player(playerX,playerY)
    Enemy(enemyX, enemyY)
    pygame.display.update()
