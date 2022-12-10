pscore=int(0)
cscore=int(0)

from random import randint
choices= ["rock", "paper","scissors"]
while True:    
    for i in range(1,6):
        computer=choices[randint(0,2)] 
        player =input("Enter your choice 1: rock, 2:paper, 3:scissors - ").lower()
        if player == computer:
            print("Both chose the same and draw")
        elif (player=="rock" and computer =="scissors") or (player=="scissors" and computer =="paper") or (player=="paper" and computer =="rock"):
            pscore+=1
            print("You win")
        else: 
            cscore+=1
            print("Computer wins")
    print("You won "+ str(pscore)+ " times against the cpu out of 5 times")
    if pscore>cscore:
        print("Player wins against CPU")
    else:
        print("CPU wins against player")
    player_input= input("Do you want to continue playing y/n - ")
    if player_input == "y":
        continue
    else:
        print("Thank you for playing!")
        break
    

        
