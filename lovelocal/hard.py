def shortest_palindrome(s):
    if not s:
        return ""

    # Function to check if a string is a palindrome
    def is_palindrome(string):
        return string == string[::-1]

    # Find the longest palindrome substring starting from the beginning
    i = 0
    for j in range(len(s), 0, -1):
        if is_palindrome(s[:j]):
            break
        i += 1

    # Reverse the remaining part of the string and concatenate it to the original string
    return s[i:][::-1] + s

# Example usage:
input_string = "abcd"
result = shortest_palindrome(input_string)
print("Shortest palindrome:", result)

