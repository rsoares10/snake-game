from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("#0000FF")
        self.speed("fastest")
        self.set_random_pos()

    def set_random_pos(self) -> None:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)
