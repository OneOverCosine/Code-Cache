def findKthPositive(arr, k):
    current = 1
    missing = []

    index = 0

    while len(missing) < k:

        # the missing number is 'outside' the given array
        if index == len(arr):

            if missing == []:
                return arr[len(arr) - 1] + k

            k_new = k - len(missing)
            return arr[len(arr) - 1] + k_new

        if arr[index] > current:
            missing.append(current)
        elif arr[index] == current:
            index += 1

        current += 1

    print(missing)
    return missing[k-1]

arr = [1, 3, 4, 5]
k = 2

print(findKthPositive(arr, k))