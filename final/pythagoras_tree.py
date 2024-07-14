# pythagoras_tree.py

import turtle
import tkinter as tk

def draw_branch(t, branch_length, angle, level):
    """
    Малює одну гілку дерева Піфагора.
    
    :param t: об'єкт turtle
    :param branch_length: довжина гілки
    :param angle: кут розгалуження
    :param level: рівень рекурсії
    """
    if level == 0:
        return

    # Якщо рівень рекурсії 1, встановлюємо зелений колір для листя
    if level == 1:
        t.color("green")
    else:
        t.color("brown")

    # Малюємо головну гілку
    t.forward(branch_length)

    # Зберігаємо поточну позицію та напрямок
    position = t.position()
    heading = t.heading()

    # Малюємо праву гілку
    t.right(angle)
    draw_branch(t, branch_length * 0.7, angle, level - 1)

    # Повертаємося до головної гілки
    t.penup()
    t.goto(position)
    t.setheading(heading)
    t.pendown()

    # Малюємо ліву гілку
    t.left(angle)
    draw_branch(t, branch_length * 0.7, angle, level - 1)

    # Повертаємося до головної гілки
    t.penup()
    t.goto(position)
    t.setheading(heading)
    t.pendown()

def draw_tree(level):
    """
    Малює дерево Піфагора з заданим рівнем рекурсії.
    
    :param level: рівень рекурсії
    """
    # Налаштовуємо turtle
    root = tk.Tk()
    canvas = tk.Canvas(master=root, width=800, height=600)
    canvas.pack()
    screen = turtle.TurtleScreen(canvas)
    screen.bgcolor("white")

    t = turtle.RawTurtle(screen)
    t.speed(0)
    t.penup()
    t.goto(0, -200)
    t.pendown()
    t.left(90)  # Повертаємо turtle вгору

    # Малюємо дерево Піфагора
    draw_branch(t, 100, 30, level)

    # Завершуємо малювання
    root.mainloop()
