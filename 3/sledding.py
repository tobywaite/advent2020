import ipdb
from copy import deepcopy

class SleddingMap:
    def __init__(self, input):
        rawInput = [row.strip("/n") for row in input]
        self.width = len(rawInput[0]) - 1
        self.height = len(rawInput)
        self.lookupArray = [[val for val in row.strip("\n")] for row in input]
        self.result = deepcopy(self.lookupArray)

    def lookup(self, x,y):
        realX = x % self.width
        value = self.lookupArray[y][realX]
        print("{x}, {y} => {val}".format(x=x, y=y, val=value))
        return value

    def run(self, xStep=3, yStep=1):
        xPosition = 0
        yPosition = 0

        collisions = 0

        while yPosition+1 < self.height:
            yPosition += yStep
            xPosition += xStep

            if self.lookup(xPosition, yPosition) == "#":
                collisions += 1
                self.result[yPosition][xPosition % self.width] = "X"
            else:
                self.result[yPosition][xPosition % self.width] = "O"

        return collisions

with open("input.txt") as f:
    input = f.readlines();

sledding = SleddingMap(input)

print("Collisions: {c}".format(c=sledding.run()))

print("Part 2: {c}".format(c=(sledding.run(1,1) * sledding.run(3,1) * sledding.run(5,1) * sledding.run(7,1) * sledding.run(1,2))))
