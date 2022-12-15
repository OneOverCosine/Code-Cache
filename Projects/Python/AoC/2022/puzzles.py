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

        your_choices = outcomes[outcome]  # left off here



if __name__ == "__main__":
    day_02()