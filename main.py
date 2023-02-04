from turtle import Screen, Turtle


def screen_builder() -> Screen:
    s = Screen()
    s.setup(width=600, height=600)
    s.bgcolor("#000000")
    s.title("Snake Game")
    return s


def main():
    s = screen_builder()
    s.exitonclick()


if __name__ == "__main__":
    main()
