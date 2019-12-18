def calc(value):
    fuel = (value // 3) - 2
    if fuel <= 0:
        return 0
    return fuel + calc(fuel)


with open('input.txt') as f:
    data = [int(d) for d in f.readlines()]
    result = sum([calc(d) for d in data])
    print(result)
