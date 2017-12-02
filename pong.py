#pong

import pygame, pygame.locals

WIDTH = 800
HEIGHT = 600

def main():
    # Initialise screen
    pygame.init()
    pygame.display.set_caption('Pong')
    screen = pygame.display.set_mode((800, 600))
    paddle = pygame.Surface((10, 100))
    paddle2 = pygame.Surface((10, 100))
    paddlePosition = 300
    paddlePosition2 = 300
    while True:
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                return
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            paddlePosition = paddlePosition - 1
            if paddlePosition < 0:
                paddlePosition = 0
        if keys[pygame.K_s]:
            paddlePosition = paddlePosition + 1
            if paddlePosition > 500:
                paddlePosition = 500
        if keys[pygame.K_UP]:
            paddlePosition2 = paddlePosition2 - 1
        if keys[pygame.K_DOWN]:
            paddlePosition2 = paddlePosition2 + 1
        screen.fill((128, 128, 200))    
        screen.blit(paddle, (5, paddlePosition))
        screen.blit(paddle2, (785, paddlePosition2))
        pygame.display.flip()

main()



