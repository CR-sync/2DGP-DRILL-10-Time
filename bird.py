from pico2d import *
import game_world
import game_framework


class bird:
    image = None

    def __init__(self,x=100,y=300):
        if bird.image == None:
            bird.image = load_image('bird_animation.png')

    def update(self):
        pass

    def draw(self):
        pass