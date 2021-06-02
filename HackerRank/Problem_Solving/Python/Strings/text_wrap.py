import textwrap

string = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
max_width = 4

wrapped_list = textwrap.wrap(string, max_width)

wrapped_string = ""

for i in range(len(wrapped_list)):
    wrapped_string += wrapped_list[i]
    if i != len(wrapped_list) - 1:
        wrapped_string += "\n"

print(wrapped_string)