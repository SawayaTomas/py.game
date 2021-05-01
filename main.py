import turtle
import time 
import random

posponer = 0.1

#marcador
score = 0 
high_score = 0


#Configuracion de la ventana
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("#000")
wn.setup(width=600, height = 600)
wn.tracer(0) #Hace mejor las animaciones 

#Cabeza serpiente
cabeza = turtle.Turtle()
cabeza.speed(0) #con esto el dibujo ya esta aca
cabeza.shape("square") #con
cabeza.penup() #esto cambias la forma (forma cuadrado)
cabeza.goto(0,0)
cabeza.direction = "stop"
cabeza.color("#43D096")

#Comida
comida = turtle.Turtle()
comida.speed(0) #con esto el dibujo ya esta aca
comida.shape("circle") #con esto cambias la forma (forma cuadrado)
comida.penup()
comida.goto(0,100)
comida.color("white")

# Segmentos / Cuerpo de la serpiente

segmentos = [] #Asi creo una lista

#Texto

texto = turtle.Turtle()
texto.speed(0)
texto.color("#43D096")
texto.penup()
texto.hideturtle()
texto.goto(0,200)
texto.write("Score: 0          High Score: 0", align = "center", font = ("Courier", 20, "normal"))

#Funciones

def arriba():
	cabeza.direction = "up"

def abajo():
	cabeza.direction = "down"

def izquierda():
	cabeza.direction = "left"

def derecha():
	cabeza.direction = "right"

def mov():
	if cabeza.direction == "up":
		y = cabeza.ycor()
		cabeza.sety(y + 20)

	if cabeza.direction == "down":
		y = cabeza.ycor()
		cabeza.sety(y - 20)

	if cabeza.direction == "left":
		x = cabeza.xcor()
		cabeza.setx(x - 20)

	if cabeza.direction == "right":
		x = cabeza.xcor()
		cabeza.setx(x + 20)

#Teclado

wn.listen()
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(izquierda, "Left")
wn.onkeypress(derecha, "Right")


while True:
	wn.update()

	#Colisiones bordes
	if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280:
		time.sleep(1)
		cabeza.goto(0,0)
		cabeza.direction = "stop"

		#esconder los segmentos
		for segmento in segmentos:
			segmento.goto(10000,10000)

		#limpiar lista de segmentos
		segmentos.clear()

		#resetear marcador
		score = 0 
		texto.clear()
		texto.write("Score: {}		High Score: {}".format(score, high_score), 
			align = "center", font = ("Courier", 20, "normal"))

	if cabeza.distance(comida) < 25:
		x = random.randint(-280,280)
		y = random.randint(-280,280)
		comida.goto(x,y)

		nuevo_segmento = turtle.Turtle()
		nuevo_segmento.speed(0) #con esto el dibujo ya esta aca
		nuevo_segmento.shape("square") #con
		nuevo_segmento.penup() #esto cambias la forma (forma cuadrado)
		nuevo_segmento.goto(0,0)
		nuevo_segmento.color("#7CF5C4")
		segmentos.append(nuevo_segmento) #Asi se agregan cosas a las listas

		#Aumentar marcador
		score += 10

		if score > high_score:
			high_score = score

		texto.clear()
		texto.write("Score: {}          High Score: {}".format(score, high_score), 
			align = "center", font = ("Courier", 20, "normal"))

	totalSeg = len(segmentos)
	for index in range(totalSeg -1, 0, -1):
		x = segmentos[index - 1].xcor()
		y = segmentos[index - 1].ycor()
		segmentos[index].goto(x,y)



	if totalSeg > 0:
		x = cabeza.xcor()
		y = cabeza.ycor()
		segmentos[0].goto(x,y)

	mov()
	time.sleep(posponer)

wn.mainloop()