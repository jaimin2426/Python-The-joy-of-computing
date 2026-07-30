# Rock-Paper-Scissor
🔹 Game Flow

Both players enter a number

Example:

Player 1 → 12345

Player 2 → 67890

Each player chooses a secret bit position (index of a digit)

Python indexes start from 0.

Example:

Player 1 → chooses position 2 → digit at index 2 in 12345 is 3.

Player 2 → chooses position 4 → digit at index 4 in 67890 is 0.

The chosen digit is converted into a move (Rock, Paper, or Scissor)

The digit is taken mod 3 (digit % 3).

Then it’s mapped like this:

Player One: {0:'Rock', 1:'Paper', 2:'Scissor'}
Player Two: {0:'Paper', 1:'Rock', 2:'Scissor'}


In our example:

Player 1 → digit = 3 → 3 % 3 = 0 → "Rock"

Player 2 → digit = 0 → 0 % 3 = 0 → "Paper"

Winner is decided based on Rock-Paper-Scissors rules

Rock beats Scissor

Scissor beats Paper

Paper beats Rock

Same choice = Draw

Game continues until you enter n when asked.

🔹 Example Play
Player one, Enter your choice: 12345<br>
Player two, Enter your choice: 67890<br>
Player one, Enter the secret bit position: 2<br>
Player two, Enter the secret bit position: 4<br>
Player two wins!!<br>
Do you want to continue? y/n: n<br>