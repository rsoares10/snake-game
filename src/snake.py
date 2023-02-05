from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self) -> None:
        self.body = Body()
        self.head = self.body.segments[0]

    def move(self) -> None:
        for seg_num in range(len(self.body.segments) - 1, 0, -1):
            new_x = self.body.segments[seg_num - 1].xcor()
            new_y = self.body.segments[seg_num - 1].ycor()
            self.body.segments[seg_num].goto(new_x, new_y)
        self.body.segments[0].forward(MOVE_DISTANCE)

    def left(self) -> None:
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self) -> None:
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def up(self) -> None:
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self) -> None:
        if self.head.heading() != UP:
            self.head.setheading(270)


class Body:
    def __init__(self) -> None:
        self.segments: list[Turtle] = self.build_body()

    def build_body(self) -> list[Turtle]:
        segments = []
        for pos in STARTING_POSITIONS:
            s = self.build_segment()
            s.goto(pos)
            segments.append(s)
        return segments

    def build_segment(self) -> Turtle:
        s = Turtle()
        s.shape("square")
        s.color("#FFFFFF")
        s.penup()
        return s
