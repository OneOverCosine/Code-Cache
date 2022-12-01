def super_reduced_string(s):
    """
    re-read the problem
    """
    result, prev = '', ''
    for current in s:
        print(f"prev: {prev} | current: {current} | result: {result}")
        if prev == current:
            prev = ''
            continue
        
        result += prev
        prev = current

    result += prev # to catch the last valut for prev
    return result


if __name__ == "__main__":
    s = "aaabccddd"

    print(f"result: {super_reduced_string(s)}")