def count_words(sentence):
    words = sentence.split()
    return len(words)

# Main
print(count_words("what did you do all day?"))  # Output: 5
