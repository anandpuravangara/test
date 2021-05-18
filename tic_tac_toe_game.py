# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
def display_board(in_gamelist):
        
        print('┌' +'─' * 3 + ('┬' + '─' * 3 ) * 2 + '┐')
        print('│ {:^} │ {:^} │ {:^} │'.format(in_gamelist[0],in_gamelist[1],in_gamelist[2]))
        print('├' +'─' * 3 + ('┼' + '─' * 3 ) * 2 + '┤')
        print('│ {:^} │ {:^} │ {:^} │'.format(in_gamelist[3],in_gamelist[4],in_gamelist[5]))
        print('├' +'─' * 3 + ('┼' + '─' * 3 ) * 2 + '┤')
        print('│ {:^} │ {:^} │ {:^} │'.format(in_gamelist[6],in_gamelist[7],in_gamelist[8]))
        print('└' +'─' * 3 + ('┴' + '─' * 3 ) * 2 + '┘')

def reset_board():
        return [1,2,3,4,5,6,7,8,9]

def get_player_name(in_symbol):
        player_name = ''
        while player_name == '':
               player_name = input(f'Name of Player using symbol is {in_symbol} ? :')
        return player_name

def get_player_choice(in_player, in_available_boxes):

        player_choice_str = ''
        
        while player_choice_str == '':
                player_choice_str = input (f"{in_player['Name']}, What is your choice?")
                
                if player_choice_str.isdigit():
                        player_choice = int (player_choice_str)

                        if player_choice not in in_available_boxes:
                                print (f"{in_player['Name']}, That box is not available! Choose an available box")
                                player_choice_str = ''
                        else :
                                return player_choice
                else:
                        print (f"{in_player['Name']}, Choose a number representing  any available box")
                        player_choice_str = ''

def check_winner(in_player, game_list ):
        win_index_list = [[0,1,2], [3,4,5], [6,7,8],[0,3,6], [1,4,7],[2,5,8], [0,4,8], [2,4,6]]
        win_index_check_list = []
        for i in win_index_list:
                win_index_check_list.append ( game_list[i[0]])
                win_index_check_list.append ( game_list[i[1]])
                win_index_check_list.append ( game_list[i[2]])
                #print (win_index_check_list)
                if set(win_index_check_list) == set(in_player['symbol']):
                        #print (f"We have a winner!! Congratulations {in_player['Name']}")
                        return True

                win_index_check_list = []
        return False
    
def declare_winner(won  ,in_player):
        print ('-' * 50)
        if won:
                print(f"Congratulations {in_player['Name']} !")
        else:
                print(f"No winner this time")
        print ('-' * 50)
        print (' ' *10 + 'GAME OVER')
        print ('-' * 50)


def play_tic_tac_toe():
        player1 = {'symbol':'X'}
        player2 = {'symbol':'O'}

        print ('Choose Players:')
        player1['Name'] = get_player_name(player1['symbol'])
        player2['Name'] = get_player_name(player2['symbol'])
        players_list = [player1,player2]

        print ('Let us start tic tac toe!')
        print(f"{player1['symbol']} for  {player1['Name']}")
        print(f"{player2['symbol']} for {player2['Name']}")
        game_list = reset_board()
        available_boxes = game_list.copy()
        display_board (game_list)

        for turn in range(1,10):
    
                if not turn % 2 == 0 :
                        player = players_list[0]
                else:
                        player = players_list[1]
                
                player_choice = get_player_choice (player, available_boxes)
                game_list[player_choice - 1] = player['symbol']
                display_board (game_list)
                available_boxes.pop(available_boxes.index(player_choice))
                if turn > 2 and check_winner(player,game_list):
                        declare_winner(True,player)
                        return
        
        declare_winner(False,None)
        return


# %%
play_tic_tac_toe()


# %%



# %%

    



# %%



