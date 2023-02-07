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


def has_hit_wall(s: Snake) -> bool:
    hit_right_wall = s.head.xcor() > 280
    hit_left_wall = s.head.xcor() < -280
    hit_top_wall = s.head.ycor() > 280
    hit_bottom_wall = s.head.ycor() < -280
    return hit_bottom_wall or hit_left_wall or hit_top_wall or hit_right_wall


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
            snake.extend()
            food.set_random_pos()
            score_board.increase_score()
        if has_hit_wall(snake):
            game_is_on = False
            score_board.game_over()
    screen.exitonclick()


if __name__ == "__main__":
    main()
