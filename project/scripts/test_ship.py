from scripts.player_ship import Player_Ship
import arcade
from scripts import constants

class Test_Ship(Player_Ship):
    """This is the test ship will not be put into the game but is here for testing
    a chiled of Plyer_Ship"""
    def __init__(self):
        super().__init__()
        self.sprit =  "project\images\\test_ship.png"