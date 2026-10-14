from aocd import get_data

 
input = get_data(day=1, year=2022).split('\n')

def calories_totals():
    '''Sum up the total calories in each elf's pack'''
    elves = []
    curr_elf = 0
    for item in input:
        if item != '':
            curr_elf += int(item)
        else:
            elves.append(curr_elf)
            curr_elf = 0
    
    return elves

def part1():
    elves = calories_totals()
    return max(elves)

def part2():
    elves = calories_totals()
    elves.sort(reverse=True)
    return sum(elves[0:3])


if __name__ == '__main__':
    print(f"Answer for part 1 is: {part1()} calories")
    print(f"Answer for part 2 is: {part2()} calories")