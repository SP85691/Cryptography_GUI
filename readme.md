## Project Name: Cryptography Algorithm

## Project Description

The Encryption and Decryption Algorithm is a project created for a college mini project. The purpose of the project is to encrypt and decrypt messages using a predefined set of characters and a specific shift value. The project includes two main functions, encrypt() and decrypt(), which take in user input and either encrypt or decrypt the message based on user choice.

## Features

The Encryption and Decryption Algorithm includes the following features:

* Encryption: Allows users to encrypt their message using a predefined set of characters and a specific shift value.
* Decryption: Allows users to decrypt their message using the same predefined set of characters and shift value used to encrypt the message.
* User Input: Allows users to input their message and choose whether to encrypt or decrypt it.
* File Input: Reads the predefined set of characters from a file to ensure consistency in encryption and decryption.

## Requirements

* Python 3
* A text editor or integrated development environment (IDE)
* A file containing the predefined set of characters (included in the project)

## Installation

1. Clone the repository to your local machine.
2. Ensure that you have Python 3 installed on your machine.
3. Open the command prompt or terminal in the cloned directory.
4. Run the program using the command "python encryption_algorithm.py".

## Usage

1. Enter your message in the console when prompted.
2. Choose whether to encrypt or decrypt the message.
3. The encrypted or decrypted message will be displayed in the console.
4. Choose whether to continue or exit the program.

## Encryption and Decryption Algorithm

This algorithm takes in user input message and either encrypts or decrypts it based on user choice. It uses a predefined set of characters as keys and shifts the characters based on a specific value. The shifted value is determined by taking the last character of the key and appending the rest of the keys to it.

The algorithm reads the keys from a file and stores them in a variable. Then, the keys are shifted to create a new value. The new value is then used to create a dictionary, where the keys represent the original set of characters, and the values represent the shifted set of characters. If the mode is 'E' (encrypt), the user input message is converted to lowercase and each character is replaced with the corresponding character in the dictionary. If the mode is 'D' (decrypt), the shifted values are used to create a dictionary, where the keys represent the shifted set of characters, and the values represent the original set of characters. The user input message is then converted to lowercase, and each character is replaced with the corresponding character in the dictionary. Finally, the resulting message is printed to the console.

The program also includes a function to convert a list of strings to a single string.

## How to Use

1. Clone the repository to your local machine
2. Make sure you have Python 3 installed on your machine
3. Open the command prompt/terminal in the cloned directory
4. Run the program using the command "python encryption_algorithm.py"
5. Enter your message and choose to encrypt or decrypt
6. The encrypted/decrypted message will be displayed on the console
7. Choose to continue or exit the program

## About Cryptography GUI

This code is a simple graphical user interface (GUI) for encrypting and decrypting files using the functions from `cryptomachine.py`. It uses the `tkinter` module to create the GUI.

#### Here's what the code does:

1. Imports the necessary modules and functions.
2. Defines a class `App` for the GUI.
3. Initializes the GUI with a title, size, and background color.
4. Creates a frame and a label for the heading.
5. Adds a button for opening files.
6. Defines a method `openfile` for opening the selected file and adding buttons for encryption and decryption.
7. Defines a method `list_to_string` for converting a list to a string.
8. Defines a method `encrypt` for encrypting the selected file and displaying the result in a new window.
9. Defines a method `decrypt` for decrypting the selected file and displaying the result in a new window.

Note that the `encrypt` and `decrypt` methods both write the results to new files (with "encrypted_file.txt" and "decrypted_file.txt" as the filenames) instead of modifying the original file. Also, the `decrypt` method currently prints the decrypted data to the console, which may not be desirable behavior.

Overall, the code appears to be well-organized and easy to understand. However, there may be some potential issues with error handling, especially if the user selects invalid files or inputs.

#### Outputs

![1678468831136](image/readme/1678468831136.png)

#### Encrypted Output

![1678469107594](image/readme/1678469107594.png)

#### Decrypted Output

![1678469015091](image/readme/1678469015091.png)

## Contributors

This project was created by `Surya Pratap` for a college mini project.

## Future Improvements

* Add more advanced encryption algorithms
* Improve user input validation and error handling
* Allow users to choose the key set and shift value
* Add a graphical user interface (GUI) for ease of use.

## Conclusion

The Encryption and Decryption Algorithm is a simple but effective project for encrypting and decrypting messages. It is designed to be easy to use and customizable. Future improvements could include more advanced encryption algorithms and user input validation.
