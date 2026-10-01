from io import BytesIO

from PIL import Image
from rembg import remove

input_image = Image.open("Sharingan.jpg")

output = remove(input_image)

if isinstance(output, bytes):
    output = Image.open(BytesIO(output))

output.save("output_image.png")

# Tree
import turtle

screen = turtle.Screen()
screen.bgcolor("black")

tree = turtle.Turtle()
tree.speed(0)
tree.color("brown")
tree.left(90)
tree.penup()
tree.goto(0, -250)
tree.pendown()


def draw_tree(branch):
    if branch < 5:
        return
    tree.forward(branch)

    tree.right(25)
    draw_tree(branch * 0.75)

    tree.left(50)
    draw_tree(branch * 0.75)

    tree.right(25)
    tree.backward(branch)


draw_tree(100)

turtle.done()

# R_P_S_Game
import random

items = ["rock", "paper", "scissors"]

computer = random.choice(items)

user = input("Enter rock, paper, or scissors: ").lower()

print("Computer chooses:", computer)

if user == computer:
    print("It's a tie!")
elif user == "rock" and computer == "scissors":
    print("You win!")
elif user == "paper" and computer == "rock":
    print("You win!")
elif user == "scissors" and computer == "paper":
    print("You win!")
elif computer == "rock" and user == "scissors":
    print("Computer wins!")
elif computer == "paper" and user == "rock":
    print("Computer wins!")
elif computer == "scissors" and user == "paper":
    print("Computer wins!")
else:
    print("Invalid input. Please enter rock, paper, or scissors!!!")
