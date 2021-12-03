from game import constants
import arcade
from game.menu import MenuView

# This is the main file that runs the game.
def main():
    window = arcade.Window(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, "Space Force")
    menu = MenuView()
    window.show_view(menu)
    arcade.run()

if __name__ == "__main__":
    main()
 