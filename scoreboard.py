from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()  # Hide the Turtle cursor
        self.penup()  # No drawing while moving
        self.goto(-280, 250)  # Set initial position on the screen
        self.update_scoreboard()  # Display the initial score

    def update_scoreboard(self):
        self.clear()  # Clear the previous scoreboard content
        self.write(f"Level: {self.level}", align="left", font=FONT)   # Write the updated score

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
