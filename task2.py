import turtle
import math
import sys

def draw_tree(branch_length, level, pen): 
    if level == 0 or branch_length < 2:
        return

    pen.forward(branch_length)  
    new_length = branch_length * math.sqrt(2) / 2

    pen.left(45)
    draw_tree(new_length, level - 1, pen) 
    pen.right(90)
    draw_tree(new_length, level - 1, pen) 
    pen.left(45)

    pen.backward(branch_length) 

def main():
    sys.setrecursionlimit(1000)

    level = int(input("Введіть рівень рекурсії (рекомендовано 10-20): "))
    level = min(level, 20)

    screen = turtle.Screen() 
    pen = turtle.Turtle()   

    pen.speed(0)
    pen.left(90)
    pen.penup()
    pen.goto(0, -200)
    pen.pendown()

    draw_tree(100, level, pen) 

    screen.exitonclick()  


if __name__ == "__main__":
    main()