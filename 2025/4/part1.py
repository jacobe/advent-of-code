def readfile(file_path):
    with open(file_path, "r") as file:
        return [line.strip() for line in file.readlines()]


input = readfile("input.txt")
accessible_roll_count = 0

for y in range(len(input)):
    line = input[y]
    for x in range(len(line)):
        c = line[x]
        if c == ".":
            continue

        adjacent = []

        def add(dx, dy):
            nx = x + dx
            ny = y + dy
            if 0 <= nx < len(line) and 0 <= ny < len(input):
                c = input[ny][nx]
                if c != ".":
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
            accessible_roll_count += 1

print(accessible_roll_count)
