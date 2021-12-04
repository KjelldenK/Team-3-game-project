import arcade
from game.testing_alien import Tesing_Alien
import game.menu
from game import constants
import random


class GameView(arcade.View):
    # game View this screen will show the main game screen and handles the inputs for the game and outputs for the game

    def __init__(self, ship):
        super().__init__()
        
        self.left = False
        self.right = False
        self.player = None
        self.player_list = None
        self.enemy_list = None
        self.bullet_list = None
        self.menu_Background = "project\images\Backgrounds\darkPurple.png"
        self.score = 0
        self.wave = 1
        self.lives = 3


        self.set_up(ship)
        


    def set_up(self, ship):
        # sets up the game screen

        # sets up the lists for the alian sprites
        self.alian_ships = arcade.SpriteList()
        self.alian_bullet_list = arcade.SpriteList()

        # sets up the player sprites
        self.player_list = arcade.SpriteList()
        

        # creates the player 
        self.player = ship
        self.player.center_x = constants.SCREEN_WIDTH / 2 
        self.player.center_y = 100
        self.player_list.append(self.player)

        self.bullet_list = self.player.get_bullet_list()

        # sets up the shooting timer for the ship that was picked
        self.shooting = False
        self.ship_attack_timer = self.player.get_attack_speed()
        self.time_between_shooting = self.player.get_attack_speed()

        # makes the grid for the enemys to spawn on
        self.open_spot = []
        
        
        for y in range(400, 701, 50):
            for x in range(100, 701, 50):
                self.open_spot.append([x, y])
                

        self.taken_spot = []

        # starts by making wave one of the game
        i = 0
        while i < 5:

            self.alian = Tesing_Alien("project\images\enemy ships\enemyBlack1.png",
            scale= 0.5, 
            alian_bullet_list= self.alian_bullet_list,
            time_between_firing= 15)
            enemy_spot = self.open_spot[random.randint(0, len(self.open_spot) - 1)]
            self.alian.center_y = enemy_spot[1]
            self.alian.center_x = enemy_spot[0]
            self.alian_ships.append(self.alian)
            self.taken_spot.append(enemy_spot)
            self.open_spot.remove(enemy_spot)
            i += 1



    def on_draw(self):
        # Draws all the objects for the game
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, arcade.load_texture(self.menu_Background))
        self.player_list.draw()
        self.bullet_list.draw()
        self.alian_ships.draw()
        self.alian_bullet_list.draw()
        arcade.draw_text(f"Score: {self.score}",10 , constants.SCREEN_HEIGHT / 50, arcade.color.WHITE, font_size=15, font_name = "Kenney Rocket")
        arcade.draw_text(f"lives: {self.lives}",600 , constants.SCREEN_HEIGHT / 50, arcade.color.WHITE, font_size=15, font_name = "Kenney Rocket")


    def on_update(self, delta_time):
        
        self.player_list.on_update(delta_time)
        self.alian_ships.on_update(delta_time)
        self.player_list.update()
        self.bullet_list.update()
        self.alian_bullet_list.update()
        # checks to see if there was a collision
        
        #make the alians shoot at random times

        for alian in self.alian_ships:
            
            odds = int(250 * (1 /60) / delta_time)

            if random.randrange(odds) == 0:
                bullet = arcade.Sprite(alian.bullet_type)
                bullet.center_x = alian.center_x
                bullet.top = alian.bottom
                bullet.angle = 180
                bullet.change_y = -5
                self.alian_bullet_list.append(bullet)



        for bullet in self.bullet_list:
        
            hit_list = arcade.check_for_collision_with_list(bullet, self.alian_ships)

            if len(hit_list) > 0:
                bullet.remove_from_sprite_lists()

            for alien in hit_list:
                self.score += alien.get_value()
                alien.remove_from_sprite_lists()

            if bullet.top > constants.SCREEN_HEIGHT:
                bullet.remove_from_sprite_lists()
            
            
            
        for bullet in self.alian_bullet_list:

            hit_list = arcade.check_for_collision_with_list(bullet, self.player_list)

            if len(hit_list) > 0:
                bullet.remove_from_sprite_lists()
                self.lives -= 1

            if bullet.top < 0:
                bullet.remove_from_sprite_lists() 

        # checks to see if there are any more alians and if there is not reset them
        if len(self.alian_ships) == 0:

            for spot in self.taken_spot:
                self.open_spot.append(spot)
                self.taken_spot.remove(spot)

            i = 0
            while i < 10:

                self.alian = Tesing_Alien("project\images\enemy ships\enemyBlack1.png",
                scale= 0.5, 
                alian_bullet_list= self.alian_bullet_list,
                time_between_firing= 15)
                enemy_spot = self.open_spot[random.randint(0, len(self.open_spot) - 1)]
                self.alian.center_y = enemy_spot[1]
                self.alian.center_x = enemy_spot[0]
                self.alian_ships.append(self.alian)
                self.taken_spot.append(enemy_spot)
                self.open_spot.remove(enemy_spot)
                i += 1
        
        # if you run out of lives go back to the menu this will change later
        if self.lives <= 0:
            menu = game.menu.MenuView()
            self.window.show_view(menu)



    def on_key_press(self, key, _modifiers):
        # checks for key press
        for ship in self.player_list:
            if key == arcade.key.LEFT:
                ship.action("left", True)

            if key == arcade.key.RIGHT:
                ship.action("right", True)
            
            if key == arcade.key.SPACE:
                ship.action("shoot", True)
                
        

    def on_key_release(self, key, _modifiers):
        # checks to see if a key was released so it can stop moving the player
        for ship in self.player_list:

            if key == arcade.key.LEFT:
                ship.action("left", False)

            if key == arcade.key.RIGHT:
                ship.action("right", False)

            if key == arcade.key.SPACE:
                ship.action("shoot", False)
                