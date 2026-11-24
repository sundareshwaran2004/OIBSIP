# Random Password Generator

## OASIS InfoByte Internship – Task 3

**Domain:** Python Programming  
**Task:** Random Password Generator  
**Level:** Beginner

## Project Description

This project is a Random Password Generator developed using Python. It allows users to create secure, random passwords based on their preferred length and character types.

## Features

- Generates random passwords with a minimum length of 8 characters.
- Allows users to include uppercase letters (A–Z).
- Allows users to include lowercase letters (a–z).
- Allows users to include numbers (0–9).
- Allows users to include special symbols.
- Requires at least two character types.
- Accepts Yes/No responses for easy interaction.
- Handles invalid user inputs.
- Allows users to generate multiple passwords without restarting the program.
- Uses Python's `secrets` module for secure random generation.

## Technologies Used

- Python 3
- Visual Studio Code
- Python `secrets` module
- Python `string` module

## How to Run

1. Open the project folder in Visual Studio Code.
2. Open `password-generator.py`.
3. Run the Python file.
4. Enter the required password length.
5. Select the desired character types using Yes or No.
6. View the generated password.
7. Choose whether to generate another password.

## Sample Output

```text
===== RANDOM PASSWORD GENERATOR =====

Enter password length (minimum 8): 12

Include CAPITAL letters (A-Z)? (yes/no): yes
Include small letters (a-z)? (yes/no): yes
Include numbers (0-9)? (yes/no): yes
Include special symbols (!@#$)? (yes/no): yes

===== YOUR PASSWORD =====
Generated Password: K7#mP2@xL9!q
Password Length: 12

Do you want to generate another password? (yes/no): no

Thank you for using Password Generator!
```

*Note: The password above is an illustrative example. Actual generated passwords vary.*

## Conclusion

This project demonstrates Python programming concepts such as loops, functions, conditional statements, input validation, string manipulation, and secure random password generation.