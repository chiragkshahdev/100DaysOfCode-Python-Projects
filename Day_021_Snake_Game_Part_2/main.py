import pygame
import random
import sys

pygame.init()

# Settings
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
FPS = 12

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 50, 50)
WHITE = (255, 255, 255)
DARK_GREEN = (0, 150, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Day 21 - Snake Game Part 2 | By Chirag")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 25, bold=True)

def get_random_food(snake):
    while True:
        x = random.randint(0, GRID_WIDTH - 1)
        y = random.randint(0, GRID_WIDTH - 1)
        if (x, y) not in snake:
            return (x, y)

def main():
    snake = [(10, 10), (9, 10), (8, 10)]
    direction = (1, 0) # Right
    food = get_random_food(snake)
    score = 0
    level = 1

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                # Direction Control - No reverse
                if event.key == pygame.K_UP and direction!= (0, 1):
                    direction = (0, -1)
                elif event.key == pygame.K_DOWN and direction!= (0, -1):
                    direction = (0, 1)
                elif event.key == pygame.K_LEFT and direction!= (1, 0):
                    direction = (-1, 0)
                elif event.key == pygame.K_RIGHT and direction!= (-1, 0):
                    direction = (1, 0)

        # Move Snake
        head_x, head_y = snake[0]
        new_head = (head_x + direction[0], head_y + direction[1])

        # Wall Collision - Game Over
        if not (0 <= new_head[0] < GRID_WIDTH and 0 <= new_head[1] < GRID_WIDTH):
            break

        # Self Collision - Game Over
        if new_head in snake:
            break

        snake.insert(0, new_head)

        # Food Eat
        if new_head == food:
            score += 10
            if score % 50 == 0:
                level += 1
                global FPS
                FPS += 2 # Speed badhega
            food = get_random_food(snake)
        else:
            snake.pop() # Food nahi khaya to tail hatao

        # Draw
        screen.fill(BLACK)

        # Food
        pygame.draw.rect(screen, RED, (food[0]*GRID_SIZE, food[1]*GRID_SIZE, GRID_SIZE, GRID_SIZE), border_radius=5)

        # Snake
        for i, segment in enumerate(snake):
            color = GREEN if i == 0 else DARK_GREEN
            pygame.draw.rect(screen, color, (segment[0]*GRID_SIZE, segment[1]*GRID_SIZE, GRID_SIZE-2, GRID_SIZE-2), border_radius=4)

        # Score Board
        score_text = font.render(f"Score: {score} | Level: {level}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(FPS)

    # Game Over Screen
    screen.fill(BLACK)
    over_text = font.render(f"Game Over! Final Score: {score}", True, RED)
    restart_text = font.render("Press R to Restart or Q to Quit", True, WHITE)
    screen.blit(over_text, (WIDTH//2 - over_text.get_width()//2, HEIGHT//2 - 30))
    screen.blit(restart_text, (WIDTH//2 - restart_text.get_width()//2, HEIGHT//2 + 10))
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    main() # Restart
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

if __name__ == "__main__":
    main()