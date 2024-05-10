import turtle as t
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def add_segment(self, position):
        new_segment = t.Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def create_snake(self):
        for i in range(3):
            self.add_segment(STARTING_POSITIONS[i])

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def go_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def go_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def go_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def go_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_snake(self):
        for j in range(len(self.segments) - 1, 0, -1):
            self.segments[j].setx(self.segments[j - 1].xcor())
            self.segments[j].sety(self.segments[j - 1].ycor())
        self.head.forward(DISTANCE)

    def reset_snake(self):
        for segment in self.segments:
            segment.goto(1200, 1200)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
