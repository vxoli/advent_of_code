import re

class Solver(int):
    def __mul__(self, inp):
        return Solver(int(self) + inp)
    def __add__(self, inp):
        return Solver(int(self) + inp)
    def __sub__(self, inp):
        return Solver(int(self) * inp)

def evaluate1(expression):
    expression = re.sub(r"(\d+)", r"Solver(\1)", expression)
    expression = expression.replace("*", "-")
    return eval(expression, {}, {"Solver": Solver})

def evaluate2(expr):
    expr = re.sub(r"(\d+)", r"Solver(\1)", expr)
    expr = expr.replace("*", "-")
    expr = expr.replace("+", "*")
    return eval(expr, {}, {"Solver": Solver})

with open("d18-input.txt") as fp:
    lines = [line.split("\n")[0] for line in fp.readlines()]
print("Part 1:", sum(evaluate1(l) for l in lines))
print("Part 2:", sum(evaluate2(l) for l in lines))