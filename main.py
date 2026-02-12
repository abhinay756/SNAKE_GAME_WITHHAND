import pygame
import cv2
from settings import *
from snake import SnakeGame
from hand_tracking import get_direction

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gesture Snake Game")
clock = pygame.time.Clock()

game = SnakeGame()
cap = cv2.VideoCapture(0)

running = True
while running:
    clock.tick(SPEED)
    screen.fill(BLACK)

    # Camera frame
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)  # Flip horizontally
    frame, gesture = get_direction(frame)

    if gesture:
        game.change_direction(gesture)

    # Move snake
    if not game.move():
        game = SnakeGame()  # Reset game on collision

    # Draw snake
    for block in game.snake:
        pygame.draw.rect(screen, GREEN, (block[0], block[1], BLOCK_SIZE, BLOCK_SIZE))

    # Draw food
    pygame.draw.rect(screen, RED, (game.food[0], game.food[1], BLOCK_SIZE, BLOCK_SIZE))
    
    # Draw Score
    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f"Score: {game.score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    cv2.imshow("Camera", frame)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
cap.release()
cv2.destroyAllWindows()
