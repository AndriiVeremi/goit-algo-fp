import turtle
import math
import sys

def draw_tree(branch_length, level):
    if level == 0 or branch_length < 2:
        return
    
    turtle.forward(branch_length)
    new_length = branch_length * math.sqrt(2) / 2
    
    turtle.left(45)
    draw_tree(new_length, level - 1)
    turtle.right(90)
    draw_tree(new_length, level - 1)
    turtle.left(45)
    
    turtle.backward(branch_length)

def main():
    sys.setrecursionlimit(1000)  # Збільшення ліміту рекурсії
    
    level = int(input("Введіть рівень рекурсії (рекомендовано 10-20): "))
    level = min(level, 20)  # Обмежуємо рівень рекурсії до 20
    
    turtle.speed(0)
    turtle.left(90)
    turtle.up()
    turtle.goto(0, -200)
    turtle.down()
    
    draw_tree(100, level)
    
    turtle.done()

if __name__ == "__main__":
    main()
