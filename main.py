import pygame
import random

pygame.init()

sprite_colour_change_event = pygame.USEREVENT + 1
background_colour_change_event = pygame.USEREVENT + 2

black = pygame.Color("black")
lightblue = pygame.Color("lightblue")
orange = pygame.Color("orange")

yellow = pygame.Color("yellow")
magenta = pygame.Color("magenta")
purple = pygame.Color("purple")
white = pygame.Color("white")

class sprite(pygame.sprite.Sprite):

    def __init__(self,color,height,width):
        super().__init__()

        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.randint(-1,1),random.randint(-1,1)]

    def update(self):
        self.rect.move_ip(self.velocity)
        boundary_hit = False
        if self.rect.left <= 0 or self.rect.right >= 500:
            self.velocity[0] = -self.velocity[0]
            boundary_hit = True

        if self.rect.top <= 0 or self.rect.bottom >= 400:
            self.velocity[1] = -self.velocity[1]
            boundary_hit = True

        if boundary_hit:
            pygame.event.post(pygame.event.Event(sprite_colour_change_event))
            pygame.event.post(pygame.event.Event(background_colour_change_event))

    def change_colour(self):
        self.image.fill(random.choice([yellow,magenta,purple,white]))


def change_background_color():
    global bg_color
    bg_color = random.choice([black, lightblue, orange])

all_sprites_list = pygame.sprite.Group()
sp1 = sprite(yellow, 20, 20)
sp1.rect.x = random.randint(0, 480)
sp1.rect.y = random.randint(0, 370)
all_sprites_list.add(sp1)

screen = pygame.display.set_mode([500,400])
pygame.display.set_caption("Sprite Collision Example")
bg_color = black
screen.fill(bg_color)

exit = False
clock = pygame.time.Clock()

while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        elif event.type == sprite_colour_change_event:
            sp1.change_colour()
        elif event.type == background_colour_change_event:
            change_background_color()

    all_sprites_list.update()
    screen.fill(bg_color)
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(240)

pygame.quit()