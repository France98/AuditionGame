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

        for y in range(0,601,200):
            arcade.draw_line(0,y,800,y,arcade.color.BLACK,2)

        self.world = World(width, height)
        self.arrow_sprite = ModelSprite('images/ship.png',model=self.world.arrow)
 
    def on_draw(self):
        arcade.start_render()
        self.arrow_sprite.draw()
 
if __name__ == '__main__':
    window = AuditionWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()