def get_input():
    filepath = "./inputs/day08.txt"

    try:
        puzzle_input = open(filepath)
    except FileNotFoundError as e:
        print(e)
        return -1
    else:
        return puzzle_input.split()


def part01():
    print("- Part 1 -\n")

    puzzle_input = get_input()
    if puzzle_input == -1:
        return
    
    print(puzzle_input)


def main():
    print("=== Day 8 ===\n")
    part01()

    input('\nPress enter to exit\n')


main()