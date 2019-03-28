import pyglet

music = pyglet.resourse.media('Metalica - Matalica - Master of puppets.mp3',streaming=False)
music.play()

pyglet.app.run()