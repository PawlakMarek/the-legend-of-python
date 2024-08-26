### Checkpoint ⛳️
# Congratulations on completing the first four chapters of The Legend of Python! Now let's use the skills you've learned (variables, control flow statements, and loops) to build a Python project on your own.
#
# Use the Python Code Editor, Visual Studio Code, or your code editor of choice for this project.
#
# # Rock Paper Scissors
# Rock, Paper, Scissors is a classic game that resonates with folks from around the world.
#
# Create a rock_paper_scissors.py program where the user plays a round of Rock, Paper, Scissors with the computer.
#
# The rules are as follows:
#
# Rock beats Scissors.
# Scissors beat Paper.
# Paper beats Rock.
# First, create a player and a computer variable.
#
# Prompt the player to select number between 1 and 3 with input() and store it in player:
#
# 1 is for “✊” (Rock).
# 2 is for “✋” (Paper).
# 3 is for “✌” (Scissors).
# Then, use the random.randint() method to assign a number to the computer variable (1 to 3).
#
# Lastly, use control flow to compare the user's choice and the computer's choice, determine the winner, and print out who won.
#
# The output should look something like this:
#
# ===================
# Rock Paper Scissors
# ===================
# 1) ✊
# 2) ✋
# 3) ✌️
# Pick a number: 2
#
# You chose: ✋
# CPU chose: ✊
# The player won!
#
# # Bonus: Rock Paper Scissors Lizard Spock
# Okay, you have played Rock, Paper, Scissors, but have you heard of Rock, Paper, Scissors, Lizard, Spock? It's a fun variation of the classic game brought to popularity with a TV show called The Big Bang Theory.
#
# The rules are very similar to the ones from the classic “Rock Paper Scissors” but with two new options, “Lizard” and “Spock”:
#
# Scissors cut Paper.
# Paper covers Rock.
# Rock crushes Lizard.
# Lizard poisons Spock.
# Spock smashes Scissors.
# Scissors beat Lizard.
# Lizard eats Paper.
# Paper disproves Spock.
# Spock vaporizes Rock.
# Rock breaks Scissors.
# Watch this video to understand it better.
#
# Here's a note from the creator, Sam Kass:
#
# “I invented this game (with Karen Bryla) because it seems like when you know someone well enough, 75-80% of any Rock Paper Scissors games you play with that person end up in a tie. Well, here is a slight variation that reduces that probability. This version is also nice because it satisfies the Law of Fives.”
#
# Go back to your Rock Paper Scissors program and see if you can turn it into Rock Paper Scissors Lizard Spock!
#
# Use "🖖" for "Spock and "🦎" for "Lizard".
#
# The output should look something like this:
#
# ================================
# Rock Paper Scissors Lizard Spock
# ================================
# 1) ✊
# 2) ✋
# 3) ✌️
# 4) 🦎
# 5) 🖖
# Pick a number: 3
#
# You chose: ✌️
# CPU chose: ✌️
# It's a tie!
#
# # Submit Your Project
# After completing your project, join our Community and submit it to the Checkpoint channel. One of our team members will get back to you with feedback and the completion status!
#
# If you have any questions, feel free to ask them in the #python or #checkpoint Discord channels.
#
# Happy coding!
#
# Get help from Code Mentors and submit your project for review!

import random

print(
    """Welcome to Rock, Paper, Scissors, Lizard, Spock!
The rules are simple:
- ✌️ cuts ✋
- ✋ covers ✊
- ✊ crushes 🦎
- 🦎 poisons 🖖
- 🖖 smashes ✌️
- ✌️ decapitates 🦎
- 🦎 eats ✋
- ✋ disproves 🖖
- 🖖 vaporizes ✊
- ✊ crushes ✌️
- First to 3 wins!
"""
)

choices = ["✊", "✋", "✌️", "🦎", "🖖"]
player_score = 0
computer_score = 0
turn = 1

while player_score < 3 and computer_score < 3:
    print(
        f"""===========================
Round {turn}
Player: {player_score}
Computer: {computer_score}

Available weapons:
1) ✊ - Rock
2) ✋ - Paper
3) ✌️ - Scissors
4) 🦎 - Lizard
5) 🖖 - Spock
"""
    )
    player_choice = int(input("Choose your weapon: "))
    if player_choice < 1 or player_choice > 5:
        print("Invalid choice! Try again.\n")
        continue

    computer_choice = random.randint(1, 5)
    print(f"Computer chooses {choices[computer_choice-1]}")

    if player_choice == computer_choice:
        print("It's a tie!")
    elif player_choice == 1:
        if computer_choice == 2 or computer_choice == 5:
            computer_score += 1
            if computer_choice == 2:
                print("✋ covers ✊")
            else:
                print("🖖 vaporizes ✊")
            print("Computer wins!")
        else:
            player_score += 1
            if computer_choice == 3:
                print("✊ crushes ✌️")
            else:
                print("✊ crushes 🦎")
            print("You win!")
    elif player_choice == 2:
        if computer_choice == 3 or computer_choice == 4:
            computer_score += 1
            if computer_choice == 3:
                print("✌️ cuts ✋")
            else:
                print("🦎 eats ✋")
            print("Computer wins!")
        else:
            player_score += 1
            if computer_choice == 1:
                print("✋ covers ✊")
            else:
                print("✋ disproves 🖖")
            print("You win!")
    elif player_choice == 3:
        if computer_choice == 1 or computer_choice == 5:
            computer_score += 1
            if computer_choice == 1:
                print("✊ crushes ✌️")
            else:
                print("🖖 smashes ✌️")
            print("Computer wins!")
        else:
            player_score += 1
            if computer_choice == 2:
                print("✌️ cuts ✋")
            else:
                print("✌️ decapitates 🦎")
            print("You win!")
    elif player_choice == 4:
        if computer_choice == 1 or computer_choice == 3:
            computer_score += 1
            if computer_choice == 1:
                print("✊ crushes 🦎")
            else:
                print("✌️ decapitates 🦎")
            print("Computer wins!")
        else:
            player_score += 1
            if computer_choice == 2:
                print("🦎 eats ✋")
            else:
                print("🦎 poisons 🖖")
            print("You win!")
    elif player_choice == 5:
        if computer_choice == 4 or computer_choice == 2:
            computer_score += 1
            if computer_choice == 4:
                print("🦎 poisons 🖖")
            else:
                print("✋ disproves 🖖")
            print("Computer wins!")
        else:
            player_score += 1
            if computer_choice == 1:
                print("🖖 vaporizes ✊")
            else:
                print("🖖 smashes ✌️")
            print("You win!")

    print("")
    turn += 1

if player_score == 3:
    print("Congratulations on your wits! You win!")
else:
    print("Better luck next time! Computer wins!")
