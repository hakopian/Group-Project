import pygame
import sys
import random

pygame.init()


WIDTH, HEIGHT = 1000, 800
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")


custom_font_path = 'PressStart2P-vaV7.ttf'
font = pygame.font.Font(custom_font_path, 36)  
game_over_font = pygame.font.Font(custom_font_path, 50)  


clock = pygame.time.Clock()


snake_block = 10
snake_speed = 15


score = 0

def draw_snake(snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, BLUE, [x[0], x[1], snake_block, snake_block])

def draw_food(foodx, foody):
    pygame.draw.rect(screen, RED, [foodx, foody, snake_block, snake_block])

def draw_score(score):
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

def game_over():
    screen.fill(BLACK)
    
    you_scored_text = font.render(f"You Scored: {score}", True, WHITE)
    you_scored_rect = you_scored_text.get_rect(center=(WIDTH // 2, HEIGHT // 8))
    screen.blit(you_scored_text, you_scored_rect)

    game_over_text = game_over_font.render("Game Over", True, RED)
    game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    screen.blit(game_over_text, game_over_rect)
    
    play_again_text = font.render("Press P to Play Again", True, WHITE)
    play_again_rect = play_again_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(play_again_text, play_again_rect)
    
    back_to_lobby_text = font.render("Press L to Back to Lobby", True, WHITE)
    back_to_lobby_rect = back_to_lobby_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    screen.blit(back_to_lobby_text, back_to_lobby_rect)
    
    pygame.display.update()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    game()
                if event.key == pygame.K_l:
                    import lobby
                    lobby.lobby()

def game():
    global score
    game_over_flag = False

    x1 = WIDTH / 2
    y1 = HEIGHT / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, WIDTH - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, HEIGHT - snake_block) / 10.0) * 10.0

    score = 0

    while not game_over_flag:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_over()
            return

        x1 += x1_change
        y1 += y1_change
        screen.fill(BLACK)
        draw_food(foodx, foody)
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_over()
                return

        draw_snake(snake_List)
        draw_score(score)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, WIDTH - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, HEIGHT - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
            score += 1

        clock.tick(snake_speed)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    game()
