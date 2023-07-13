import random
ch = ['r','p','s','1','2','3']

cont_Play = True
player_Ponits = 0
computer_Points = 0
game_Record = []

def compare(p_choise):
    computer = random.choice(ch)
    p = 0
    c = 0
    if p_choise == "r" or p_choise == "1" and computer == "s" or computer =="3":
        print('Rock smashes Scissors, Player Wins')
        p = 1
    elif p_choise == "p" or p_choise == "2" and computer == "r" or computer =="1":
        print("Paper cover Rock ,  Player Wins")
        p = 1

    elif p_choise == "s" or p_choise == "3" and computer == "p" or computer =="2":
        print("Scissors cut Paper, Player Wins")
        p = 1
    elif computer == "p" or computer =="2" and p_choise == "r" or p_choise == "1" :
        print("Paper cover Rock ,  Computer Wins")
        c = 1

    elif computer == "s" or computer =="3" and p_choise == "p" or p_choise == "2" :
        print("Scissors cut Paper, Computer Wins")
        c = 1
    elif computer == "r" or computer =="1" and p_choise == "s" or p_choise == "3" :
        print('Rock smashes Scissors, Computer Wins')
        c = 1
    else:
        return p , c

    return p , c


    

def err_Trap():
    try :
        player = input ("pick r or 1 for Rock , p or 2 for Paper , s or 3 Scissor :").strip()
        if player not in ch:
            raise ValueError ('invalid a value',"cannot enter", player, "as  an input.")
        return player
    except ValueError as expt:
        print(expt)



while cont_Play:
    p_choise =err_Trap()
    p_Ponits , c_Points =compare(p_choise)
    player_Ponits = player_Ponits + p_Ponits
    computer_Points = computer_Points + c_Points
    
    game_Record.append([player_Ponits ,computer_Points])

    cont_Play = (input ("Play again press 'Y' or 'y' ")).strip()
    if cont_Play.lower() != "y":
        print(game_Record)
        print (f"Your score {player_Ponits} , computer score {computer_Points}")
        cont_Play = False
        
    

    
    