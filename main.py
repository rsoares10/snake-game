from turtle import Screen, Turtle
import time


def turtle_builder() -> Turtle:
    t = Turtle()
    t.shape("square")
    t.color("#FFFFFF")
    t.penup()
    return t


segments: list[Turtle] = []


def snake_builder() -> None:
    starting_positions = [(0, 0), (-20, 0), (-40, 0)]
    for pos in starting_positions:
        t = turtle_builder()
        t.goto(pos)
        segments.append(t)


def screen_builder() -> Screen:
    s = Screen()
    s.setup(width=600, height=600)
    s.bgcolor("#000000")
    s.title("Snake Game")
    s.tracer(0)
    return s


def main() -> None:
    snake = snake_builder()
    s = screen_builder()

    game_is_on = True
    while game_is_on:
        s.update()
        time.sleep(0.1)

        for seg_num in range(len(segments) - 1, 0, -1):
            new_x = segments[seg_num - 1].xcor()
            new_y = segments[seg_num - 1].ycor()
            segments[seg_num].goto(new_x, new_y)
        segments[0].forward(20)
        segments[0].left(90)

    s.exitonclick()


if __name__ == "__main__":
    main()
