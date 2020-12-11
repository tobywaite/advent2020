from collections import Counter

class AdapterChain():
    def __init__(self, adapters):
        self.adapters = adapters
        # memo dictionary for efficiently calculating valid chains. 
        # Initialized with "1", to represent the chain that starting from the "final adapter".
        self.memo = {adapters[-1]: 1} 

    def countValidBranches(self, index=0):
        # From this node, the next valid nodes are those with values up to 3 greater than the current value.
        currentValue = self.adapters[index]
        numBranches = sum(map(lambda value: value > currentValue and value <= currentValue + 3, self.adapters))

        # if the value for this node hasn't already been computed, calculate the value 
        if currentValue not in self.memo:
            # Sum the number of paths for each subsequent valid branch and memoize the result
            self.memo[currentValue] = sum([self.countValidBranches(idx) for idx in range(index+1, index+numBranches+1)])

        return self.memo.get(currentValue)
        

with open("input.txt") as f:
    inputValues = sorted([int(adapter.strip("\n")) for adapter in f.readlines()])

initialValue = 0
terminalValue = inputValues[-1] + 3
adapters = [initialValue] + inputValues + [terminalValue] # Add the 'initial adapter' & 'final adapter' values to the list

# Problem 1: Find distribution of differences between subsequent adapter values
diffs = [(adapters[idx+1] - val) for idx, val in enumerate(adapters[:-1])]

distribution = Counter(diffs)
solution1 = distribution[1] * distribution[3]
print("Solution 1: {}".format(solution1))

# problem 2: count the number of valid adapter chains
solution2 = AdapterChain(adapters).countValidBranches()
print("Solution 2: {}".format(solution2))