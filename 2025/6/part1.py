def readfile(file_path):
    with open(file_path, "r") as file:
        for line in file.readlines():
            if line.strip() == "":
                continue
            yield list(filter(lambda x: x != "", line.strip().split(" ")))


def transpose(matrix):
    transposed = []
    for x in range(len(matrix[0])):
        col = []
        for y in range(len(matrix)):
            col.append(matrix[y][x])
        transposed.append(col)
    return transposed


def calculate(line):
    operator = line[-1]
    numbers = map(lambda n: int(n), line[:-1])
    if operator == "+":
        return sum(numbers)
    elif operator == "*":
        result = 1
        for n in numbers:
            result *= n
        return result
    else:
        raise ValueError(f"Unknown operator: {operator}")


input = list(readfile("input.txt"))

transposed = transpose(input)
check = 0
for line in transposed:
    check += calculate(line)

print(check)
