def get_priority(char):
    if char.isupper():
        return ord(char) - ord('A') + 27
    else:
        return ord(char) - ord('a') + 1
    

def get_common_char(arrs):
    sequence = arrs.pop(0)
    for char in sequence:
        if all(char in arr for arr in arrs):
            return char