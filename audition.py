import arcade
import pyglet

from models import World

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
# pygame.mixer.music.load("Metalica - Matalica - Master of puppets.mp3")

class ModelSprite(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('model', None)
 
        super().__init__(*args, **kwargs)
 
    def draw(self):
        self.sync_with_model()
        super().draw()

    def sync_with_model(self):
        if self.model:
            self.set_position(self.model.x, self.model.y)
            self.angle = self.model.angle
 
class AuditionWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.GRAY_BLUE)
        arcade.draw_line(150,0,150,600,arcade.color.BLACK,10)

        self.world = World(width, height)
 
    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("score", 880, 540, arcade.color.BLACK, 20)
 
if __name__ == '__main__':
    window = AuditionWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()