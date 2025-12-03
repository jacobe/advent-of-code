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
        is_invalid = False
        for seq_len in range(len(s) // 2, 0, -1):
            if len(s) % seq_len != 0:
                continue

            parts = [s[j : j + seq_len] for j in range(0, len(s), seq_len)]
            if all(p == parts[0] for p in parts):
                is_invalid = True
                break

        if is_invalid:
            invalid_id_sum += i

print(invalid_id_sum)
