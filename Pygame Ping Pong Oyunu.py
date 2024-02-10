import pygame
import sys

# OYUN PENCERESİ
pygame.init()
clock = pygame.time.Clock()
genislik = 800
yukseklik = 600
pencere = pygame.display.set_mode((genislik, yukseklik))
pygame.display.set_caption("Ping Pong Oyunu :)")

# RENKLER
beyaz = (255,255,255)
siyah = (0,0,0)

# ŞEKİLLER
raket1 = pygame.Rect(750,yukseklik/2 - 50,20,100)
raket2 = pygame.Rect(30,yukseklik/2 - 50,20,100)
top = pygame.Rect(genislik/2 - 10,yukseklik/2 - 10,20,20)
raket1_hiz = 0
raket2_hiz = 0
top_hiz_x = 5
top_hiz_y = 5

# SKOR
skor1 = 0
skor2 = 0
font = pygame.font.Font(None, 50)

# OYUN DÖNGÜSÜ
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                raket1_hiz += 7
            if event.key == pygame.K_UP:
                raket1_hiz -= 7
            if event.key == pygame.K_s:
                raket2_hiz += 7
            if event.key == pygame.K_w:
                raket2_hiz -= 7
        if event.type == pygame.KEYUP:
            raket1_hiz = 0
            raket2_hiz = 0
    if top.left <= 0:
        top_hiz_x *= -1
        top.center = (genislik/2, yukseklik/2)
        skor2 += 1
    if top.right >= genislik:
        top_hiz_x *= -1
        top.center = (genislik/2, yukseklik/2)
        skor1 += 1
    if top.colliderect(raket1) or top.colliderect(raket2):
        top_hiz_x *= -1
    if top.top <= 0 or top.bottom >= yukseklik:
        top_hiz_y *= -1

    if raket1.top <= 0:
         raket1.top = 0
    if raket1.bottom >= yukseklik:
         raket1.bottom = yukseklik
    if raket2.top <= 0:
         raket2.top = 0
    if raket2.bottom >= yukseklik:
         raket2.bottom = yukseklik

    raket1.y += raket1_hiz
    raket2.y += raket2_hiz
    top.x += top_hiz_x
    top.y += top_hiz_y
    
    pencere.fill(siyah)
    pygame.draw.rect(pencere, beyaz, raket1)
    pygame.draw.rect(pencere, beyaz, raket2)
    pygame.draw.ellipse(pencere, beyaz, top)
    skor_yazisi = font.render("1. Oyuncu: {} 2. Oyuncu: {}".format(skor1, skor2), False, beyaz)
    pencere.blit(skor_yazisi, (167,20))

    clock.tick(60)
    pygame.display.update()