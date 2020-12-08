import re
from functools import reduce

class Bag():
    def __init__(self, input_line):

        def parse(line):
            bag_pattern = r"(?P<color>\w+ \w+) bags contain (?P<children_string>.*)\."
            child_pattern= r"(?P<count>\d+) (?P<color>\w+ \w+) bags?"
            
            bag_color, children_string = re.match(bag_pattern, line).groups()
            children = [(int(count), color) for (count, color) in re.findall(child_pattern, children_string)]

            return bag_color, children

        self.color, self.children = parse(input_line)
        self.count = None

    def __repr__(self):
        return "{color} (total: {total}): {children}".format(color=self.color, total=self.total_children, children=self.children)
    
    def countBags(self, bagGraph):
        if len(self.children) == 0:
            return 0
        else:
            if self.count:
                return self.count
            self.count = sum([count * (1 + bagGraph[child].countBags(bagGraph)) for (count, child) in self.children])
            return self.count
        

with open("input.txt") as f:
    input = [line.strip("\n") for line in f.readlines()]

bags = [Bag(line) for line in input]
graph = {bag.color: bag for bag in bags}

starting_bag = 'shiny gold'

solution1 = set()
possible_bags = set([starting_bag, ])

while len(possible_bags) > 0:
    possible_bag = possible_bags.pop()
    solution1.add(possible_bag)

    for bag in graph:
        if bag not in solution1 and possible_bag in [color for (count, color) in graph[bag].children]:
            possible_bags.add(bag);

solution1.remove(starting_bag)

print("Possible bags ({})".format(len(solution1)))

solution2 = graph[starting_bag].countBags(graph);

print("Total contained bags in {}: {}".format(starting_bag, solution2))