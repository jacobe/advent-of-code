def readfile(file_path):
    with open(file_path, "r") as file:
        return [line.strip() for line in file.readlines()]


input = readfile("input.txt")
input = input[0].split(",")
input = [(x, y) for x, y in (pair.split("-") for pair in input)]

invalid_id_sum = 0
for rng in input:
    for i in range(int(rng[0]), int(rng[1]) + 1):
        s = str(i)
        if len(s) % 2 != 0:
            continue

        mid = len(s) // 2
        first_half = s[:mid]
        second_half = s[mid:]

        if first_half == second_half:
            invalid_id_sum += i


print(invalid_id_sum)
