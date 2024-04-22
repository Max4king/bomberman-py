from map import Map
from player import Player
import random


def game():
    player = Player('R')
    m = Map('maps/map1.txt')
    m.add_player(player)
