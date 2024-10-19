Wordle Clone: Python Implementation
Overview
This is a text-based Python clone of the popular word-guessing game Wordle. Players have up to six attempts to guess a secret five-letter word, with feedback provided after each guess using colored emojis:

🟩 (Green) for correct letters in the correct position
🟨 (Yellow) for correct letters in the wrong position
⬜️ (White) for incorrect letters
The project demonstrates core programming concepts like loops, conditionals, string manipulation, and function abstraction.

Features
User Input Handling: Ensures the user input matches the expected word length.
Emoji Feedback: Provides clear feedback using emojis to show which letters are correct, misplaced, or incorrect.
Modular Design: The game logic is divided into separate functions for better code readability and organization.
Game Loop: Allows players to make up to six guesses, with an early win condition if the word is guessed correctly.
How to Play
The game prompts you to enter a five-letter word.
You’ll receive feedback in the form of emojis:
🟩 (Green): Correct letter in the correct position.
🟨 (Yellow): Correct letter, but in the wrong position.
⬜️ (White): Incorrect letter.
You have six attempts to guess the word correctly. If successful, you’ll see a winning message. If not, the correct word is revealed.
Tech Stack
Language: Python 3
Libraries: No external libraries required
How to Run
Clone the repository:
bash
Copy code
git clone https://github.com/mfandohan05/simple-wordle.git
cd wordle-clone
Run the program:
bash
Copy code
python wordle.py
Follow the prompts in the terminal to play the game.
What I Learned
Implementing basic game logic with loops and conditionals.
Working with string manipulation and validating user inputs.
Building modular functions to organize the code structure.
Adding emoji-based feedback for user interaction.
Contributing
Feel free to fork this repository, submit issues, or suggest improvements via pull requests. Contributions are welcome!

License
This project is licensed under the MIT License.
