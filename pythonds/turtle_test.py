import turtle

myTurtle = turtle.Turtle()
myWin = turtle.Screen()
points = [[-200,0],[0,200],[200,0]]

def drawSpiral(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        drawSpiral(myTurtle,lineLen-5)

#drawSpiral(myTurtle,100)
def getMid(p1,p2):
    return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2)

def draw(myTurtle,points):
    
    myTurtle.up()
    myTurtle.goto(points[1])
    myTurtle.down()
   
    
    myTurtle.goto(points[1])
    myTurtle.goto(points[2])
    myTurtle.goto(points[0])
    myTurtle.goto(points[1])
    
    
        
def sierpinski(myTurtle,points,degree):

    draw(myTurtle,points)
    if degree > 0:
        sierpinski(myTurtle,[points[0],getMid(points[0],points[1]),getMid(points[0],points[2])],degree -1)
        sierpinski(myTurtle,[points[1],getMid(points[0],points[1]),getMid(points[1],points[2])],degree -1)
        sierpinski(myTurtle,[points[2],getMid(points[2],points[1]),getMid(points[0],points[2])],degree -1)
    
        
    
    
sierpinski(myTurtle,points,3)  
myWin.exitonclick()



