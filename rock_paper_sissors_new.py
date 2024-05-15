from random import choice

print("""\nRock - Paper - Sissors
Best of three 
lets's GOOO !\n""")

player = 0
computer = 0
opt = ["rock","paper","sissors"]

for i in range(3):

    user = input("Enter your choice: ")
    automatic = choice(opt)
    print(automatic)

    if (user == "paper" and automatic == "rock") or (user == "rock" and automatic == "sissors") or (user == "sissors" and automatic == "paper"):
        print("\nRound won\n")
        player += 1

    elif user == automatic: print("Tie")

    else:
        print("\nRound lost\n")
        computer += 1
    
    if player == 2: 
        print("YOU WIN !!")
        break
    elif computer == 2: 
        print("YOU LOOOOSE !!")
        break

if player > computer: print("YOU WIN !!")
else: print("YOU LOOOOSE !!")