# make a nice looking door mat
import math
import sys

def make_door_mat(n, m):
    # m = n * 3
    symbols = ("-", ".|.")
    
    mat = ""

    # middle WELCOME is (m - 7)/2 dashes each side
    # first and last row have .|. then (m - 3)/2 dashes each side 
    # others have 2n + 1 .|. then m - (2n + 1 * 3) / 2 dashes each side
    # upto middle adds .|. 2 for each row

    c_lines = math.floor((m-7)/2) * symbols[0]
    center_line = c_lines + "WELCOME" + c_lines

    # go up to the floor of n/2

    rows = []

    for i in range(math.floor(n/2)):
        d_multiplier = math.floor((math.floor(n/2) - i) * 3) # the number of dashes per row
        c_multiplier = (2 * i) + 1 # the number of these '.|.' per row

        row = symbols[0] * d_multiplier + symbols[1] * c_multiplier + symbols[0] * d_multiplier
        rows.append(row)

    for row in rows:
        mat += row + "\n"

    mat += center_line + "\n"

    for i in range(len(rows) - 1, -1, -1):
        mat += rows[i]
        
        if i != 0:
            mat += "\n"

    print(mat)

if __name__ == "__main__":
    n = 13

    # inputs_list = []

    # for line in sys.stdin:
    #     inputs_list.append(line.strip())

    # inputs_list = inputs_list[0].split()

    # # remember to convert strings to integers
    # n = int(inputs_list[0])
    # m = int(inputs_list[1])

    m = 3 * n

    make_door_mat(n, m)
