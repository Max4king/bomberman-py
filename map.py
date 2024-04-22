class Map:
    def __init__(self, filename) -> None:
        self.filename = filename
        self.map = []
        self.load_map()

    def add_player(self, player):
        x, y = self.find_loc('2')
        self.map[y][x] = player.id

    def load_map(self):
        with open(self.filename, 'r') as f:
            for lines in f:
                line = []
                for char in lines:
                    if char != '\n':
                        line.append(char)
                self.map.append(line)

    def find_loc(self, char):
        for y, row in enumerate(self.map):
            for x, col in enumerate(row):
                if col == char:
                    return (x, y)
        return None
    
    def print_map(self):
        # print(self.map)
        for row in self.map:
            for col in row:
                print(col, end='')
            print()
        print()


if __name__ == '__main__':
    m = Map('maps/map1.txt')
    m.print_map()