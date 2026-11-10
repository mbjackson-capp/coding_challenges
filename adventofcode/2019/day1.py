from aocd import get_data

from myutils import apply_then_combine

input = [int(i) for i in get_data(day=1, year=2019).split('\n')]

def part2_helper(mass: int) -> int:
    '''Recursive function to calculate fuel needs for a starting mass'''
    fuel_req = mass // 3 - 2
    if fuel_req <= 0:
        return 0
    else:
        return fuel_req + part2_helper(fuel_req)

if __name__ == '__main__':
    print(f"Part 1 answer: {apply_then_combine(input, lambda mass: mass // 3 - 2)}")
    print(f"Part 2 answer: {apply_then_combine(input, part2_helper)}")