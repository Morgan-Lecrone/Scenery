"""
This program will draw a scene with either a house and two trees, or four trees depending on user input.
If the user indicates that they would like a house, the program will ask them what position they would
like the house at and what color they would like the house to be.
It then draws the scene to the user's specifications.
The trees are chosen randomly to be either pine or maple and are also a random size.

@author Morgan Lecrone
"""

import random
import turtle
import math


def trunk(trunkHeight):
    """
    This function draws a single vertical line to be the tree's trunk.

    trunkHeight: The height of the trunk of the tree.

    Preconditions: The turtle is at the base of where the tree is to be drawn facing East.
    Postconditions: The turtle is at the top of the tree facing East.
    """
    turtle.down()
    turtle.left(90)
    turtle.forward(trunkHeight)
    turtle.right(90)

def pineTree():
    """
    This function draws a pine tree.
    It has a randomly chosen trunk height and a triangle at the top with sides that are 60 percent of the trunk height.

    Preconditions: The turtle is at the bottom of where the tree is to be drawn facing East.
    Postconditions: The turtle is at the bottom of the tree facing East.
    """
    trunkHeight = random.randint(50,200)
    triangleAngle = 120
    trunk(trunkHeight)
    turtle.forward(trunkHeight*.3)
    turtle.left(triangleAngle)
    turtle.forward(trunkHeight*.6)
    turtle.left(triangleAngle)
    turtle.forward(trunkHeight*.6)
    turtle.left(triangleAngle)
    turtle.forward(trunkHeight*.3)
    turtle.right(90)
    turtle.forward(trunkHeight)
    turtle.left(90)
    return trunkHeight * 2.8

def mapleTree():
    """
    This function draws a maple tree.
    The tree's height is chosen randomly and its top is a circle with a radius that is 40 percent of the trunk height.

    Preconditions: The turtle is at the bottom of where the tree is to be drawn facing East.
    Postconditions: The turtle is at the bottom of the tree facing East.
    """
    trunkHeight = random.randint(50,150)
    trunk(trunkHeight)
    turtle.circle(trunkHeight*.4)
    turtle.right(90)
    turtle.forward(trunkHeight)
    turtle.left(90)
    return trunkHeight + (math.pi * trunkHeight * .8)

def tree():
    """
    This function randomly chooses to draw a pine or maple tree.
    It also moves the turtle spacing units forward to draw the grass.

    Preconditions: The turtle is at the base of where the tree is to be drawn facing East.
    Postconditions: The turtle is spacing units to the right of the base of the tree.
    """
    spacing = 100
    turtle.pencolor("green")
    treeType = random.randint(1,2)
    if treeType == 1:
        ink = pineTree()
    else:
        ink = mapleTree()
    turtle.forward(spacing)
    return ink + spacing

def house(houseColor):
    """
    This function draws a house with a peak roof.

    houseColor: the color of the house

    Preconditions: The turtle is at the bottom left corner of where the house is to be drawn facing East.
    Postconditions: The turtle is spacing to the right of the house.
    """
    wallHeight = 100
    wallAngle = 90
    roofAngle = 45
    spacing = 100
    turtle.pencolor(houseColor)
    turtle.forward(wallHeight)
    turtle.left(wallAngle)
    turtle.forward(wallHeight)
    turtle.left(roofAngle)
    turtle.forward(wallHeight/math.sqrt(2))
    turtle.left(wallAngle)
    turtle.forward(wallHeight/math.sqrt(2))
    turtle.left(roofAngle)
    turtle.forward(wallHeight)
    turtle.left(90)
    turtle.forward(wallHeight)
    turtle.color("green")
    turtle.forward(spacing)
    return spacing + 3 * wallHeight + (math.sqrt(2) * 2 * wallHeight)

def drawScene(isHouse, position, houseColor):
    """
    This function will draw a scene with either a house and two trees, or four trees depending on user input.

    isHouse: y if there is a house, n if there is not a house.
    position: The position of the house.  It can be 1, 2, or 3.
    houseColor: The color of the house.

    Preconditions: The turtle is at the origin, facing East.
    Postconditions: The turtle is at the origin, facing East.
    """
    offset = 250
    spacing = 100
    turtle.up()
    turtle.back(offset)
    turtle.down()
    turtle.pencolor("green")
    turtle.forward(spacing)
    ink = spacing
    if isHouse == 'n':
        ink = ink + tree()
        ink = ink + tree()
        ink = ink + tree()
        ink = ink + tree()
    else:
        if position == "1":
            ink = ink + house(houseColor)
            ink = ink + tree()
            ink = ink + tree()
        elif position == "3":
            ink = ink + tree()
            ink = ink + tree()
            ink = ink + house(houseColor)
        else:
            ink = ink + tree()
            ink = ink + house(houseColor)
            ink = ink + tree()
    turtle.back(offset)
    return ink

def main():
    """
    This function asks the user to specify what elements are in the scene.  Then, it draws the scene.
    Preconditions: The turtle is at the origin, facing East.
    Postconditions: The turtle is at the origin, facing East.
    """
    isHouse = input("Is there a house in the forest? (y/n)")
    position = "2"
    houseColor = "blue"
    if isHouse != 'n':
        position = input("At what position? (1,2,3)")
        houseColor = input("What color is the house?")
    print("We used " + str(drawScene(isHouse, position, houseColor)) + " units of ink for the drawing.")
    turtle.done()


if __name__ == '__main__':
    main()