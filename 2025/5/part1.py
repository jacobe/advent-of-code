def readfile(file_path):
    with open(file_path, "r") as file:
        for line in file.readlines():
            yield line.strip()


def read_fresh(input):
    fresh = []
    for line in input:
        if line == "":
            break
        start, stop = map(int, line.split("-"))
        fresh.append(range(start, stop + 1))
    return fresh


def count_fresh(fresh, input):
    count = 0
    for line in input:
        ingredient = int(line)
        for rng in fresh:
            if ingredient in rng:
                count += 1
                break
    return count


input = readfile("input.txt")
fresh = read_fresh(input)
count = count_fresh(fresh, input)
print(count)
