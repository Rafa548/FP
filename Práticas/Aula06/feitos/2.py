
import turtle

def main():
    wn = turtle.TurtleScreen
    t = turtle.Turtle()
    name = input("File?")
    if not ".txt" in name:
        name = name + ".txt"
    print(...(t, name))
    

def ns(t, filename):
    with  open(filename, "r") as e:
        mm = e.read().split()
        i = 0
        while i < len(mm):
            if (mm[i] == "Up"):
                t.up
                i+=1
            if (mm[i] == "Down"):
                t.down
                i+=1
            if (mm[i].strip("-").isdigit()):
                x = int(mm[i])
                y = int(mm[i])
                t.goto(x,y)
                i += 1

turtle.Screen().exitonclick()

