from pico2d import *
import game_world
import game_framework


class bird:
    image = None

    def __init__(self):
        if bird.image == None:
            bird.image = load_image('bird_animation.png')