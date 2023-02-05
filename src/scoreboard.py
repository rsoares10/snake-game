from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color("#FFFFFF")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self) -> None:
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self) -> None:
        self.score += 1
        self.clear()
        self.update_scoreboard()
