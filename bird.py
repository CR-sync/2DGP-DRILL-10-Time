from pico2d import *
import game_world
import game_framework



class Bird:
    image = None

    def __init__(self,x=100,y=300,left=50, right=750):
        if self.image == None:
            self.image = load_image('bird_animation.png')

        self.x, self.y = x, y
        self.frame = 0
        self.face_dir = 1
        self.dir = 0

    def update(self):
        pass

    def draw(self):
        pass