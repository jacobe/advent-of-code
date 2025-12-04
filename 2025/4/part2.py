def readfile(file_path):
    with open(file_path, "r") as file:
        return [list(line.strip()) for line in file.readlines()]


input = readfile("input.txt")


def remove_rolls():
    removed = 0
    for y in range(len(input)):
        line = input[y]
        for x in range(len(line)):
            c = line[x]
            if c != "@":
                continue

            adjacent = []

            def add(dx, dy):
                nx = x + dx
                ny = y + dy
                if 0 <= nx < len(line) and 0 <= ny < len(input):
                    c = input[ny][nx]
                    if c == "@":
                        adjacent.append(c)

            # top line
            add(0, -1)
            add(-1, -1)
            add(1, -1)

            # same line
            add(-1, 0)
            add(1, 0)

            # bottom line
            add(0, 1)
            add(-1, 1)
            add(1, 1)

            if len(adjacent) < 4:
                input[y][x] = "x"
                removed += 1

    for y in range(len(input)):
        for x in range(len(input[y])):
            if input[y][x] == "x":
                input[y][x] = "."

    return removed


total_removed = 0
while True:
    removed = remove_rolls()
    if removed == 0:
        break
    total_removed += removed
print(total_removed)
