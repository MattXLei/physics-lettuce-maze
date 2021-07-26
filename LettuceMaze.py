from turtle import *
from Loading import *
from MazeCreation import *
from Questions import *
from time import sleep;


def main():
    print("")
    # Present the units
    print("A. One-Dimensional Motion")
    print("B. Forces")
    print("C. Work, Energy, and Power")
    print("D. Linear Momentum and Impulse")
    print("E. Rotational Kinematics")
    print("F. Rotational Dynamics")
    print("G. Universal Gravitation")
    print("H. Simple Harmonic Motion")
    topic = input("Type the letter for the topic you would like to be quizzed on. ")
    while (not "A" <= topic.upper() <= "H"): # Checks if user put an answer from A to H without using many if statements
        print("")
        topic = input("Type the letter for the topic you would like to be quizzed on. ")
    print("")
    print("")
    print("")
    practice(topic, turby) # Directs to the Questions project

    again = input("If you would like to play this game again, enter Y. Else, enter N. ")
    if again.isalpha() and again.upper() == "Y":
        main()
    else:
        print("")
        bye() # Directs to the press any key to leave command

# Setup the Screen
screen = Screen()
question = Turtle()
question.hideturtle()
question.speed(0)
question.shape("turtle")
question.color("white")
question.penup()
question.goto(-300, 0)
turby = Turtle()
turby.hideturtle()
turby.speed(0)
turby.shape("turtle")
turby.penup()
turby.goto(-250, -200)
turby.left(90)
turby.color("green")
turby.showturtle()
loading.reset()
loading.hideturtle()
    
print("Welcome to the AP Physics 1 Lettuce Maze!")
sleep(2)
print("To complete the maze, you must answer all 10 questions correctly for a AP Physics 1 Unit of your choice.")
sleep(3)
main()
