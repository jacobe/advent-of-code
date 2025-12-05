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
    return sorted(fresh, key=lambda r: r.start)


def count_fresh(fresh):
    count = 0
    max_p = 0
    for rng in fresh:
        if rng.start < max_p:
            rng = range(max_p, rng.stop)
        count += len(rng)
        max_p = max(max_p, rng.stop)
    return count


input = readfile("input.txt")
fresh = read_fresh(input)
count = count_fresh(fresh)
print(count)
