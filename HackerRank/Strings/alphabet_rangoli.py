import string

def print_rangoli(n):
    
    # a list of letters (indexing starts from 0)
    letters = string.ascii_lowercase[0:n]

    rows = []
    center_row = letters[0]
    rangoli_string = ""

    half_way = ((2 * n) - 1) // 2

    # no of rows: (2*n) - 1
    # no of cols: (4*n) - 3
    #print(letters, "\n")

    # build up the center row
    # range(stop)
    for i in range(1, n):
        center_row = letters[i] + "-" + center_row + "-" + letters[i]

    dash_count = 1
    for i in range(half_way - 1, -1, -1):
        temp = letters[n - (i + 1)]
        dashes = "--" * dash_count
        dash_count += 1

        for j in range(n - (i + 1) + 1, n):
            temp = letters[j] + "-" + temp + "-" + letters[j]

        rows.append(f"{dashes}{temp}{dashes}")

    # build the string
    for i in range(len(rows) - 1, -1, -1):
        rangoli_string += rows[i] + "\n"

    rangoli_string += center_row + "\n"

    for i in range(len(rows)):
        rangoli_string += rows[i]
        if i != len(rows) - 1:
            rangoli_string += "\n"

    print(rangoli_string)

if __name__ == "__main__":
    n = 10

    print_rangoli(n)