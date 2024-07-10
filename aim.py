import pygame
import sys
import random
import time

pygame.init()


WIDTH, HEIGHT = 1000, 800
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aim Trainer")


custom_font_path = 'PressStart2P-vaV7.ttf'
font = pygame.font.Font(custom_font_path, 36)  
game_over_font = pygame.font.Font(custom_font_path, 50)  


clock = pygame.time.Clock()


target_radius = 25
score = 0
game_time = 30
start_time = None

def draw_target(x, y):
    pygame.draw.circle(screen, RED, (x, y), target_radius)

def draw_score(score):
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

def draw_timer(time_left):
    if time_left > 20:
        color = GREEN
    elif time_left > 10:
        color = YELLOW
    else:
        color = RED
    timer_text = font.render(f"Time: {time_left}", True, color)
    screen.blit(timer_text, (WIDTH - 300, 10))

def game_over():
    screen.fill(BLACK)
    
    you_scored_text = font.render(f"You Scored: {score}", True, WHITE)
    you_scored_rect = you_scored_text.get_rect(center=(WIDTH // 2, HEIGHT // 8))
    screen.blit(you_scored_text, you_scored_rect)

    game_over_text = game_over_font.render("Time's Up!", True, RED)
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
                    main()
                if event.key == pygame.K_l:
                    import lobby
                    lobby.lobby()

def main():
    global score, start_time
    score = 0
    start_time = time.time()

    
    target_x = random.randint(target_radius, WIDTH - target_radius)
    target_y = random.randint(target_radius, HEIGHT - target_radius)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if (mouse_x - target_x) ** 2 + (mouse_y - target_y) ** 2 <= target_radius ** 2:
                    score += 1
                    target_x = random.randint(target_radius, WIDTH - target_radius)
                    target_y = random.randint(target_radius, HEIGHT - target_radius)

        
        elapsed_time = time.time() - start_time
        time_left = max(0, game_time - int(elapsed_time))
        if time_left == 0:
            game_over()

        
        screen.fill(BLACK)
        draw_target(target_x, target_y)
        draw_score(score)
        draw_timer(time_left)
        pygame.display.update()

        
        clock.tick(30)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
