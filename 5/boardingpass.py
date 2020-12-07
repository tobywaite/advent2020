import ipdb

with open("input.txt") as f:
    input = [val.strip("\n") for val in f.readlines()]

maxseatID = 0
seats = []
for val in input:
    replaced = val.replace("F", "0").replace("B", "1").replace("L", "0").replace("R","1")
    rowID = replaced[:7]
    colID = replaced[7:]
    row, col = int(rowID,2), int(colID,2)

    seatID = row * 8 + col
    if seatID > maxseatID:
        maxseatID = seatID
    
    seats.append(seatID)

print("max seat: {}".format(maxseatID))

seats.sort()

for idx, seat in enumerate(seats[:-1]):
    if seats[idx+1] != seat+1:
        print("Your seat is {}".format(seat+1))