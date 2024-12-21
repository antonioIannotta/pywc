# Pywc

This is a simple command-line program that mimics the functionality of the Unix `wc` command. It allows you to count the number of lines, words, and characters in a text file.

## Table of Contents

1. [Features](#features)  
2. [Installation](#installation)  
3. [Usage](#usage)    
4. [License](#license)  

## Features

- **Count Lines**: Use the `-l` option to count the number of lines in a file.
- **Count Words**: Use the `-w` option to count the number of words in a file.
- **Count Characters**: Use the `-c` option to count the number of characters in a file.
- **Combine Options**: You can combine multiple options to get a summary of lines, words, and characters.

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/antonioIannotta/pywc.git
   cd pywc
   ```
2. **Install dependencies**:
This program only requires Python 3, so no additional dependencies are needed.
3. **Create a virtual environment venv and start it**:
    ```bash
   python -m venv env
   source env/bin/activate
   ```

4. **Create a package of the software and install it**:
    ```bash
   python setup.py bdist_wheel sdist
   pip install .
   ```


## Usage
Run the program from the command line:
   ```bash
   pywc <file_name> [options]
   ```

### Options
- -l: count the number of lines
- -w: count the number of words
- -c: count the number of characters

## License
This project is licensed under the MIT License. See the LICENSE file for details.