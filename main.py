import random

done = False
wins, losses, ties = 0, 0, 0

names = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}
loses_to = {'R': 'P', 'S': 'R', 'P': 'S'}

while not done:
    choice = input("Please choose your next move (R, P, S) (Q to quit): ").upper()
    if choice == 'Q':
        done = True
        continue

    if choice not in names:
        print("Invalid command")
        continue

    cpu_choice = random.choice(['R', 'P', 'S'])

    if choice == cpu_choice:
        print(f"It's a tie! You both chose {names[choice]}")
        ties += 1
    elif cpu_choice == loses_to[choice]:
        print(f"CPU wins! You chose {names[choice]}, the CPU chose {names[cpu_choice]}")
        losses += 1
    else:
        print(f"You win! You chose {names[choice]}, the CPU chose {names[cpu_choice]}")
        wins += 1

    print(f"Current stats: {wins} Wins, {losses} Losses, {ties} Ties")
