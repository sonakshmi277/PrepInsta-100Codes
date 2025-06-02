def solve(a, b):
    # Base case: both strings empty → match
    if len(a) == 0 and len(b) == 0:
        return True

    # If pattern is empty but text is not → no match
    if len(a) == 0:
        return False

    # If text is empty but pattern has remaining characters
    if len(b) == 0:
        # If pattern has only '*'s left, it's okay
        return all(char == '*' for char in a)

    # If characters match or pattern has '?'
    if a[0] == b[0] or a[0] == '?':
        return solve(a[1:], b[1:])

    # If pattern has '*', it can match 0 or more chars
    if a[0] == '*':
        return solve(a[1:], b) or solve(a, b[1:])

    # Else: characters don't match
    return False


str1="Prep?"
str2="Prep2i"
print("First string with wild characters :" , str1)
print("Second string without wild characters ::" , str2)
print(solve(str1,str2))