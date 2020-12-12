from advent.solution import Solution
from copy import deepcopy, copy


class Seating(Solution):
    def setup(self):
        pass

    def inputTransform(self, line): 
        return list(line.strip("\n"))

    def converge(self, state):
        while True:
            nextState = copy(state)
            for seat in state.seats:
                nextState.setSeat(seat, state.updateSeat(seat))

            if state == nextState:
                return nextState
            state = copy(nextState)

    def solution1(self):
        finalSeating = self.converge(SeatingMap(self.input, 4, "immediate"))
        return finalSeating.occupiedSeats()

    def solution2(self):
        finalSeating = self.converge(SeatingMap(self.input, 5, "sight"))
        return finalSeating.occupiedSeats()


class SeatingMap():
    def __init__(self, inputMap, maxOccupancy, adjecencyMode):
        self.map = deepcopy(inputMap)
        self.depth = len(inputMap)
        self.width = len(inputMap[0])
        self.seats = [(x,y) for y in range(self.depth) for x in range(self.width)]

        self.maxOccupancy = maxOccupancy
        self.adjecencyMode = adjecencyMode

    def __copy__(self):
        return SeatingMap(self.map, self.maxOccupancy, self.adjecencyMode)
    
    def __repr__(self):
        return "Seating Map: \n" + "\n".join(["".join(row) for row in self.map])

    def __eq__(self, other):
        if self.depth != other.depth or self.width != other.width:
            return False
        return all([self.getSeat(seat) == other.getSeat(seat) for seat in self.seats])

    def getSeat(self, seat):
        x, y = seat
        return self.map[y][x]

    def setSeat(self, seat, nextValue):
        x, y = seat
        self.map[y][x] = nextValue

    def occupancy(self, seat):
        x, y = seat
        x_range = range(max(x-1, 0), min(x+1, self.width-1)+1)
        y_range = range(max(y-1, 0), min(y+1, self.depth-1)+1)
        adjecentSeats = [(x, y) for x in x_range for y in y_range]
        adjecentSeats.remove((x,y)) # A seat can't be adjecent to itself!

        if self.adjecencyMode == "immediate":
            visibleSeats = adjecentSeats
        elif self.adjecencyMode == "sight":
            visibleSeats = []
            for adj_x, adj_y in adjecentSeats:
                x_step = adj_x - x
                y_step = adj_y - y
                steps = 0
                visible_x = adj_x
                visible_y = adj_y

                while visible_x >= 0 and visible_x < self.width and visible_y >= 0 and visible_y < self.depth:
                    currentSeat = (visible_x, visible_y)
                    currentValue = self.getSeat(currentSeat)
                    if currentValue != ".":
                        visibleSeats.append(currentSeat)
                        break

                    steps += 1
                    visible_x = adj_x + steps * x_step
                    visible_y = adj_y + steps * y_step

        return sum([self.getSeat(seat)=="#" for seat in visibleSeats]) # count occupied seats in immediately adjecent set

    def updateSeat(self, seat):
        seatValue = self.getSeat(seat)
        occupancy = self.occupancy(seat)
        if seatValue == "#" and occupancy >= self.maxOccupancy:
                return "L"
        elif seatValue == "L" and occupancy == 0:
            return "#"
        else:
            return seatValue

    def occupiedSeats(self):
        return sum([self.getSeat(seat) == "#" for seat in self.seats])


solution = Seating(problemNumber=11)
solution.run()