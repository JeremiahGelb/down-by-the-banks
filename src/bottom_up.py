"bottom up soln"

def solve(num_players, num_beats):
    pos_of_winner = 0
    pos_of_loser_of_last_round = 1

    for num_players_last_round in range(2, num_players + 1):
        print("\nround of ", num_players_last_round)
        
        print("pos_of_loser_last_round ", pos_of_loser_of_last_round)

        starting_player_to_make_loser_lose = (pos_of_loser_of_last_round - num_beats) % num_players_last_round
        print("starting_player_to_make_loser_lose ", starting_player_to_make_loser_lose)
        
        pos_of_loser_of_last_round = (starting_player_to_make_loser_lose)
        if (pos_of_loser_of_last_round == 0):
            pos_of_loser_of_last_round = num_players_last_round
    
        print("new pos_of_loser_last_round ", pos_of_loser_of_last_round)



    

solve(6, 1*2*3*4*5*6)


