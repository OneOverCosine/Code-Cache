def dec_to_bin(value):
    """ converts integer numbers from decimal to binary
    and prints them to the console """

    remainder = ""

    while value > 0:
        remainder += str(value % 2)
        value = value // 2

    print(value)
    print(remainder[::-1])


def bin_to_dec(value):
    """ converts integer numbers from binary to decimal
    and prints them to the console.
    Assumes input as list of digits, so [1, 0, 0, 0, 1, 1] for example """

    exponent = 0
    result = 0

    for bit in value[::-1]:
        result += bit * (2 ** exponent)
        exponent += 1

    print(result)


if __name__ == "__main__":
    
    bin_to_dec([1, 0, 0, 0, 1, 1])