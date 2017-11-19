#pong

import pygame, pygame.locals

def main():
    # Initialise screen
    pygame.init()
    pygame.display.set_caption('Pong')
    screen = pygame.display.set_mode((800, 600))
    paddle = pygame.Surface((10, 100))
    paddlePosition = 300
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    paddlePosition = paddlePosition - 10
                if event.key == pygame.K_s:
                    paddlePosition = paddlePosition + 10
        screen.fill((128, 128, 200))    
        screen.blit(paddle, (5, paddlePosition))
        pygame.display.flip()

main()



