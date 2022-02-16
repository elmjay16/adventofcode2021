#!/usr/bin/env python3

fname = "input.txt"

BOARD_WIDTH = 5
BOARD_HEIGHT = 5

class Entry:
    def __init__(self, val):
        self.val = int(val)
        self.seen = False

    def __repr__(self):
        return "({}, {})".format(self.val, self.seen) 

    def mark(self, draw):
        if self.val == draw:
            self.seen = True

class Board:
    def __init__(self, width=BOARD_WIDTH, height=BOARD_HEIGHT):
        self.width = width
        self.height = height
        self.rows = []  # List[List[Entry]]

    def __repr__(self):
        for r in self.rows:
            print(r)
        return ""

    def add_row(self, lst):  # type(lst) == List[Entry]
        self.rows.append(lst)

    def mark(self, val):
        for i in self.rows:
            for j in i:
                j.mark(val)

    def check(self):
        for i in self.rows:
            r = [x.seen for x in i]
            if all(r):
                return True
        
        # check columns
        for i in range(self.width):
            c = [r[i].seen for r in self.rows]
            if all(c):
                return True

        return False

    def score(self):
        res = 0
        for i in self.rows:
            for j in i:
                if not j.seen:
                    res += j.val
        return res

def get_draws(buf):
    return [int(x) for x in buf.split(",")]

def get_board(buf):
    assert(len(buf) == BOARD_HEIGHT)
    board = Board()
    for i in buf:
        row = [Entry(x) for x in i.split()]
        assert(len(row) == BOARD_WIDTH)
        board.add_row(row)
    return board

with open(fname) as f:
    data = f.readlines()

data.append('\n')  # to make board extraction loop simpler

draws = get_draws(data[0])

boards = []
buf = []
for line in data[2:]:
    if line == '\n':
        boards.append(get_board(buf))
        buf = []
    else:
        buf.append(line)


def game_loop(ds, bs):
    for d in ds:
        for b in bs:
            b.mark(d)
            res = b.check()
            if res:
                return b.score() * d

print(game_loop(draws, boards))


