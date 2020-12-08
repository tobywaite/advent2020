class Instruction():
    def __init__(self, line=None, operation=None, value=None):
        if line:
            operation, value = line.strip("\n").split(" ");
            
        self.operation = operation 
        self.value = int(value)

    def __repr__(self):
        repr = "{} {}".format(self.operation, self.value)
        return repr

    def execute(self):
        op, val = self.operation, self.value

        if op == "nop":
            return 1, 0
        elif op == "acc":
            return 1, val
        elif op == "jmp":
            return val, 0


class InfiniteLoopException(Exception):
    pass


def run(instructions, idx=0, acc=0, visited=None):
    if not visited:
        visited = set()

    if idx >= len(instructions):
        return acc

    print("{}: {} | acc: {}".format(idx, instructions[idx], acc))

    step, addend = instructions[idx].execute()
    
    if idx in visited:
        raise InfiniteLoopException("Loop detected with final value {}".format(acc), acc)
    else:
        visited.add(idx)

    return run(instructions, idx + step, acc+addend, visited)

def fix(instructions):
    for idx, instruction in enumerate(instructions):
        next_op = instruction.operation
        if next_op == "nop":
            next_op = "jmp"
        elif next_op == "jmp":
            next_op = "nop"

        instructions[idx] = Instruction(operation=next_op, value=instruction.value) 

        try:
            return run(instructions)
        except InfiniteLoopException: 
            print("{}: failed run w/ {}".format(idx, instruction))
            # swap back
            instructions[idx] = instruction

    raise Exception("No swap found")


with open("input.txt") as f:
    instructions = [Instruction(line=line) for line in f.readlines()]

print(instructions)

# problem 1 will fail to execute, because it will hit a loop. 
# print the final accumulator value
try: 
    run(instructions)
except InfiniteLoopException as err:
    print("Final acc value for given input: {}".format(err.args[1]))

final_value = fix(instructions)

print("Final acc value for fixed input: {}".format(final_value))