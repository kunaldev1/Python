"""Draw a simple recursive tree using Python's turtle graphics."""

import turtle


def draw_tree(branch_length, pen):
    """Draw branches recursively while the branch length is large enough."""
    if branch_length > 5:
        pen.forward(branch_length)
        pen.right(20)
        draw_tree(branch_length - 15, pen)
        pen.left(40)
        draw_tree(branch_length - 15, pen)
        pen.right(20)
        pen.backward(branch_length)


def main():
    """Create a turtle window and draw the tree."""
    pen = turtle.Turtle()
    window = turtle.Screen()
    pen.left(90)
    pen.penup()
    pen.backward(100)
    pen.pendown()
    pen.color("green")
    draw_tree(75, pen)
    window.exitonclick()


if __name__ == "__main__":
    main()
