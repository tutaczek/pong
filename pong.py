#pong

import pygame, pygame.locals

def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Pong')
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                return
        pygame.display.flip()

main()



