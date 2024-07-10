import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 1000, 800
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shooter")


custom_font_path = 'PressStart2P-vaV7.ttf'
font = pygame.font.Font(custom_font_path, 36)  
game_over_font = pygame.font.Font(custom_font_path, 50)  


asteroid_image = pygame.image.load('asteroid.png')
original_asteroid_width, original_asteroid_height = asteroid_image.get_size()
asteroid_width = int(original_asteroid_width * 0.3)
asteroid_height = int(original_asteroid_height * 0.3)
asteroid_image = pygame.transform.scale(asteroid_image, (asteroid_width, asteroid_height))


clock = pygame.time.Clock()


player_width = 50
player_height = 60
player_x = WIDTH // 2
player_y = HEIGHT - player_height - 10
player_speed = 5


bullet_width = 5
bullet_height = 10
bullet_speed = 7
bullets = []


asteroid_speed = 5
asteroids = []


health = 100


score = 0

def draw_player(x, y):
    pygame.draw.polygon(screen, BLUE, [
        (x, y + player_height),
        (x + player_width // 2, y),
        (x + player_width, y + player_height)
    ])

def draw_bullet(bullets):
    for bullet in bullets:
        pygame.draw.rect(screen, RED, [bullet[0], bullet[1], bullet_width, bullet_height])

def draw_asteroid(asteroids):
    for asteroid in asteroids:
        screen.blit(asteroid_image, (asteroid[0], asteroid[1]))

def draw_health(health):
    if health >= 80:
        health_color = GREEN
    elif health >= 40:
        health_color = YELLOW
    else:
        health_color = RED
    health_text = font.render(f"Health: {health}", True, health_color)
    screen.blit(health_text, (10, 10))

def draw_score(score):
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 50))

def update_bullets(bullets):
    for bullet in bullets:
        bullet[1] -= bullet_speed
        if bullet[1] < 0:
            bullets.remove(bullet)

def update_asteroids(asteroids):
    global health
    for asteroid in asteroids:
        asteroid[1] += asteroid_speed
        if asteroid[1] > HEIGHT:
            asteroids.remove(asteroid)
            health -= 10
            if health <= 0:
                game_over()

def check_collision(bullets, asteroids):
    global score
    for bullet in bullets:
        for asteroid in asteroids:
            if (asteroid[0] < bullet[0] < asteroid[0] + asteroid_width) and (asteroid[1] < bullet[1] < asteroid[1] + asteroid_height):
                bullets.remove(bullet)
                asteroids.remove(asteroid)
                score += 1
                break

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
                    main()
                if event.key == pygame.K_l:
                    import lobby
                    lobby.lobby()

def main():
    global player_x, player_y, bullets, asteroids, health, score
    player_x, player_y = WIDTH // 2, HEIGHT - player_height - 10
    bullets = []
    asteroids = []
    health = 100
    score = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullets.append([player_x + player_width // 2, player_y])
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
            player_x += player_speed
        if keys[pygame.K_UP] and player_y > 0:
            player_y -= player_speed
        if keys[pygame.K_DOWN] and player_y < HEIGHT - player_height:
            player_y += player_speed

        
        update_bullets(bullets)
        update_asteroids(asteroids)
        check_collision(bullets, asteroids)

        
        if len(asteroids) < 5:
            asteroids.append([random.randint(0, WIDTH - asteroid_width), -asteroid_height])

        
        screen.fill(BLACK)
        draw_player(player_x, player_y)
        draw_bullet(bullets)
        draw_asteroid(asteroids)
        draw_health(health)
        draw_score(score)
        pygame.display.update()

        
        clock.tick(30)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
