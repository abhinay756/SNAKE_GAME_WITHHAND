import random
from settings import BLOCK_SIZE, WIDTH, HEIGHT

class SnakeGame:
    def __init__(self):
        self.snake = [(300,300)]
        self.direction = "RIGHT"
        self.food = self.spawn_food()
        self.score = 0

    def spawn_food(self):
        x = random.randint(0, (WIDTH-BLOCK_SIZE)//BLOCK_SIZE) * BLOCK_SIZE
        y = random.randint(0, (HEIGHT-BLOCK_SIZE)//BLOCK_SIZE) * BLOCK_SIZE
        return (x,y)

    def move(self):
        head_x, head_y = self.snake[0]

        if self.direction == "UP":
            head_y -= BLOCK_SIZE
        elif self.direction == "DOWN":
            head_y += BLOCK_SIZE
        elif self.direction == "LEFT":
            head_x -= BLOCK_SIZE
        elif self.direction == "RIGHT":
            head_x += BLOCK_SIZE

        new_head = (head_x, head_y)
        self.snake.insert(0, new_head)

        # Check food collision
        if new_head == self.food:
            self.food = self.spawn_food()
            self.score += 1
        else:
            self.snake.pop()
        
        # Screen Wrapping
        if head_x < 0:
            head_x = WIDTH - BLOCK_SIZE
        elif head_x >= WIDTH:
            head_x = 0
        
        if head_y < 0:
            head_y = HEIGHT - BLOCK_SIZE
        elif head_y >= HEIGHT:
            head_y = 0
            
        # Update head position after wrapping
        self.snake[0] = (head_x, head_y)

        # Check self collision
        if len(self.snake) > 1 and (head_x, head_y) in self.snake[1:]:
             return False
            
        return True

    def change_direction(self, new_dir):
        self.direction = new_dir
