from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self) -> None:
        self.body = Body()

    def move(self) -> None:
        for seg_num in range(len(self.body.segments) - 1, 0, -1):
            new_x = self.body.segments[seg_num - 1].xcor()
            new_y = self.body.segments[seg_num - 1].ycor()
            self.body.segments[seg_num].goto(new_x, new_y)
        self.body.segments[0].forward(MOVE_DISTANCE)
        self.body.segments[0].left(90)


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
