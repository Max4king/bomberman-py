class Player:
    def __init__(self, id) -> None:
        self.id = id
        self.max_bombs = 1
        self.bombs = 0
        self.bomb_range = 2
        self.score = 0
        self.pos = (0, 0)
        self.score = 0
        self.alive = True

    def move(self, direction):
        pass

    def place_bomb(self):
        pass

    def die(self):
        pass
