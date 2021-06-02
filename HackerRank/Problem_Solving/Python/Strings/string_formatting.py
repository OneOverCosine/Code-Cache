# was unaware of the built-in methods of converting from decimal
# to the other bases while attempting this

def print_formatted(number):
    # number is the max value (decimal) to print

    dec_vals = []
    bin_vals = []
    oct_vals = []
    hex_vals = []

    for i in range(1, number + 1):

        dec_vals.append(str(i))
        bin_vals.append(convert_to_nth_base(i, 2))
        oct_vals.append(convert_to_nth_base(i, 8))
        hex_vals.append(convert_to_nth_base(i, 16))

    string_width = len(bin_vals[number - 1])

    for i in range(number):
        print(dec_vals[i].rjust(string_width), oct_vals[i].rjust(string_width), hex_vals[i].rjust(string_width), bin_vals[i].rjust(string_width))

def convert_to_nth_base(number, base):
    converted_value = ""
    hex_vals = ["A", "B", "C", "D", "E", "F"]

    while number != 0:

        remainder = number % base
        number = int(number / base)

        # a little extra for base 16
        if remainder > 9:
            converted_value = hex_vals[remainder - 10] + converted_value
            continue

        converted_value = str(remainder) + converted_value

    return converted_value

if __name__ == "__main__":
    print_formatted(20)