def readfile(file_path):
    with open(file_path, "r") as file:
        return [line.strip() for line in file.readlines()]


input = readfile("input.txt")

total_joltage = 0
for bank in input:
    batteries = [int(x) for x in bank]

    bat1 = max(b for b in batteries[:-1])
    bat1_idx = batteries[:-1].index(bat1)
    bat2 = max(b for b in batteries[bat1_idx + 1 :])

    joltage = int(f"{bat1}{bat2}")
    total_joltage += joltage

print(total_joltage)
