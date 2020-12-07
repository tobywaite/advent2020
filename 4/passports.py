import ipdb
import re

def parsePassport(inputLine):
    # input lines are split by new lines and spaces, so we need to jump through some hoops to parse each input.
    spaceTokens = inputLine.split(" ")
    newLineTokens = [token.split("\n") for token in spaceTokens]
    kvPairs = [item.split(":") for sublist in newLineTokens for item in sublist]
    return {k: v for k, v in kvPairs}

def validate(passport):
    hcl_re = re.compile("#[0-9a-f]{6,}")
    def hgt_rule(hgt):
        num = hgt[:-2]
        units = hgt[-2:]

        if units == "cm":
             return int(num) >=150 and int(num) <= 193
        elif units == "in":
            return int(num) >=59 and int(num) <= 76
        else:
            return False

    rules = [
        {
            "key": 'byr',
            "rule": lambda year: int(year) >= 1920 and int(year)<=2002,
        }, 
       {
            "key": 'iyr',
            "rule": lambda year: int(year) >= 2010 and int(year)<=2020,
        }, 
        {
            "key": 'eyr',
            "rule": lambda year: int(year) >= 2020 and int(year)<=2030,
        }, 
        {
            "key": 'hgt',
            "rule": hgt_rule,
        }, 
        {
            "key": 'hcl',
            "rule": lambda value: hcl_re.match(value),
        }, 
        {
            "key": 'ecl',
            "rule": lambda value: value in ('amb', 'blu', 'brn', 'gry', 'hzl', 'grn', 'oth'),
        }, 
        {
            "key": 'pid',
            "rule": lambda value: len(value) == 9 and int(value),
        } 
    ]

    for rule in rules:
        try:
            if rule["rule"](passport.pop(rule["key"])):
                continue
            else:
                return False
        except:
            return False

    return True


with open("input.txt") as f:
    input = f.read(); 

passportLines = input.split("\n\n")

passports = [parsePassport(line) for line in passportLines]

validPassports = list(filter(validate, passports))

print("Valid Passports: {}".format(len(validPassports)))