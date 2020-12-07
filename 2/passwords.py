def parse(line):
    policy, password = line.split(":")
    reps, policyChar = policy.split()
    minReps, maxReps = map(int, reps.split("-"))

    return minReps, maxReps, policyChar, password.strip()

def checkPolicy1(minReps, maxReps, policyChar, password):
    charcount = 0
    for c in password:
        if c == policyChar:
            charcount+=1
    return ((charcount >= minReps) and (charcount <= maxReps))

def checkPolicy2(firstChar, secondChar, policyChar, password):
    if len(password) >= secondChar:
        return 1 == len(list(filter(lambda x: x==policyChar, [password[firstChar-1], password[secondChar-1]])))
    return False

with open("input.txt") as f:
    input = f.readlines()

pol1count = 0
pol2count = 0

for line in input:
    # example: 2-5 c: xczcczc
    print("line: " + line)
    if checkPolicy1(*parse(line)):
        pol1count += 1
    if checkPolicy2(*parse(line)):
        pol2count += 1

print("policy1 matching passwords: {ct}".format(ct=pol1count))
print("policy 2 matching passwords: {ct}".format(ct=pol2count))

