from aocd import get_data


input = [int(i) for i in get_data(day=1, year=2019).split('\n')]

def part1():
    return sum([mass // 3 - 2 for mass in input])

def part2():
    return sum([part2_helper(mass) for mass in input])

def part2_helper(mass: int) -> int:
    '''Recursive function to calculate fuel needs for a starting mass'''
    fuel_req = mass // 3 - 2
    if fuel_req <= 0:
        return 0
    else:
        return fuel_req + part2_helper(fuel_req)

print(f"Part 1 answer: {part1()}")
print(f"Part 2 answer: {part2()}")