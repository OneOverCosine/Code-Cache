# given a string and a substring, find the number of times that substring appears
def count_substring(string, sub_string):
    sub_len = len(sub_string)
    count = 0
    
    for i in range(0, len(string) + 1 - sub_len):
        # check segments between i - (i + sub_len)
        current = string[i:i + sub_len]
        print(f"{sub_string} is being compared with {current}")
        
        if string[i:i + sub_len] == sub_string:
            count += 1
    
    return count


def main():

    string = "kekkers"
    sub_string = "ke"

    print("Running count_substring()")
    print(count_substring(string, sub_string))

main()