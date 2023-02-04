from turtle import Screen, Turtle


def turtle_builder() -> Turtle:
    t = Turtle()
    t.shape("square")
    t.color("#FFFFFF")
    return t


def snake_builder() -> None:
    starting_positions = [(0, 0), (-20, 0), (-40, 0)]
    for pos in starting_positions:
        t = turtle_builder()
        t.goto(pos)


def screen_builder() -> Screen:
    s = Screen()
    s.setup(width=600, height=600)
    s.bgcolor("#000000")
    s.title("Snake Game")
    return s


def main() -> None:
    snake = snake_builder()

    s = screen_builder()
    s.exitonclick()


if __name__ == "__main__":
    main()
