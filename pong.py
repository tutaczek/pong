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
    ball = pygame.Surface((10, 10))
    paddlePosition = 300
    paddlePosition2 = 300
    ballPositionX = 400
    ballPositionY = 300
    ballVelocityX = 200
    ballVelocityY = 200
    lastTime = pygame.time.get_ticks() / 1000.0

    while True:
        currentTime = pygame.time.get_ticks() / 1000.0
        dt = currentTime - lastTime
        lastTime = currentTime
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
        
        if ballPositionX >= 5 and ballPositionX <= 15 \
                and ballPositionY >= paddlePosition and ballPositionY <= paddlePosition + 100:
            ballVelocityX = -ballVelocityX
        if ballPositionX + 10 >= 785 and ballPositionX + 10 <= 795 \
                and ballPositionY >= paddlePosition2 and ballPositionY <= paddlePosition2 + 100:
            ballVelocityX = -ballVelocityX

        if ballPositionY <= 0 or ballPositionY >= 600:
            ballVelocityY = -ballVelocityY
        ballPositionX = ballPositionX + ballVelocityX * dt
        ballPositionY = ballPositionY + ballVelocityY * dt
        screen.fill((128, 128, 200))    
        screen.blit(paddle, (5, paddlePosition))
        screen.blit(paddle2, (785, paddlePosition2))
        screen.blit(ball, (ballPositionX, ballPositionY))
        pygame.display.flip()

main()



