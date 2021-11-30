"""
This program shows how to have a pause screen without resetting the game.

Make a separate class for each view (screen) in your game.
The class will inherit from arcade.View. The structure will
look like an arcade.Window as each View will need to have its own draw,
update and window event methods. To switch a View, simply create a view
with `view = MyView()` and then use the "self.window.set_view(view)" method.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.view_pause_screen
"""

import arcade
from scripts import constants
from scripts.menu import MenuView



# the start of the program run this to run the game.
def main():
    window = arcade.Window(constants.WIDTH, constants.HEIGHT, "Instruction and Game Over Views Example")
    menu = MenuView()
    window.show_view(menu)
    arcade.run()

 
if __name__ == "__main__":
    main()