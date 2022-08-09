import curses
import random
from package.snake import Snake
from package.food import Food
from package.table import Field

def game():
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)
    field = Field()
    snake = Snake()
    food = Food(random.randint(0, 14), random.randint(0, 14), random.choice(['G', 'D', 'E']))
    head_x = snake.body[0][0]
    head_y = snake.body[0][1]

    while 0 <= head_x < 15 and 0 <= head_y < 15:
        
        stdscr.clear()             
        field.turn(snake, food)
        for elm in field.pole:
            a = ' '.join(elm) + '\n'
            stdscr.addstr(a)
            stdscr.refresh()

        key = stdscr.getch()

        if key == 452:
            head_y -= 1
        elif key == 454:
            head_y += 1
        elif key == 450:
            head_x -= 1
        elif key == 456:
            head_x += 1

        snake.move(head_x, head_y)

        if head_x == food.x and head_y == food.y:
            snake.eat()
            food = Food(random.randint(0, 14), random.randint(0, 14), random.choice(['G', 'D', 'E']))
    
    print('Game Over')

