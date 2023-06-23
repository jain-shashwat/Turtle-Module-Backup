from turtle import Turtle, getscreen

vro = Turtle()
print(vro)
vro.shape("turtle")
vro.color("DarkRed")
my_screen = getscreen()

vro.forward(100)
vro.left(90)
vro.forward(100)
vro.left(90)
vro.forward(100)
vro.left(90)
vro.forward(100)
vro.left(90)


print(my_screen.canvheight)
my_screen.exitonclick()













# from prettytable import PrettyTable
#
# table = PrettyTable()
#
# table.add_column("Pokemon Name",["Adelaide","Brisbane","Darwin","Hobart","Sydney","Melbourne","Perth"])
# table.add_column("Type",["aide","sbane","win","art","ney","bourne","erth"])
# table.align = "l"
# table.header= True
#
#
#
# print(table)