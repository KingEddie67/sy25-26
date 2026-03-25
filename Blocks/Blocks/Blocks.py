import pygame 
import random 

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge the Red Square")
clock = pygame.time.Clock()

# Player properties
player_pos = [WIDTH // 2, HEIGHT - 50]
player_size = 50

# Enemy properties
enemy_size = 50
enemy_pos = [random.randint(0, WIDTH - enemy_size), 0]
enemy_speed = 10

score = 0
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Movement Logic (with screen boundaries)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= 10  
    if keys[pygame.K_RIGHT] and player_pos[0] < WIDTH - player_size:
        player_pos[0] += 10  

    # Update enemy position
    enemy_pos[1] += enemy_speed

    # --- FIX BUG 2: Resetting the Enemy ---
    # Move the enemy back to the top and pick a new random X
    if enemy_pos[1] > HEIGHT:
        enemy_pos[1] = 0 - enemy_size
        enemy_pos[0] = random.randint(0, WIDTH - enemy_size)
        score += 1
        print(f"Score: {score}")

    # --- FIX BUG 3: Collision Detection ---
    # Using Pygame's Rect objects makes collision math much easier
    player_rect = pygame.Rect(player_pos[0], player_pos[1], player_size, player_size)
    enemy_rect = pygame.Rect(enemy_pos[0], enemy_pos[1], enemy_size, enemy_size)

    if player_rect.colliderect(enemy_rect):
        print(f"Game Over! Final Score: {score}")
        game_over = True
        
    # Drawing
    screen.fill((0, 0, 0))
    
    pygame.draw.rect(screen, RED, enemy_rect)
    pygame.draw.rect(screen, BLUE, player_rect)

    pygame.display.update()
    clock.tick(30)

pygame.quit()
