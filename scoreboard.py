from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.show_score()

    def show_score(self):
        self.color("White")
        self.penup()
        self.hideturtle()
        self.setpos(-30, 250)
        self.write(f"Score: {self.score} ", move= False, align= "center", font= ("Arial", 18, "normal"))

    def increase_score(self):
        self.score += 1

    def game_over(self):
        self.color("White")
        self.penup()
        self.hideturtle()
        self.setpos(0, 0)
        self.write("GAME OVER", move= False, align= "center", font= ("Arial", 24, "normal"))

