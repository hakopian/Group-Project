import pygame
import sys
import snake
import aim
import shooter

pygame.init()


WIDTH, HEIGHT = 1000, 800
GREEN = (0, 255, 0)
RED = (255, 0, 0)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Virtual Arcade Lobby")


background_image = pygame.image.load('background.jpg')  

custom_font_path = 'PressStart2P-vaV7.ttf'
title_font = pygame.font.Font(custom_font_path, 50)  
option_font = pygame.font.Font(custom_font_path, 30)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def lobby():
    while True:
        screen.blit(background_image, (0, 0)) 
        draw_text('Virtual Arcade', title_font, GREEN, screen, 150, 100)
        draw_text('1. Snake', option_font, RED, screen, 300, 250)
        draw_text('2. Aim Test', option_font, RED, screen, 300, 350)
        draw_text('3. Shooter', option_font, RED, screen, 300, 450)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    snake.game()
                elif event.key == pygame.K_2:
                    aim.main()
                elif event.key == pygame.K_3:
                    shooter.main()

        pygame.display.flip()

if __name__ == "__main__":
    lobby()
