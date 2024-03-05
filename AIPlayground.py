# Programmer: Brian Kuhn
# Date: 2.29.2024
# Program: AI Playground

print("This will be a place for me to play with programming using AI Technology\n")

def analyze_paragraph(paragraph):
    # Split the paragraph into words
    words = paragraph.split()

    # Count the total number of words
    num_words = len(words)

    # Create a dictionary to store word frequencies
    word_count = {}

    # Count the number of repeated words
    repeated_words = 0
    for word in words:
        # Convert word to lowercase to treat "Word" and "word" as the same
        word = word.lower()
        if word in word_count:
            word_count[word] += 1
            repeated_words += 1
        else:
            word_count[word] = 1

    # Calculate the percentage of repeated words
    if num_words > 0:
        repeat_percentage = repeated_words / num_words
    else:
        repeat_percentage = 0

    return num_words, repeated_words, repeat_percentage, word_count

# Test the function
paragraph = input("Enter a paragraph: ")
num_words, repeated_words, repeat_percentage, word_count = analyze_paragraph(paragraph)
print("Number of words:", num_words)
print("Number of repeated words:", repeated_words)
print("Percentage of repeated words:", repeat_percentage)
print("Word frequency count:", word_count)
