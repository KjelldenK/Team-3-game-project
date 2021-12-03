import arcade
from game import constants
from game.character_selection import Character_Selection_View

#from scripts.character_selection import Character_selection



class MenuView(arcade.View):
    """This is the menu this will show when you start the game allows the player to hit play and go to ship selection"""
    def __init__(self):
        super().__init__()
        self.play_button = False
        self.menu_Background = "project\images\menu_background.jpg"
        self.Play_Button = "project\images\playbutton.png"
        self.play_hover = False

    def on_show(self):
        #draws background
        arcade.set_background_color(arcade.color.WHITE)
        

    def on_draw(self):
        # draws everything every frame.
        arcade.start_render()

        arcade.draw_lrwh_rectangle_textured(0,
            0,
            constants.SCREEN_WIDTH,
            constants.SCREEN_HEIGHT,
            arcade.load_texture(self.menu_Background))

        arcade.draw_texture_rectangle(constants.SCREEN_WIDTH // 2,
            constants.SCREEN_HEIGHT // 2 + 100,
            200,
            100,
            arcade.load_texture(self.Play_Button))
            
        if self.play_hover == True:
            arcade.draw_rectangle_outline(constants.SCREEN_WIDTH // 2,
                constants.SCREEN_HEIGHT // 2 + 100,
                200,
                100,
                arcade.color.GRAY, 3)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        # checks for mouse press to see if the player hit the play button
        if _button == arcade.MOUSE_BUTTON_LEFT:
            if _x >= constants.SCREEN_WIDTH // 2 - 100 and _x <= constants.SCREEN_WIDTH // 2 + 100 and _y <= constants.SCREEN_HEIGHT // 2 + 150 and _y >= constants.SCREEN_HEIGHT // 2 + 50:
            
                character_selection = Character_Selection_View()
                self.window.show_view(character_selection)

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        # checks where the mouse is at all times.
        if x >= constants.SCREEN_WIDTH // 2 - 100 and x <= constants.SCREEN_WIDTH // 2 + 100 and y <= constants.SCREEN_HEIGHT // 2 + 150 and y >= constants.SCREEN_HEIGHT // 2 + 50:
            self.play_hover = True

        else:
            self.play_hover = False