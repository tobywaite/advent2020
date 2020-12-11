import argparse

class Solution():
    def __init__(self, problemNumber=None):
        self.problemNumber = problemNumber or 1

        parser = argparse.ArgumentParser()
        parser.add_argument("--input", default="input.txt")
        arguments = parser.parse_args()

        self.input = self.parseInput(arguments.input)

        self.setup()

    def setup(self):
        pass

    def parseInput(self, inputFile):
        with open("{}/{}".format(self.problemNumber, inputFile)) as f:
            inputLines = [self.inputTransform(line) for line in f.readlines()]

        return inputLines

    def inputTransform(self, inputLine):
        return inputLine.strip("\n")

    def run(self):
        solution1 = self.solution1()
        if solution1:
            print("Solution 1: {}".format(solution1))

        solution2 = self.solution2()
        if solution2:
            print("Solution 2: {}".format(solution2))

    def solution1():
        pass

    def solution1():
        pass