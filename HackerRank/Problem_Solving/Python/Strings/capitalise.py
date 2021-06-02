def solve(s):
    # second attempt after 'my_solve' failed some cases
    prev = " "
    s_new = ""

    for i in range(len(s)):
        
        if s[i].isalpha():
            # print(f"{s[i]} is an alphabetic character")

            if s[i] == s[i].lower() and prev == " ":
                # print(f"{s[i]} needs to be capitalised!")
                s_new += s[i].upper()
            else:
                s_new += s[i]
        else:
            s_new += s[i]

        prev = s[i]

    return s_new

def my_solve(s):
    # the initial problem didn't make clear a few of the
    # reqirements - this was my initial solution

    # words = s.split()
    words = s.split(" ") # all I needed to do was explicitly split on spaces
    # to get my initial solution to work

    capitalised_string = ""

    for word in words:
        capitalised_string += word.capitalize() + " "

    # just for the sake of readablilty
    # to remove the last space from the output
    size = len(capitalised_string)

    return capitalised_string[:size - 1]


if __name__ == '__main__':

    s = "q w e r t y u i o p a s d f g h j  k l z x c v b n m Q W E R T Y U I O P A S D F G H J  K L Z X C V B N M"

    print(my_solve(s))