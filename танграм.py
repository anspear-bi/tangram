import turtle as t


def draw_triangle_big(color, position):
    t.penup()  # Поднимаем перо
    t.goto(position)  # Переходим в указанную позицию
    t.pendown()  # Опускаем перо
    t.fillcolor(color)  # Устанавливаем цвет заливки
    t.color(color)  # Устанавливаем цвет линии
    t.begin_fill()  # Начинаем заливку

    t.forward(75)  # База треугольника
    t.left(90)  # Поворачиваем на 90 градусов
    t.forward(75)  # Высота треугольника
    t.goto(position)  # Возвращаемся к началу

    t.end_fill()  # Заканчиваем заливку
    t.setheading(0)  # Поворачиваем вправо


def draw_parallelogram(color, position):
    t.penup()
    t.goto(position)
    t.pendown()
    t.fillcolor(color)
    t.color(color)
    t.begin_fill()
    t.forward(42.5)
    t.left(60)
    t.forward(30)
    t.left(120)
    t.forward(42.5)
    t.left(60)
    t.forward(30)
    t.end_fill()
    t.setheading(0)  # Поворачиваем вправо


def draw_triangle_mini(color, position):
    t.penup()
    t.goto(position)
    t.pendown()
    t.fillcolor(color)
    t.color(color)
    t.begin_fill()

    t.forward(30)
    t.left(90)
    t.forward(30)
    t.goto(position)

    t.end_fill()
    t.setheading(0)
    
def draw_triangle_mini_mirror(color, position):
    t.penup()
    t.goto(position)
    t.pendown()
    t.fillcolor(color)
    t.color(color)
    t.begin_fill()

    t.forward(30)
    t.right(90)
    t.forward(30)
    t.goto(position)

    t.end_fill()
    t.setheading(0)

def draw_triangle_midle(color, position):
    t.penup()
    t.goto(position)
    t.pendown()
    t.fillcolor(color)
    t.color(color)
    t.begin_fill()

    t.forward(50)
    t.left(90)
    t.forward(50)
    t.goto(position)

    t.end_fill()
    t.setheading(0)


def draw_square(color, position):
    t.penup()
    t.goto(position)
    t.pendown()
    t.color(color)
    t.fillcolor(color)
    t.begin_fill()
    for i in range(4):
        t.forward(37.5)  # Длина стороны
        t.right(90)
    t.end_fill()
    t.setheading(0)  # Поворачиваем вправо
    
    
def draw_square_big(color, position):
    t.penup()
    t.goto(position)
    t.pendown()
    t.color(color)
    t.fillcolor(color)
    t.begin_fill()
    for i in range(4):
        t.forward(75)  # Длина стороны
        t.right(90)
    t.end_fill()
    t.setheading(0)  # Поворачиваем вправо

def draw__rectangle (color, position):
    t.penup()
    t.goto(position)
    t.pendown()
    t.color(color)
    t.fillcolor(color)
    t.begin_fill()
    t.forward(120)
    t.right(90)
    t.forward(160)
    t.right(90)
    t.forward(120)
    t.right(90)
    t.forward(160)
    t.end_fill()
    t.setheading(0)
 

def draw_circle_big(color, position):
    t.penup()
    t.goto(position)
    t.pendown()
    t.color(color)
    t.fillcolor(color)
    t.begin_fill()
    t.circle(60)
    t.end_fill()
    t.setheading(0)
    
def draw_circle_midle(color, position):
     t.penup()
     t.goto(position)
     t.pendown()
     t.color(color)
     t.fillcolor(color)
     t.begin_fill()
     t.circle(30) 
     t.end_fill()
     t.setheading(0)
     
def draw_circle_mini(color, position):
    t.penup()
    t.goto(position)
    t.pendown()
    t.color(color)
    t.fillcolor(color)
    t.begin_fill()
    t.circle(7)
    t.end_fill()
    t.setheading(0)

# Настройка turtle
t.speed(30)

#кролик
draw_triangle_midle('cyan', (-400, 250))
t.left(270)
draw_triangle_mini('magenta', (-350, 280))
t.left(180)
draw_triangle_big('yellow', (-325, 325))
draw_triangle_big('red', (-400, 325))
draw_square('orange', (-325, 418.75))
t.left(45)
draw_triangle_mini('pink', (-325, 325 - 1800**0.5/2))
t.left(120)
draw_parallelogram('lightgreen', (-306.25, 418.75))


#рыбка
t.left(120)
draw_parallelogram('lightgreen', (-90, 355))
t.left(180)
draw_triangle_mini('pink', (-90, 355))
draw_triangle_mini('magenta', (-150, 325))
t.left(45)
draw_square('orange', (-90, 355))
draw_triangle_big('yellow', (-165 + 2812.5**0.5, 280))
t.left(90)
draw_triangle_big('red', (-90 + 2812.5**0.5, 355))
t.left(45)
draw_triangle_midle('cyan', (-89 + 2812.5**0.5, 355 - 5000**0.5/2))



#бабочка

draw_triangle_big('yellow', (575, -300))
t.left(270)
draw_triangle_big('red', (500, -225))
draw_square('orange', (575, -301))
t.left(180)
draw_triangle_mini('pink', (644, -301))
t.left(180)
draw_triangle_midle('cyan', (575, -301))
t.left(47)
draw_parallelogram('lightgreen', (546, -371))
t.left(90)
draw_triangle_mini('magenta', (613, -370))

#уточка
t.left(0)
draw_triangle_big('yellow', (190, -360))
t.left(315)
draw_triangle_big('red', (158, -285))
t.left(135)
draw_triangle_mini('magenta', (260, -380))
t.left(45)
draw_triangle_midle('cyan', (266, -355))
t.left(90)
draw_parallelogram('lightgreen', (294, -313))
t.left(42)
draw_square('orange', (266, -239))
t.left(131)
draw_triangle_mini('pink', (339, -265))


# всадник

t.left(90)
draw_triangle_big('blue', (-200, -300))
t.left(270)
draw_triangle_big('lightblue', (-305, -195))
draw_triangle_mini('cyan', (-335, -225))
t.left(90)
draw_triangle_mini('lightgrey', (-270, -300 ))
t.left(120)
draw_parallelogram('lightgreen', (-148, -262))
draw_triangle_midle('magenta', (-275, -225))
t.left(45)
draw_square('lightpink', (-273, -167.5))

# краб
draw_circle_big('red', (-500,-270))
draw__rectangle ('white', (-560,-72))
t.left(135)
draw_triangle_big('red',(-448.2,-231.6))
draw_circle_mini('black', (-518,-195))
draw_circle_mini('black', (-484,-195))
t.left(185)
draw_triangle_mini('darkblue',(-558,-231.6))
t.left(210)
draw_triangle_mini('darkblue',(-545,-245))

draw_triangle_mini_mirror('darkblue',(-444.4,-231.6))
t.right(30)
draw_triangle_mini_mirror('darkblue',(-454.4,-245))

draw_circle_midle('darkred', (-560,-200))
draw_circle_midle('darkred', (-440,-200))


t.right(45)
draw_square('white', (-570,-130))
t.right(45)
draw_square('white', (-427.5,-130))

t.hideturtle()
t.done()























































