# Guess the Word Game – Python

## Description
**Guess the Word Game** is a Python-based console game where the player must guess a hidden word within 6 chances.  
For each correct letter guessed, the remaining chances stay the same. For each incorrect guess, the chances decrease by 1.  
The game continues until the player guesses the entire word or runs out of chances.

---

## Project Overview
The game randomly selects a word from a predefined list and displays it as underscores (`_`) representing each letter.  
The player guesses one letter at a time:
- If the guessed letter is in the word, it is revealed in its correct position(s).
- If the guessed letter is not in the word, the remaining chances are reduced.
The game ends with either:
- **Victory** – The player correctly guesses all letters before running out of chances.
- **Defeat** – The player fails to guess the word within 6 chances.

---

## Features
- Random word selection from a predefined list.  
- Tracks correct and incorrect guesses.  
- Displays the current state of the word after each guess.  
- Case-insensitive letter matching.  
- Clear win/lose game-ending messages.

---

## Tools & Technologies
- **Python** – Core programming language.  
- **Random** module – For word selection.  

---

## How to Run
1. Ensure Python is installed on your system.  
2. Download the project files from this repository.  
3. Open the terminal/command prompt in the project folder.  
4. Run the game:
   ```bash
   python guess_the_word.py
