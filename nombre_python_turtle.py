import turtle   # Esto es para importar la libreria turtle
import random

def random_color():
    t.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

opcion = int(input("""Ingrese el numero de la opcion que desea ver: 
1) Generacion CONTINUA del nombre con segmentos de colores ALEATORIOS
2) Generacion UNICA del nombre en negro
"""))

if opcion == 1:
    while True:
        t = turtle.Turtle() # Esto es para crear una nueva tortuga llamada "t"
        wn = turtle.Screen()    # Esto es para crear la ventana donde se va a ubicar la tortuga
        wn.title("Hello, turtle!")  # Esto es para asignarle un nombre a la ventana donde esta la tortuga
        wn.colormode(255)
        t.width(3)
        t.speed(25)

        t.hideturtle()  # Esconde la tortuga
        t.penup()       # Sube el lapicero y evita que la tortuga escriba cuando se mueva
        t.goto(-200, 0) # Mueve la tortuga hacia una ubicacion
        t.showturtle()  # Hace que la tortuga sea visible
        t.pendown()     # Baja el lapicero y hace que la tortuga escriba cuando se mueva

        # Creacion de la "J"
        t.rt(65)
        random_color()
        t.circle(-20, 180)
        random_color()
        t.circle(-40, 100)
        random_color()
        t.fd(84)
        random_color()
        t.circle(20, 240)
        random_color()
        t.fd(250)   
        random_color()
        t.circle(-26, 210)
        random_color()
        t.fd(100)

        # Creacion de la "o"
        t.circle(-120, 40)
        random_color()
        t.circle(-40, 340)
        random_color()
        t.rt(115)
        random_color()
        t.circle(35, 140)
        random_color()
        t.rt(30)
        random_color()
        # Creacion de la "s"
        t.circle(120, 45)
        random_color()
        t.rt(105)
        random_color()
        t.circle(-70, 115)
        random_color()
        t.circle(-10, 200)
        random_color()
        t.circle(300, 23)

        # Creacion de la "e"
        t.circle(50, 55)
        random_color()
        t.circle(10, 115)
        random_color()
        t.circle(100, 30)
        random_color()
        t.circle(40, 165)
        random_color()
        t.circle(400, 10)
        t.reset()

if opcion == 2:
    t = turtle.Turtle() # Esto es para crear una nueva tortuga llamada "t"
    wn = turtle.Screen()    # Esto es para crear la ventana donde se va a ubicar la tortuga
    wn.title("Hello, turtle!")  # Esto es para asignarle un nombre a la ventana donde esta la tortuga
    wn.colormode(255)
    t.width(3)
    t.speed(15)

    t.hideturtle()  # Esconde la tortuga
    t.penup()       # Sube el lapicero y evita que la tortuga escriba cuando se mueva
    t.goto(-200, 0) # Mueve la tortuga hacia una ubicacion
    t.showturtle()  # Hace que la tortuga sea visible
    t.pendown()     # Baja el lapicero y hace que la tortuga escriba cuando se mueva

    # Creacion de la "J"
    t.rt(65)
    t.circle(-20, 180)
    t.circle(-40, 100)
    t.fd(84)
    t.circle(20, 240)
    t.fd(250)   
    t.circle(-26, 210)
    t.fd(100)

    # Creacion de la "o"
    t.circle(-120, 40)
    t.circle(-40, 340)
    t.rt(115)
    t.circle(35, 140)
    t.rt(30)
    # Creacion de la "s"
    t.circle(120, 45)
    t.rt(105)
    t.circle(-70, 115)
    t.circle(-10, 200)
    t.circle(300, 23)

    # Creacion de la "e"
    t.circle(50, 55)
    t.circle(10, 115)
    t.circle(100, 30)
    t.circle(40, 165)
    t.circle(400, 10)
    
    wn.exitonclick()




