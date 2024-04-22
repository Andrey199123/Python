# Andrey Vasilyev 4/21/24
from typing import Tuple, List, Type, Set, Optional
from copy import deepcopy
import numpy as np

Move = str  # type alias


class Board:
    def __init__(self, ncols=8, nrows=7):
        self.player_board = None
        self.ncols = ncols
        self.nrows = nrows
        self.board = list()
        self.tiles = {'r', 'g', 'y', 'b', 'p', 'bl'}  # tile colors

    def create_random(self, seed: Optional[int] = None):
        np.random.seed(seed)
        for i in range(self.nrows):
            row = list()
            for j in range(self.ncols):
                forbidden_tiles = set()
                if i > 0:
                    forbidden_tiles.add(self.board[-1][j])  # forbid color of above tile
                if j > 0:
                    forbidden_tiles.add(row[-1])  # forbid color of leftward tile
                eligible_tiles = self.tiles - forbidden_tiles  # rest of tiles eligible
                row.append(np.random.choice(list(eligible_tiles)))  # add color
            self.board.append(row)  # add row to board

        # Assign corner tiles to players
        self.player_board = [[None for j in range(self.ncols)] for i in range(self.nrows)]  # instantiate player board
        self.player_board[-1][0] = 0  # bottom left is player 0
        self.player_board[0][-1] = 1  # top right is player 1

    def add_move(self, move: str, player: int):
        """Returns new board"""
        new_board = Board()
        new_board.board = deepcopy(self.board)
        new_board.player_board = deepcopy(self.player_board)

        for i in range(self.nrows):
            for j in range(self.ncols):
                if new_board.player_board[i][j] == player:  # controlled tile
                    new_board.board[i][j] = move  # set tile's color to move

                    if i > 0 and new_board.player_board[i - 1][j] is None and new_board.board[i - 1][j] == move:  #
                        # usurp above tile
                        new_board.player_board[i - 1][j] = player

                    if i + 1 < self.nrows and new_board.player_board[i + 1][j] is None and new_board.board[i + 1][
                        j] == move:
                        new_board.player_board[i + 1][j] = player

                    if j > 0 and new_board.player_board[i][j - 1] is None and new_board.board[i][
                        j - 1] == move:
                        new_board.player_board[i][j - 1] = player

                    if j + 1 < self.ncols and new_board.player_board[i][j + 1] is None and new_board.board[i][
                        j + 1] == move:  # usurp rightward tile  
                        new_board.player_board[i][j + 1] = player
        return new_board

    def get_player_tiles(self) -> str:
        """Used for getting legal and potential moves"""
        if self.player_board[-1][0] == 0:  # if player 0 is bottom left
            return self.board[-1][0], self.board[0][-1]
        else:  # if player 0 is top right
            return self.board[0][-1], self.board[-1][0]

    def get_board_value(self, player: int) -> int:
        """Number of squares controlled by player"""
        player_value = sum(self.player_board[i].count(player) for i in range(self.nrows))
        opponent_value = sum(self.player_board[i].count(1 - player) for i in range(self.nrows))
        return player_value - opponent_value

    def get_potential_moves(self, player: int) -> Set[str]:
        potential_moves = set()
        for i in range(self.nrows):
            for j in range(self.ncols):
                if self.player_board[i][j] == player:  # add adjacent tiles not controlled for each controlled tile

                    if i > 0 and self.player_board[i - 1][j] is None:
                        potential_moves.add(self.board[i - 1][j])

                    if i + 1 < self.nrows and self.player_board[i + 1][j] is None:
                        potential_moves.add(self.board[i + 1][j])

                    if j > 0 and self.player_board[i][j - 1] is None:
                        potential_moves.add(self.board[i][j - 1])

                    if j + 1 < self.ncols and self.player_board[i][j + 1] is None:
                        potential_moves.add(self.board[i][j + 1])
        player_0_tile, player_1_tile = self.get_player_tiles()  # subtract tiles of both players to avoid overcounting
        return potential_moves - {player_0_tile, player_1_tile}

    def get_legal_moves(self, player: int) -> Set[str]:
        """To top user from entering an illegal move or wrong text"""
        player_0_tile, player_1_tile = self.get_player_tiles()
        return self.tiles - {player_0_tile, player_1_tile}

    def print_score(self):
        p0_score = sum(self.player_board[i].count(0) for i in range(self.nrows)) # every controlled square for each
        # row on the board
        p1_score = sum(self.player_board[i].count(1) for i in range(self.nrows))
        return f"{p0_score} to {p1_score}"
