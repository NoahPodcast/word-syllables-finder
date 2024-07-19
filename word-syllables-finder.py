# Function to read the file and create the word dictionary
def read_dictionary(file_path):
    word_dictionary = {}
    with open(file_path, 'r') as file:
        for line in file:
            word = line.strip()  # Remove spaces and newlines
            word_dictionary[word] = file_path
    return word_dictionary

# Language selection
language = "en"  # "en" for English, "fr" for French, "other" for other languages

# Path of the file containing the words
if language == "en": 
    file_path = "en_dictionary.txt" # English dictionary file path
elif language == "fr":
    file_path = "fr_dictionary.txt" # French dictionary file path
elif language == "other":
    file_path = ""  # Enter the name file of the dictionary file of the other language
else:
    print("Invalid language selection.")
    exit()

# Read the file and create the word dictionary
word_dictionary = read_dictionary(file_path)

# Ask the user to enter syllables
syllables = input("Enter syllables: ")

# Search for matching words with length constraint
found_words = []
for word in word_dictionary:
    if syllables in word and len(word) <= 8: # Check if the syllables are in the word and the word length is less than or equal to 8, you can change the length constraint
        found_words.append(word)
        if len(found_words) == 10:  # Stop the search after finding 10 words
            break

# Display the results
if found_words:
    print("Found words:")
    for word in found_words:
        print(f"- {word} (File path: {word_dictionary[word]})")
else:
    print("No matching word found.")