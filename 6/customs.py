from functools import reduce 

with open("input.txt") as f:
    input = f.read();

groups = input.split("\n\n")
 
any_yeses = [set(answers.replace("\n", "")) for answers in groups]

print("Any Yesses Sum: {}".format(reduce(lambda a, b: a + b, [len(yes) for yes in any_yeses])))

answer_groups = [answer for answer in [group.split("\n") for group in groups]]

all_yesses = [set(answers[0]).intersection(*[set(ans) for ans in answers[1:]]) for answers in answer_groups]

print("All Yesses Sum: {}".format(reduce(lambda a, b: a + b, [len(yes) for yes in all_yesses])))