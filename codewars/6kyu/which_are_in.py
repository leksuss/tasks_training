# https://www.codewars.com/kata/550554fd08b86f84fe000a58


def in_array(array1, array2):
    substrgins = []
    for word in array1:
        if word in '|'.join(array2) and word not in substrgins:
            substrgins.append(word)
    return sorted(substrgins)


arr1 = ["live", "arp", "strong"]
arr2 = ["lively", "alive", "harp", "sharp", "armstrong"]
assert in_array(arr1, arr2) == ['arp', 'live', 'strong']

arr1 = ["arp", "mice", "bull"]
arr2 = ["lively", "alive", "harp", "sharp", "armstrong"]
assert in_array(arr1, arr2) == ['arp']
