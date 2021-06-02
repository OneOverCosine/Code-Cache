def minion_game(string):
    vowels = "AEIOU"
    players = {"Stuart": 0,
               "Kevin": 0}

    anagrams = {}

    window = 0 # this is the size of the anagram

    for i in range(len(string)):

        window = len(string) - i

        # left off here - running will probs cause errors
        for j in range(i, window):
            current = string[:i+1]
            if current in anagrams.keys():
                print(f"{current} is already in the dictionary")
            else:
                anagrams.update({current: string.count(current)})
                print(f"{current} was added to the dict")
        window += 1

    # final things to get the correct return value
    if players["Stuart"] == players["Kevin"]:
        return "Draw"

    if players["Stuart"] > players["Kevin"]:
        winner = "Stuart"
    else:
        winner = "Kevin"

    return f"{winner} {players[winner]}"

if __name__ == '__main__':

    s = "banana"

    print(minion_game(s.upper()))