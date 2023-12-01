def length_of_last_word(s):
    # Split the string into words
    words = s.split()

    # Check if there are any words in the string
    if len(words) > 0:
        # Return the length of the last word
        return len(words[-1])
    else:
        # No words found
        return 0
        
# Example usage:
s = "Hello World"
result = length_of_last_word(s)
print("Length of the last word:", result)
