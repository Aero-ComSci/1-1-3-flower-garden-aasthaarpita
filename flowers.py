import turtle as trtl

painter = trtl.Turtle()
screen = trtl.Screen()
screen.bgcolor("#87CEEB")
painter.speed(0)

#function to draw a sunflower
def sunflower():
    painter.color("yellow")
    #petals of sunflower
    for i in range(9):
        painter.penup()
        painter.forward(100)
        painter.pendown()
        painter.dot(60)
        painter.penup()
        painter.backward(100)
        painter.left(40)
    #center of sunflower
    painter.color("brown")
    painter.dot(140)
    painter.penup()

#function to draw a tulip
def tulip():
    painter.pendown()
    painter.fillcolor("pink")
    painter.begin_fill()
    #first petl
    painter.circle(120, 100)
    painter.left(80)
    painter.circle(120, 100)
    painter.end_fill()
    painter.penup()
    painter.setheading(90)
    painter.forward(70)
    painter.right(90)
    painter.forward(10)
    painter.pendown()
    painter.begin_fill()
    painter.left(125)
    #second petal
    painter.circle(120, 60)
    painter.left(85)
    painter.circle(120, 90)
    painter.end_fill()
    painter.penup()
    painter.begin_fill()
    painter.setheading(90)
    painter.forward(89)
    painter.right(90)
    painter.forward(25)
    painter.left(90)
    painter.pendown()
    #third petal
    painter.circle(60, 75)
    painter.left(45)
    painter.circle(60, 75)
    painter.end_fill()

#function to draw a rose
def rose():
    painter.pendown()
    painter.fillcolor("red")
    painter.begin_fill()
    painter.circle(100)
    painter.end_fill()
    painter.left(90)
    painter.penup()
    painter.forward(100)
    painter.pendown()
    painter.pencolor("black")
    #rose spirals
    for i in range(120):
        painter.forward(i * 0.5)
        painter.left(35)

#function to draw a pipsissewa
def pipsissewa():
    #petals
    for i in range(6):
        painter.penup()
        painter.setheading(i * 60)
        painter.pendown()
        painter.fillcolor("white")
        painter.begin_fill()
        painter.circle(50)
        painter.end_fill()
    painter.penup()
    painter.setheading(180)
    painter.forward(20)
    painter.setheading(270)
    painter.pendown()
    painter.fillcolor("pink")
    painter.begin_fill()
    #center of pipsissewa
    painter.circle(25)
    painter.end_fill()

#function to draw a daisy
def daisy():
    #12 petals
    for i in range(12):
        painter.color("white")
        painter.begin_fill()
        painter.circle(100, 60)
        painter.left(120)
        painter.circle(100, 60)
        painter.left(120)
        painter.end_fill()
        painter.left(30)
    painter.penup()
    painter.setheading(180)
    painter.forward(17)
    painter.setheading(270)
    painter.forward(2)
    painter.pendown()
    painter.color("yellow")
    #center of daisy
    painter.begin_fill()
    painter.circle(20)
    painter.end_fill()

#list of flower names
flowers = ["pipsissewas", "roses", "tulips", "sunflowers", "daisies"]

#to keep it running 
while True:
    prompt = input(
        "Welcome to Big n' Bold Flowers! Choose a flower to draw from our exclusive selection of pipsissewas, roses, tulips, sunflowers, and daisies: "
    ).lower()
    x = prompt.split()
    #if they don't want the code to stop, the turtle will draw the flowers they want
    stop = input("Do you want to stop? (y/n)")
    if stop == "y":
        break
    else:
        for n in range(len(x)):
            if x[n].isnumeric():
                #if they want to draw a rose
                if x[n + 1] == "roses" or x[n + 1] == "rose":
                    painter.penup()
                    painter.goto(-225, -100)
                    #how many roses they want
                    for i in range(int(x[n])):
                        rose()
                        painter.penup()
                        painter.setheading(270)
                        painter.forward(25)
                        painter.setheading(0)
                        painter.forward(300)
                #if they want to draw a sunflower
                elif x[n + 1] == "sunflowers" or x[n + 1] == "sunflower":
                    painter.penup()
                    painter.goto(-225, 245)
                    #how many sunflowers they want
                    for i in range(int(x[n])):
                        sunflower()
                        painter.setheading(0)
                        painter.penup()
                        painter.forward(225)
                #if they want to draw a tulip
                elif x[n + 1] == "tulips" or x[n + 1] == "tulip":
                    painter.penup()
                    painter.goto(-225, -300)
                    #how many tulips they want
                    for i in range(int(x[n])):
                        tulip()
                        painter.penup()
                        painter.setheading(270)
                        painter.forward(75)
                        painter.setheading(0)
                        painter.forward(250)
                #if they want to draw a daises
                elif x[n + 1] == "daisies" or x[n + 1] == "daisy":
                    painter.penup()
                    painter.goto(-120, -125)
                    #how many daisies they want
                    for i in range(int(x[n])):
                        daisy()
                        painter.setheading(0)
                        painter.penup()
                        painter.forward(200)
                #if they want to draw a pipsissewa
                elif x[n + 1] == "pipsissewas" or x[n + 1] == "pipsissewa":
                    painter.penup()
                    painter.goto(-120, 125)
                    #how many pipsissewas they want
                    for i in range(int(x[n])):
                        pipsissewa()
                        painter.setheading(0)
                        painter.penup()
                        painter.forward(200)

                #if they want to draw a flower that is not in the list
                else:
                    print(
                        "Sorry, we don't have that type of flower. Please enter pipsissewas, roses, tulips, sunflowers, or daisies."
                    )

wn = trtl.Screen()
wn.mainloop()
