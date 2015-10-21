class Tile:
    def __init__(self, passable=False):
        self.passable = passable
        self.steps = float("inf")

    def __bool__(self):
        return self.passable


def create(f):
    start = None
    end = None
    tiles = [ [Tile()]*25 for i in range(25) ]

    for y, row in enumerate(f):
        for x, tile in enumerate(row.strip()):
            if tile in (' ', 'S', 'E'):
                tiles[y][x] = Tile(True)

            if tile == 'S':
                start = (y,x)

            if tile == 'E':
                end = (y,x)

    return tiles, start, end


def show(tiles, start, end, solution):
    for y, row in enumerate(tiles):
        for x, tile in enumerate(row):
            if (y,x) == start:
                print("S", end='')
            elif (y,x) == end:
                print("E", end='')
            elif (y, x) in solution:
                print("+", end='')
            elif tile:
                print(" ", end='')
            else:
                print("#", end='')
        print()
