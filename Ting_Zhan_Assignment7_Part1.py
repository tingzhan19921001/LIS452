import turtle

def draw_checkerboard(rotation_angle: int):

    s = turtle.Screen()  # Get the turtle's screen object (a movable window)
    s.setup(width=1500, height=1500)  # set the window size
    turtle.setheading(rotation_angle) #set the heading rotatation angle

    turtle.speed(0) #set the speed of drawing
    turtle.pensize(2) #set the size of pen
    turtle.penup() #lift pen up
    turtle.goto(-160,-160) #go to point(-160,160)
    turtle.pendown() #put pen down
    turtle.color("grey") #draw color grey

    for i in range(4):#draw the big outside square
        turtle.forward(320) #set the line as 320
        turtle.left(90) #set the angle as rgiht angle

    def square(color:str): #function that draw small squares
        turtle.begin_fill() #start filling color
        turtle.fillcolor(color) #specify what color
        for i in range(4): #small square
            turtle.forward(40) # set the line as 40
            turtle.left(90) #set the angle right
        turtle.end_fill() #end filling color

    def circlecolor(color:str):#draw circle
            turtle.begin_fill() #start filling color
            turtle.fillcolor(color) #fill color as assigned
            turtle.circle(20) #draw radius as 20
            turtle.end_fill()

    for i in range(4):# four set of 2 lines
        for j in range(8): #in each set, the first line has 8 squares
            if j %2 != 0:#in this line, odd number poistion draw white square
                square('white')
                turtle.forward(40) #after drawing, move forward by 40
            elif j %2 == 0:#even number position draw grey square
                square('grey')
                turtle.forward(40)
        turtle.backward(320) #the following four steps, move the turtle to the assigned point 
        turtle.left(90) #rotate 90 angles
        turtle.forward(40) #move forward by 40
        turtle.right(90)#rotate by 90 angles
        
        for j in range(8):#in each set, the second line has 8 squares
            if j %2 != 0: #odd number position draw grey
                square('grey')
                turtle.forward(40) 
            elif j %2 == 0:#even number position draw white
                square('white')
                turtle.forward(40)
        turtle.backward(320) #the following four steps, move the turtle to the assigned point 
        turtle.left(90) #rotate 90 angles
        turtle.forward(40)#move forward by 40
        turtle.right(90)#rotate by 90 angles

    turtle.left(90) #rotate by 90 angles
    turtle.backward(320)# move backward by 320
    turtle.right(90)#rotate by 90 angles
    turtle.forward(20)#move forward 20

    for i in range(2): #start drawing circles,the first and third
        for j in range(4):#we need to draw four cirlces
                turtle.pendown()
                circlecolor('red')#draw red color circles
                turtle.penup()
                turtle.forward(80)#after drawing move forward by 80
                
        turtle.backward(320)#move to the assigned point
        turtle.left(90) #rotate by 90 angles
        turtle.forward(80)# move forward by 80
        turtle.right(90)#rotate by 90 angles

    
    turtle.right(90)#rotate by 90 angles
    turtle.forward(120)#move forward by 120
    turtle.left(90)#rotate by 90 angles
    turtle.forward(40) #to move to second line's second square 
    
    for j in range(4):#we need four circles, the second row
        turtle.pendown()
        circlecolor('red')#draw red circles
        turtle.penup()
        turtle.forward(80)
        
    turtle.backward(320)#move backward by 320
    turtle.left(90)#rotate by 90 angles
    turtle.forward(160)#move forward by 160
    turtle.right(90)#rotate by 90 angles
    
    for i in range(2):#draw 6th and 8th row
        for j in range(4):#draw 4 circles in a row
                turtle.pendown()
                circlecolor('black')#draw black circle
                turtle.penup()
                turtle.forward(80)
                
        turtle.backward(320)#move backward by 320
        turtle.left(90)#rotate by 90 angles
        turtle.forward(80)
        turtle.right(90)#rotate by 90 angles

    turtle.backward(40)#move backward by 40
    turtle.right(90)#rotate by 90 angles
    turtle.forward(120)#move forward by 120
    turtle.left(90)#rotate by 90 angles
    
    for j in range(4):#the 7th row
        turtle.pendown()
        circlecolor('black')#draw black circle
        turtle.penup()
        turtle.forward(80)#move forkward by 80

draw_checkerboard(60)



