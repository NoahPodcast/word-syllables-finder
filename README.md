# README.md

## Introduction

This script reads a file containing words and creates a custom dictionary. It allows users to search for words containing specific syllables with a length constraint. The script supports English and French dictionaries by default and can be customized for other languages.

## Prerequisites

- Python 3.x installed on your system.
- A text file containing the words for the dictionary.

## Installation

1. Clone the repository to your local machine:

    ```sh
    git clone https://github.com/yourusername/word-syllables-finder.git
    ```

2. Navigate to the project directory:

    ```sh
    cd word-syllables-finder
    ```

## Usage

### For Linux Users

1. Place your dictionary file in the appropriate location:
    - For English, place your file at `/home/your-username/word-syllables-finder/en_dictionary.txt`.
    - For French, place your file at `/home/your-username/word-syllables-finder/fr_dictionary.txt`.
    - For other languages, update the script with the path to your custom dictionary file.

2. Run the script:

    ```sh
    python script_name.py
    ```

    Replace `script_name.py` with the name of your script file.

3. Enter the syllables when prompted:

    ```sh
    Enter syllables: your_syllables
    ```

### For Windows Users

1. Place your dictionary file in the appropriate location:
    - For English, place your file at `C:\\Users\\your-username\\word-syllables-finder\\en_dictionary.txt`.
    - For French, place your file at `C:\\Users\\your-username\\word-syllables-finder\\fr_dictionary.txt`.
    - For other languages, update the script with the path to your custom dictionary file.

2. Open Command Prompt (cmd) and navigate to the project directory:

    ```cmd
    cd C:\Users\yourusername\word-syllables-finder
    ```

3. Run the script:

    ```cmd
    python script_name.py
    ```

    Replace `word-syllables-finder.py` with the name of your script file.

4. Enter the syllables when prompted:

    ```cmd
    Enter syllables: your_syllables
    ```

## Script Explanation

Here's a breakdown of what the script does:

1. **Function to read the file and create the word dictionary:**

    ```python
    def read_dictionary(file_path):
        word_dictionary = {}
        with open(file_path, 'r') as file:
            for line in file:
                word = line.strip()  # Remove spaces and newlines
                word_dictionary[word] = file_path
        return word_dictionary
    ```

    This function reads the specified file line by line, strips any spaces and newlines, and adds the words to a dictionary with the word as the key and the file path as the value.

2. **Language selection:**

    ```python
    language = "en"  # "en" for English, "fr" for French, "other" for other languages
    ```

    This variable sets the language for the dictionary. You can change it to "fr" for French or "other" for other languages.

3. **Path of the file containing the words:**

    ```python
    if language == "en": 
        file_path = "/home/your-username/word-syllables-finder/en_dictionary.txt" 
    elif language == "fr":
        file_path = "/home/your-username/word-syllables-finder/fr_dictionary.txt"
    elif language == "other":
        file_path = ""  # Enter the path of the file containing the words
    else:
        print("Invalid language selection.")
        exit()
    ```

    This block sets the file path based on the selected language. Update the path if you choose "other".

4. **Read the file and create the word dictionary:**

    ```python
    word_dictionary = read_dictionary(file_path)
    ```

    This line calls the `read_dictionary` function to create the word dictionary from the specified file.

5. **Ask the user to enter syllables:**

    ```python
    syllables = input("Enter syllables: ")
    ```

    This line prompts the user to enter the syllables they want to search for.

6. **Search for matching words with length constraint:**

    ```python
    found_words = []
    for word in word_dictionary:
        if syllables in word and len(word) <= 8:
            found_words.append(word)
            if len(found_words) == 10:
                break
    ```

    This block searches for words in the dictionary that contain the entered syllables and are 8 characters or less in length. It stops after finding 10 matching words.

7. **Display the results:**

    ```python
    if found_words:
        print("Found words:")
        for word in found_words:
            print(f"- {word} (File path: {word_dictionary[word]})")
    else:
        print("No matching word found.")
    ```

    This block displays the found words and their file paths. If no words are found, it prints a message saying so.

## Customization

- To change the length constraint, modify the number in `len(word) <= 8` to your desired length.
- To change the maximum number of words to find, modify the number in `if len(found_words) == 10`.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Contributing

Feel free to open issues or submit pull requests if you have suggestions for improvements or new features.