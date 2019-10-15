import pygame
pygame.init()
window = pygame.display.set_mode((1000, 500))
pygame.display.set_caption("My First Python game")

x = 50
y = 50
hight = 60
Width = 40
vel = 5

run = True
while run:
      pygame.time.delay(100)
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
          run = False

pygame.quit()


