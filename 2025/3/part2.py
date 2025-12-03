def readfile(file_path):
    with open(file_path, "r") as file:
        return [line.strip() for line in file.readlines()]


input = readfile("input.txt")


def max_bank_joltage(bank):
    batteries = [int(x) for x in bank]

    idx = 0
    joltage = ""
    for i in range(BAT_COUNT):
        if i < BAT_COUNT - 1:
            available = batteries[idx : -BAT_COUNT + 1 + i]
        else:
            available = batteries[idx:]
        bat = max(available)
        joltage += str(bat)
        idx = batteries.index(bat, idx) + 1

    return int(joltage)


BAT_COUNT = 12
total_joltage = 0
for bank in input:
    joltage = max_bank_joltage(bank)
    total_joltage += joltage

print(total_joltage)
