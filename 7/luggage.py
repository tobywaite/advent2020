import re
from functools import reduce

class Bag():
    def __init__(self, input_line):

        bag_color, children_input = input_line.split(" bags contain ")

        self.color = bag_color
        self.children = dict()
        self.total_children = None

        for child in children_input.split(","):
            child_regex = r"(?P<count>\d+) (?P<color>\w+ \w+) bag"
            match = re.match(child_regex, child.strip())

            if match:
                self.children[match.groupdict()["color"]] = int(match.groupdict()["count"])
                print("{child} -- {matches}".format(child=child, matches=match.groupdict()))
        

    def child_count(self, bagLookup):
        if self.total_children:
            return self.total_children
        elif len(self.children)==0:
            return 0
        else:
            total = sum([(bagsLookup[color].child_count(bagsLookup) + 1) * count for (color, count) in self.children.items()])
            self.total_children = total
            return total
    
    def __repr__(self):
        return "{color} (total: {total}): {children}".format(color=self.color, total=self.total_children, children=self.children)


with open("input.txt") as f:
    input = [line.strip("\n") for line in f.readlines()]

bags = [Bag(line) for line in input]
bagsLookup = {bag.color: bag for bag in bags}

solution = set()
starting_bag = 'shiny gold'
possible_bags = set([starting_bag, ])

while len(possible_bags) > 0:
    possible_bag = possible_bags.pop()
    solution.add(possible_bag)

    for color in bagsLookup.keys():
        if color not in solution and possible_bag in bagsLookup[color].children:
            possible_bags.add(color);

solution.remove(starting_bag)

print("Possible bags ({})".format(len(solution)))

count = bagsLookup[starting_bag].child_count(bagsLookup);

print("Total contained bags in {}: {}".format(starting_bag, count))