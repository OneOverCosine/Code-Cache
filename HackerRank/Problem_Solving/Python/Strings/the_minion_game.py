def minion_game(string):
    vowels = "AEIOU"
    players = {"Stuart": 0,
               "Kevin": 0}

    for i in range(len(string)):
        if string[i] in vowels:
            players["Kevin"] += len(string) - i
        else:
            players["Stuart"] += len(string) - i

    # final things to get the correct return value
    if players["Stuart"] == players["Kevin"]:
        print("Draw")
    elif players["Stuart"] > players["Kevin"]:
        winner = "Stuart"
        print(f"{winner} {players[winner]}")
    else:
        winner = "Kevin"
        print(f"{winner} {players[winner]}")


def force_minion_game(string):
    # my brute force method went wrong somewhere
    # I somehow understand the more optimal solution
    # better than the 'naive' version
    vowels = "AEIOU"
    players = {"Stuart": 0,
               "Kevin": 0}

    anagrams = {}

    for i in range(len(string)):
        # i will be the size of the window

        # left off here - running will probs cause errors
        for j in range(len(string) - i):
            current = string[j:j+i+1]
            # print(current)
            if current in anagrams.keys():
                #print(f"{current} is already in the dictionary")
                continue
            
            print(f"{current} is being added to the dictionary")
            anagrams.update({current: string.count(current)})
            print(f"It occurs {anagrams[current]} time(s) in {string}")
            if current[0] in vowels:
                players["Kevin"] += anagrams[current]
            else:
                players["Stuart"] += anagrams[current]
        

    # final things to get the correct return value
    if players["Stuart"] == players["Kevin"]:
        print("Draw")
    elif players["Stuart"] > players["Kevin"]:
        winner = "Stuart"
        print(f"{winner} {players[winner]}")
    else:
        winner = "Kevin"
        print(f"{winner} {players[winner]}")

    

if __name__ == '__main__':

    s = "BANANANAAAS"

    force_minion_game(s)