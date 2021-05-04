def validate_player_letter_choice(player_letter_choice):
    
    while player_letter_choice not in ["X", "O"]:
        player_letter_choice = input("Sorry, need an X or an O. Try again.").upper() 
        

def display_game_board(list_of_board_positions): 
    
    for i in list_of_board_positions:
        print("\t" * 6, "  |   |   ")
        print("\t" * 6, f"{i[0]} | {i[1]} | {i[2]}")
        print("\t" * 6, "  |   |   ")
        if i == [7, 8, 9]: break
        print("\t" * 6, '-' * 9)


def ask_player1_for_letter():     
    
    player1_letter = input("Player 1, Which letter do you choose: X or O? ").upper()
    
    return player1_letter

def assign_letters_to_players():

    player1_letter = ask_player1_for_letter()
    
    validate_player_letter_choice(player1_letter)

    if player1_letter == "X": player2_letter = "O" 
        
    else: player2_letter = "X"
        
    return player1_letter, player2_letter

def display_player_letters(player1_letter):
    
    if player1_letter == "X":
        print("Player 1 chose X, so Player 2 is an O!")
    else:
        print("Player 1 chose O, so Player 2 is an X!")

def reset():  
    
    global game_board_positions, player1, player2, game_active 
    
    while True: 
    
        ask = input("Do you want to play again? Y or N? ").upper()

        if ask == 'Y':

            player1, player2 = player_letter()

            grid_num_l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

            display_game_board(game_board_positions)
            
            break

        elif ask not in ['Y', 'N']:
            print('Need a y for yes or n for no: ') 
            

        else:
            game_board_positions = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
            game_active = False 
            break
        
    
    return game_active
    

def game_winner(triple, x):
    
    global player1, player2, game_active

    if (triple in game_board_positions) or triple in [[game_board_positions[0][0],game_board_positions[1][0], 
                                                                                game_board_positions[2][0]],  
                      [game_board_positions[0][1], game_board_positions[1][1], game_board_positions[2][1]],
                      [game_board_positions[0][2], game_board_positions[1][2], game_board_positions[2][2]],
                      [game_board_positions[0][0], game_board_positions[1][1], game_board_positions[2][2]],
                      [game_board_positions[0][2], game_board_positions[1][1], game_board_positions[2][0]]]:

        if player1 == x:
            print("Player 1 Wins!")

        else:
            print("Player 2 Wins!")

        return reset()
            


def draw():
    
    count = 0
    for i in game_board_positions:
        for j in i:
            if type(j) == str:
                count += 1

    if count == 9:
        print("It is a draw!")
        count = 0 #resets the count to 0 to use draw() again
        return reset()

    return count

def player_move(r, c, position, move, letter):
    
    if move == position:
        
        if type(game_board_positions[r][c]) == str:
            move = int(input("Already occupied. Try another position. ")) 
        
        game_board_positions[r][c] = letter
        display_game_board(game_board_positions)

def player_input(player, letter, player_num):
    
    move = input(f"Player {player_num}, which position do you choose? ")
    
    while move not in str(list(range(1,10))) or move == "":
        move = input("Need an integer from 1 to 9. Try again. ")
    else:
        move = int(move)
    
    if player == letter:

        player_move(0, 0, 1, move, letter)

        player_move(0, 1, 2, move, letter)

        player_move(0, 2, 3, move, letter)

        player_move(1, 0, 4, move, letter)

        player_move(1, 1, 5, move, letter)

        player_move(1, 2, 6, move, letter)

        player_move(2, 0, 7, move, letter)

        player_move(2, 1, 8, move, letter)

        player_move(2, 2, 9, move, letter)
            

game_board_positions = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] 

player1, player2 = assign_letters_to_players()
display_player_letters(player1) 

game_active = True

def main():
    
    global game_board_positions

    display_game_board(game_board_positions)
    
    game_winner(['X', 'X', 'X'], 'X')
    game_winner(['O', 'O', 'O'], 'O')

    
    while game_active:
        
        if player1 == 'X':

            player_input(player1, 'X', 1)
            p1_X_win = game_winner(['X', 'X', 'X'], 'X')
            
            if p1_X_win == False:
                break
                
            else:
                draw()
            
        else:
            
            player_input(player1, 'O', 1)
            p1_O_win = game_winner(['O', 'O', 'O'], 'O')
            
            if p1_O_win == False:
                break
                
            else:
                draw()
            
            
        if player2 == 'O':
                
            player_input(player2, 'O', 2)
            p2_O_win = game_winner(['O', 'O', 'O'], 'O')
            
            if p2_O_win == False:
                break
                
            else:
                draw()
        
        else:
            
            player_input(player2, 'X', 2)
            p2_X_win = game_winner(['X', 'X', 'X'], 'X')
            
            if p2_X_win == False:
                break
                
            else:
                draw()
                
                
if __name__ == "__main__":
    main()   