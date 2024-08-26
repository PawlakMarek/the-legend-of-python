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
