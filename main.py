import time
from turtle import Screen

from src.food import Food
from src.scoreboard import ScoreBoard
from src.snake import Snake


def build_screen() -> Screen:
    s = Screen()
    s.setup(width=600, height=600)
    s.bgcolor("#000000")
    s.title("Snake Game")
    s.tracer(0)
    return s


def main() -> None:
    screen = build_screen()
    snake = Snake()
    food = Food()
    score_board = ScoreBoard()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()
        if snake.head.distance(food) < 15:
            food.set_random_pos()
            score_board.increase_score()
    screen.exitonclick()


if __name__ == "__main__":
    main()
