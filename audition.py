import arcade
import pyglet

from models import World

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
 
class AuditionWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height, title = "Audition Game")

        self.world = World(width, height)
        self.high_score = int()

        self.score = int()
        self.lives = int()
        self.focus_key = None

    def setup(self):
        """ Set up the game and initialize the variables. """
        self.score = 0
        self.lives = 5
        self.focus_word = None
    
 
    def on_draw(self):
        arcade.set_background_color(arcade.color.GRAY_BLUE)
        arcade.draw_text(f"Score : {self.score}", 15, 15, arcade.color.WHITE, 50)
        arcade.start_render()
 
if __name__ == '__main__':
    window = AuditionWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()