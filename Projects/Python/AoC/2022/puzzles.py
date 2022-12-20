def get_input(day):
    """Takes a string in the form 'xx' as input.
    Returns a TextIOWrapper"""
    current_dir = "./Projects/Python/AoC/2022/inputs/"
    file_path = current_dir + "day_" + day + ".txt"

    try:
        file_input = open(file_path, "r")
    except FileNotFoundError:
        print("Could not find file")
        return -1
    else:
        return file_input


def day_01():
    print("=== Day 01 ===")

    file_input = get_input("01")
    if file_input == -1:
        return

    lines = file_input.readlines()

    cal_sums = []
    cal_sum = 0
    top_n = 3

    for line in lines:
        if line == "\n":
            cal_sums.append(cal_sum)
            cal_sum = 0
        else:
            cal_sum += int(line)
    
    size = len(cal_sums)
    cal_sums.sort()
    print(f"Max calories: {cal_sums[-1]}")  # 66186, part 1 answer
    print(f"Sum of calories for top {top_n} elves: {sum(cal_sums[size - top_n:size])}")  # 196804, part 2


def day_02():
    print("=== Day 02 ===")
    file_input = get_input("02")

    if file_input == -1:
        return

    lines = file_input.read().split("\n")
    # A = Rock, B = Paper, C = Scissors
    # X = Rock, Y = Paper, Z = Scissors

    total_points = 0
    outcome_scores = {"loss": 0, "draw": 3, "win": 6}
    choice_scores = {"X": 1, "Y": 2, "Z": 3}

    # Part 1
    outcomes = {"loss": ["A Z", "B X", "C Y"],
                "draw": ["A X", "B Y", "C Z"],
                "win": ["A Y", "B Z", "C X"]}
  
    for line in lines:
        your_choice = line[-1]

        total_points += choice_scores[your_choice]

        if line in outcomes["win"]:
            total_points += outcome_scores["win"]

        elif line in outcomes["draw"]:
            total_points += outcome_scores["draw"]

        elif line in outcomes["loss"]:
            total_points += outcome_scores["loss"]

    print(f"Final score: {total_points}")
    
    # Part 2
    total_points = 0
    true_outcomes = {"X": "loss", "Y": "draw", "Z": "win"}

    for line in lines:
        opponent_choice = line[0]
        outcome = true_outcomes[line[-1]]

        possible_choices = outcomes[outcome]
        your_choice = ""
        
        for choices in possible_choices:
            if opponent_choice == choices[0]:
                your_choice = choices[-1]
                break
        
        total_points += choice_scores[your_choice] + outcome_scores[outcome]
    
    print(f"Correct final score: {total_points}")


def day_03():
    print("=== Day 03 ===")
    
    file_input = get_input("03")

    if file_input == -1:
        return
    
    puzzle_input = file_input.read().split()

    # part 1: priority sums
    priority_sum = 0

    for rucksack in puzzle_input:
        split = len(rucksack) // 2
        item = common_substring(1, rucksack[0:split], rucksack[split:len(rucksack)])
        priority_sum += get_priority(item)

    print(f"Priority of misplaced items: {priority_sum}")


    # part 2: common in three strings


def common_substring(size, string1, string2):
    """ only looking for a single match for day 03 """

    for i in range(0, len(string1) - size + 1):
        chars1 = string1[i:i+size]
        for j in range(0, len(string2) - size + 1):
            chars2 = string2[j:j+size]
            if chars1 == chars2:
                return chars1

    return "No match found"


def multi_common_substring(size, strings):
    

    string1_test = "hello"
    string2_test = "hallo"




def get_priority(letter):
    if len(letter) > 1:
        return 0

    if letter.isupper():
        return ord(letter) - 38
    return ord(letter) - 96


if __name__ == "__main__":
    day_03()