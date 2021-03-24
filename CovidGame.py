import pygame

pygame.init()

# Iniciando o display
width = 200
height = 100
Speed = 5
screen = pygame.display.set_mode((720 ,480))
pygame.display.set_caption('Game do virus')
Clock = pygame.time.Clock()

Cor = (255,255,170)

class Virus (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.sprite = []
        self.sprite.append(pygame.image.load('Virus1.png'))
        self.sprite.append(pygame.image.load('Virus2.png'))
        self.sprite.append(pygame.image.load('Virus3.png'))
        self.sprite.append(pygame.image.load('Virus4.png'))
        self.sprite.append(pygame.image.load('Virus5.png'))
        self.sprite.append(pygame.image.load('Virus6.png'))
        self.sprite.append(pygame.image.load('Virus7.png'))
        self.sprite.append(pygame.image.load('Virus8.png'))

        self.retorne = 0
        self.image = self.sprite[self.retorne]

        self.image = pygame.transform.scale(self.image, (100 * 2 ,100 * 2))

        self.rect = self.image.get_rect()
        self.rect.topleft = width, height



    def update(self):
        self.retorne = self.retorne + 0.25
        if self.retorne >= len(self.sprite):
            self.retorne = 0
        self.image = self.sprite[int(self.retorne)]
        self.image = pygame.transform.scale(self.image, (100 * 2, 100 * 2))


all_sprite = pygame.sprite.Group()
virus_sprite = Virus()
all_sprite.add(virus_sprite)

# Criando Loop
while True:
    Clock.tick(60)
    screen.fill(Cor)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    button = pygame.key.get_pressed()
    if width >= Speed:
        width += Speed

    all_sprite.draw(screen)
    all_sprite.update()
    pygame.display.flip()
