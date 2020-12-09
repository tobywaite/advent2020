infile, windowsize = "input.txt", 25

with open(infile) as f:
    input = [int(line.strip("\n")) for line in f.readlines()]

# part 1

window = input[:windowsize]
for idx, value in enumerate(input[windowsize:]):
    window = input[idx:windowsize+idx]
    valid = False
    for num in window:
        if (value - num) in window:
            valid = True
            print("At {idx}, {value} = {num1} + {num2}".format(idx=idx, value=value, num1=num, num2=value-num))
            break

    if not valid:
        invalidValue = value
        print("At {idx}, {value} is not valid".format(idx=idx, value=value))
        break

# part 2

for checkLength in range(2, len(input)):
    for start in range(len(input)-checkLength):
        checkRange = input[start:start+checkLength]
        if sum(checkRange) == invalidValue:
            print("invalidValue = sum({}), at {}".format(checkRange, idx))
            print("Solution: {}".format(max(checkRange) + min(checkRange)))