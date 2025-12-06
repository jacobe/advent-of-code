import re


def readfile(file_path):
    with open(file_path, "r") as file:
        for line in file.readlines():
            line = line.strip("\n")
            if line == "":
                continue
            yield line


def transpose(matrix):
    transposed = []
    for x in range(len(matrix[0])):
        col = []
        for y in range(len(matrix)):
            col.append(matrix[y][x].strip("\n"))
        transposed.append(col)
    return transposed


class Problem:
    def __init__(self, op, column_width):
        self.op = op
        self.column_width = column_width
        self.lines = []

    @classmethod
    def from_operator_line(cls, operator_line):
        return cls(operator_line[0], len(operator_line) - 1)

    def add_line(self, line):
        self.lines.append(line)

    def calculate(self):
        cephalopod_transformed = [
            int(s)
            for s in map(lambda s: "".join(s).strip(), transpose(self.lines))
            if s != ""
        ]

        if self.op == "+":
            return sum(cephalopod_transformed)
        elif self.op == "*":
            result = 1
            for n in cephalopod_transformed:
                result *= n
            return result
        else:
            raise ValueError(f"Unknown operator: {self.op}")

    def __repr__(self) -> str:
        return f"Problem(operator={self.op}, column_width={self.column_width}"


def read_problems(operators_line):
    return list(
        map(Problem.from_operator_line, re.findall(r"[+*] *", operators_line + " "))
    )


def add_lines(problems, lines):
    for line in lines:
        idx = 0
        for problem in problems:
            n = line[idx : idx + problem.column_width + 1]
            if idx + problem.column_width < len(line) - 2:
                n = n[:-1]  # remove the space
            idx += problem.column_width + 1
            problem.add_line(n)


lines = list(readfile("input.txt"))
problems = read_problems(lines[-1])
add_lines(problems, lines[:-1])

check = 0
for problem in problems:
    check += problem.calculate()
print(check)
