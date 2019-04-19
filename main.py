import arcade

from audition import AuditionWindow

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def main():
    game = AuditionWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()