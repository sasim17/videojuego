import turtle 
import time 

ventana = turtle.Screen()
ventana.title ("bola")
ventana.bgcolor("green")
ventana.setup(width=600, height=600)
ventana.tracer(0) 

jugador = turtle.Turtle()
jugador.shape("square")
jugador.color("red")
jugador.shapesize(stretch_wid=1, stretch_len=5)
jugador.penup()
jugador.goto(0,-250)

pelota = turtle.Turtle()
pelota.shape("circle")
pelota.color("white")
pelota.penup()
pelota.goto(0,0)
pelota.dx = 4
pelota.dy = -4

puntuacion = 0

mensaje = turtle.Turtle()
mensaje.color("purple")
mensaje.penup()
mensaje.speed(0)
mensaje.goto(0,0)
mensaje.hideturtle()

texto = turtle.Turtle
texto.color("green")
texto.penup()
texto.speed(0)
texto.goto(0,260)
texto.hideturtle()
texto.write("puntos: 0", align="center", font=("courier",24,"normal"))

def mover_izquierda():
    x = jugador.xcor()
    if x > -240:
        jugador.setx(x - 40)

def mover_derecha():
    x = jugador.xcor()
    if x < 240:
        jugador.setx(x + 40)

ventana.listen()
ventana.onkeypress(mover_izquierda, "left")
ventana.onkeypress(mover_derecha, "right")

while True: 
    ventana.update()
    time.sleep(0.01)

    pelota.setx(pelota.xcor()+pelota.dx)
    pelota.sety(pelota.ycor()+pelota.dy)
    
    if pelota.xcor()>290 or pelota.xcor()<-290:
        pelota.dx *= -1 

    if pelota.ycor()>290:
        pelota.dy *= -1

    if (pelota.ycor()< -235 and pelota.ycor() >-245) and (pelota.xcor()< jugador.xcor()+ 55 and pelota.xcor()> jugador.xcor()-55):
        pelota.sety(.235)
        pelota.dy *=-1
        puntuacion +=1
        texto.clear()
        texto.write(f"puntos: {puntuacion}", align="center", font=("arial", 40,"bold"))

    if pelota.ycor()  <-290:
        mensaje.write("perdiste", align="center", font=("arial",40,"bold"))
        ventana.update()

        time.sleep(5)

        mensaje.clear()
        pelota.goto(0,0)
        pelota.dy *= -1
        puntuacion=0
        texto.clear()
        texto.write("puntos: 0", align="center", font=("courier",24,"normal"))  


    


