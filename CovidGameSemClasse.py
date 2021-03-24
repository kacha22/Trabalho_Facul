import pygame

Virus = [pygame.image.load('Virus1.png'), pygame.image.load('Virus1.png'), pygame.image.load('Virus1.png')
         , pygame.image.load('Virus1.png'), pygame.image.load('Virus1.png'), pygame.image.load('Virus1.png')
         , pygame.image.load('Virus1.png'), pygame.image.load('Virus1.png')]

x = 100
y = 150

retorne = 0
image = Virus[retorne]
image = pygame.transform.scale(image, (100 * 2, 100* 2))
rect = image.get_rect()
rect.topleft = x, y


velocidade = 10
screen = pygame.display.set_mode((720, 480))
pygame.display.set_caption('o jogo do covid')
cor = (255,255,255)
clock = pygame.time.Clock()
pygame.init()



while True:
    screen.fill(cor)
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.blit(Virus)
    pygame.display.flip()