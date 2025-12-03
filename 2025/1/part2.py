def readfile(file_path):
    with open(file_path, "r") as file:
        return [line.strip() for line in file.readlines()]


class Dial:
    POSITIONS = 100  # Last position is 99

    def __init__(self, start_position):
        self.position = start_position
        self.zero_counter = 0

    def rotate(self, direction, points):
        delta = 0
        if direction == "R":
            delta = 1
        elif direction == "L":
            delta = -1

        for _ in range(points):
            self.position = (self.position + delta) % self.POSITIONS
            if self.position == 0:
                self.zero_counter += 1


data = readfile("input.txt")
dial = Dial(50)

for rotation in data:
    direction = rotation[0]
    points = int(rotation[1:])
    dial.rotate(direction, points)

print(dial.zero_counter)
