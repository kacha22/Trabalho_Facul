import pygame

class Virus(pygame.sprite.Sprite):
    def __init__(self):
        super(Virus, self).__init__()
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
        self.rect = pygame.Rect(5,5,150,198)


        self.retorne += 1
        if self.retorne >= len(self.sprite):
            self.retorne = 0
        self.sprite = self.sprite[self.retorne]

pygame.init()
my_sprite = Virus()
my_group = pygame.sprite.Group(my_sprite)
clock = pygame.time.Clock()

# Iniciando o display

width = 1280
height = 720
pixelwalk = 5
screen = pygame.display.set_mode((width, height))
screen.fill((25,255,255))

#Criando o loop

Running = True
clock = pygame.time.Clock()
while Running:
    for event in pygame.event.get():
        clock.tick(10)
        if event.type == pygame.QUIT:
            Running = quit()

my_group.draw(screen, (width,height))
pygame.display.flip()
clock.tick(10)


pygame.quit()