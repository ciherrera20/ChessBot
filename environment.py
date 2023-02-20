import numpy as np

class Chess():
    def __init__(self):
        self.reset_board()
    
    def reset_board(self):
        self._state = np.zeros((8, 8))
        piece_row = np.array([2, 3, 4, 5, 6, 4, 3, 2])
        pawn_row = np.ones(8)

        # Populate white side
        self._state[0] = piece_row
        self._state[1] = pawn_row

        # Populate black side
        self._state[-2] = -pawn_row
        self._state[-1] = -piece_row
    
    def __getitem__(self, pos):
        col = {l: i for i, l in enumerate('abcdefgh')}[pos[0]]
        row = int(pos[1]) - 1
        return self._state[row, col]

    def __str__(self):
        # piece_dict = [' ', '\u2659', '\u2656', '\u2658', '\u2657', '\u2655', '\u2654', '\u265A', '\u265B', '\u265D', '\u265E', '\u265C', '\u265F']
        # Switched black and white pieces since white pieces appear black in the terminal and vice versa
        piece_dict = [' ', '\u265F', '\u265C', '\u265E', '\u265D', '\u265B', '\u265A', '\u2654', '\u2655', '\u2657', '\u2658', '\u2656', '\u2659']
        rows = []
        for r in reversed(self._state):
            rows.append('')
            for piece in r:
                rows[-1] += piece_dict[int(piece)]
        return '\n'.join(rows)
        