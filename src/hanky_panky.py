""" Test stuff """
import logging, sys

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)


class Player:
    def __init__(self, initial_position):
        self.initial_position = initial_position
        self.link = None
        self.linked_by = None
    
    def __repr__(self):
        format_str = "inital_position: {},  links_to: {} via link {}, linked_by link: {}"
        return format_str.format(
            self.initial_position,
            self.link.link_to.initial_position if self.link else None,
            self.link.creator.initial_position if self.link else None,
            self.linked_by.creator.initial_position if self.linked_by else None)

class Link:
    def __init__(self, creator, link_to):
        self.link_to = link_to
        self.linkers = {creator}
        self.creator = creator


    
    def __repr__(self):
        format_str = " linkers: {} -> link_to: {}"
        return format_str.format( [linker.initial_position for linker in self.linkers], self.link_to.initial_position)

class Game:
    def __init__(self, num_players, num_beats):
        self.players = [None]*num_players
        self.num_players = num_players
        self.num_beats = num_beats

        for i in range(num_players):
            self.players[i] = Player(i)

    def eliminate(self, index, depth=0):
        logging.debug("ELIMINATE: %d, %d", index, depth)
        player_at_index = self.players[index]

        if player_at_index.linked_by is not None:
            # eliminating a player that others link to
            next_player_index = (index + 1) % self.num_players
            next_player = self.players[next_player_index]

            if next_player.link is not None:
                # merge
                rlink = next_player.link
                llink = player_at_index.linked_by

                for linker in llink.linkers:
                    rlink.linkers.add(linker)
                    linker.link = rlink

                # clean up player at index
                player_at_index.link = rlink
                player_at_index.linked_by = None
                rlink.linkers.add(player_at_index)
                
            else:
                player_at_index.link = player_at_index.linked_by
                player_at_index.linked_by = None
                player_at_index.link.link_to = next_player
                next_player.linked_by = player_at_index.link
                

        else:
            # eliminating a player that is independent
            if player_at_index.link is not None:
                self.eliminate(player_at_index.link.link_to.initial_position, depth + 1)
            else:
                # Eliminating a player that is alive
                next_player_index = (index + 1) % self.num_players
                next_player = self.players[next_player_index]
                
                if next_player.link is not None:
                    player_at_index.link = next_player.link
                    next_player.link.linkers.add(player_at_index)
                else:
                    link = Link(player_at_index, next_player)
                    player_at_index.link = link
                    next_player.linked_by = link


    def __repr__(self):
        string = ""
        for player in self.players:
            string += str(player) + '\n'
        
        return string


def test_game_tmp():
    logging.debug("************************ START **********************************")
    game = Game(10, 31)

    logging.debug(game)
    
    logging.debug("\nelimintating 2...\n")
    game.eliminate(2)
    logging.debug(game)


    logging.debug("\nelimintating 4...\n")
    game.eliminate(4)
    logging.debug(game)

    logging.debug("\nelimintating 3...\n")
    game.eliminate(3)
    logging.debug(game)




    logging.debug("************************ END **********************************")



# run code
test_game_tmp()
