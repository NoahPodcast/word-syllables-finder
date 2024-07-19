# README word-syllables-finder

## Introduction

This Python script is designed to read a dictionary file containing words and search for words that contain a specified sequence of syllables, subject to a length constraint. The script can be configured to use different dictionaries based on language selection.

## How to run the script
### Linux (Using `apt`, `apk` or `yum`)
1. Open Terminal.
2. Update the package list with the command:

    ```bash
    sudo apt update
    ```
3. Install Python by running:
    ```bash
    sudo apt install python3
    ```

### macOS (Using `brew`)
1. Open Terminal.
2. If you don't already have Homebrew installed, you can do so by running:
    ```bash
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```
3. Install Python with Homebrew using:

    ```bash
    brew install python
    ```

### Windows
For Windows, Python can be installed by downloading the installer from [the official Python website](https://www.python.org/downloads/) <u>**and download at worst the version 3**</u> or through the Microsoft Store by searching for "Python".

After installing Python, you can run the script by navigating in Terminal or Command Prompt to the directory containing the script and using the command <u>**on Windows.**</u>
```bash
python word-syllables-finder.py
```
or <u>**on Linux and macOS.**</u>

```bash
python3 word-syllables-finder.py
```
## Script Overview

1. **Read Dictionary File**: Reads words from a dictionary file and creates a mapping of words to the file path.
2. **Language Selection**: Determines which dictionary file to use based on the selected language.
3. **Syllable Search**: Prompts the user to enter syllables and searches for words in the dictionary that contain those syllables and meet a length constraint.
4. **Display Results**: Outputs the found words and their corresponding file paths.

## Parameters

### `file_path`

- **Description**: Path to the dictionary file.
- **Type**: String
- **Usage**: Set based on the selected language.

### `language`

- **Description**: Specifies the language for the dictionary.
- **Type**: String
- **Options**:
  - `"en"`: English dictionary file
  - `"fr"`: French dictionary file
  - `"other"`: A custom dictionary file for other languages
- **Default**: `"en"`

### `syllables`

- **Description**: The sequence of syllables to search for in the dictionary.
- **Type**: String

## How to Use

1. **Select the Language**:
   - Set the `language` variable to `"en"` for English, `"fr"` for French, or `"other"` for a custom language.

2. **Specify the File Path**:
   - For `"en"` or `"fr"`, the file paths are automatically set to `"en_dictionary.txt"` or `"fr_dictionary.txt"`, respectively.
   - For `"other"`, set the `file_path` variable to the appropriate dictionary file path.

3. **Run the Script**:
   - The script will read the specified dictionary file and create a word dictionary.

4. **Enter Syllables**:
   - When prompted, input the syllables you want to search for.

5. **View Results**:
   - The script will display words that contain the specified syllables and are no longer than 8 characters. It will stop searching after finding 10 words.

## Step-by-Step Explanation

1. **Reading the Dictionary File**:
   ```python
   def read_dictionary(file_path):
       word_dictionary = {}
       with open(file_path, 'r') as file:
           for line in file:
               word = line.strip()  # Remove spaces and newlines
               word_dictionary[word] = file_path
       return word_dictionary
    ```
    - This function reads each line from the file specified by `file_path`, removes any extra spaces or newline characters, and adds each word to the `word_dictionary` with the file path as the value.

2. **Language Selection**:
    ```python
    language = "en"  # "en" for English, "fr" for French, "other" for other languages

    if language == "en": 
        file_path = "en_dictionary.txt"  # English dictionary file path
    elif language == "fr":
        file_path = "fr_dictionary.txt"  # French dictionary file path
    elif language == "other":
        file_path = ""  # Enter the name file of the dictionary file of the other language
    else:
        print("Invalid language selection.")
        exit()
    ```
    - This block sets the `file_path` based on the `language` variable. It defaults to English if no other valid language is selected.

3. **Creating the Word Dictionary**:
    ```python
    word_dictionary = read_dictionary(file_path)
    ```
    - Calls the `read_dictionary` function to populate `word_dictionary` with words from the specified file.

4. **User Input and Word Search**:
    ```python
    syllables = input("Enter syllables: ")

    found_words = []
    for word in word_dictionary:
        if syllables in word and len(word) <= 8:
            found_words.append(word)
            if len(found_words) == 10:
                break
    ```
    - Prompts the user to input syllables and searches for words containing those syllables that are no longer than 8 characters. The search stops after finding 10 words.

5. **Displaying Results**:
    ```python
    if found_words:
    print("Found words:")
    for word in found_words:
        print(f"- {word} (File path: {word_dictionary[word]})")
    else:
        print("No matching word found.")
    ```
    - Displays the words found and their file paths. If no words are found, it prints a corresponding message.

## Example Usage
    
1. Set the language to `"en"` and ensure `en_dictionary.txt` is in the same directory.
    
2. Run the script.
    
3. When prompted, enter the desired syllables, e.g., `"cat"`
    
4. Review the output for matching words.

## Notes
- Ensure that the dictionary files are properly formatted, with one word per line.

- Adjust the length constraint or number of results by modifying the script as needed.

```vbnet
This README file explains each aspect of the script, from how to configure it to how it operates step by step. It provides a clear guide for users to understand and utilize the script effectively.
```