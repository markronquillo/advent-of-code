with open('input.txt') as f:
    data = [int(d) for d in f.readlines()]
    result = sum([(d // 3) - 2 for d in data])
    print(result)
