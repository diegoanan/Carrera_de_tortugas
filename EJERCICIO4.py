import turtle
import random
#inicializa la variable de numero de tortugas con rango random
n = random.randint(5,30)
#hace un arreglo de n tortugas
t = [turtle.Turtle() for i in range (n)]

can = turtle.Screen()

can.colormode(255)
#posicion inicial de la tortuga
y = 400
for i in t:
    i.speed("fast")
    i.shape("turtle")
    #color random
    i.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    #envia a una posicion X y Y a la tortuga t[i]
    i.goto(-600,y) 
    i.sety(y)
    y -= 20

#inicia la carrera con un rango random
for itera in range (random.randint(20,300)):
    for i in t:
        i.forward(random.randint(1,10))
    
