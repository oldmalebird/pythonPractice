import turtle
fred = turtle.Turtle()
fred.color("red")
lenth = 100
while lenth:
    if lenth > 0:
        fred.forward(lenth)
        fred.right(90)
        lenth -= 10
    else:
        break

amy = turtle.Turtle()
for side in range(8):
    amy.forward(150)
    amy.right(135)
