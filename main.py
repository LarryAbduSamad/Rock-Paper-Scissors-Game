import random

is_gametime = True

while is_gametime:
    
    possible_moves = ["R", "P", "S"]
    CPU = random.choice(["R", "P", "S"])
    Player = input("Enter 'R' for Rock, 'P' for Paper or 'S' for Scissors:\n")
    error_message = "Invalid entry. Please try again"
    P = "Paper"
    R = "Rock"
    S = "Scissors"

    if Player not in possible_moves:
        print(error_message)
        
    if Player == CPU:
        print('It\'s a Tie. Play again')
        
    elif Player == "R":
        if CPU == "P":
            print(f'Player({R}) : CPU({P})')
            print('CPU Wins. Game Over')
            break
            
        else:
            print(f'Player({R}) : CPU({S})')
            print('Player Wins. Game Over')
            break
        
    elif Player == "P":
        if CPU == "S":
            print(f'Player({P}) : CPU({S})')
            print('CPU Wins. Game Over')
            break
            
        else:
            print(f'Player({P}) : CPU({R})')
            print('Player Wins. Game Over')
            break
        
    elif Player == "S":
        if CPU == "R":
            print(f'Player({S}) : CPU({R})')
            print('CPU Wins. Game Over')
            break
            
        else:
            print(f'Player({S}) : CPU({P})')
            print('Player Wins. Game Over')
            break
    
            
    
     
        
        


