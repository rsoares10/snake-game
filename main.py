import time
from turtle import Screen

from src.snake import Snake


def screen_builder() -> Screen:
    s = Screen()
    s.setup(width=600, height=600)
    s.bgcolor("#000000")
    s.title("Snake Game")
    s.tracer(0)
    return s


def main() -> None:
    snake = Snake()
    s = screen_builder()

    s.listen()
    s.onkey(snake.up, "Up")
    s.onkey(snake.down, "Down")
    s.onkey(snake.left, "Left")
    s.onkey(snake.right, "Right")

    game_is_on = True
    while game_is_on:
        s.update()
        time.sleep(0.1)
        snake.move()

    s.exitonclick()


if __name__ == "__main__":
    main()
