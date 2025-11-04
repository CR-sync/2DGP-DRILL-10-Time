from pico2d import *
import game_world
import game_framework


# bird의 Run Speed 계산
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_MPS = 6.0 #6 m/s
RUN_SPEED_PPS = RUN_SPEED_MPS * PIXEL_PER_METER
# bird Run Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14

class Bird:
    image = None

    def __init__(self,x=100,y=500,left=50, right=1550):
        if Bird.image == None:
            Bird.image = load_image('bird_animation.png')

        self.x, self.y = x, y
        self.left, self.right = left, right
        self.frame = 0
        self.face_dir = 1
        self.speed = RUN_SPEED_PPS * self.face_dir #방향 확인 포함

        self.frame_w = Bird.image.w //5
        self.frame_h = Bird.image.h //3

    def update(self):
        dt = game_framework.frame_time
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * dt) % FRAMES_PER_ACTION
        self.x += self.speed * dt

        if self.x < self.left:
            self.x = self.left
            self.face_dir = 1
            self.speed = RUN_SPEED_PPS * self.face_dir
        elif self.x > self.right:
            self.x = self.right
            self.face_dir = -1
            self.speed = RUN_SPEED_PPS * self.face_dir

    def draw(self):
        if self.face_dir == 1:  # right
            Bird.image.clip_draw(
                ((int(self.frame) % FRAMES_PER_ACTION) % 5) * (Bird.image.w // 5),
                Bird.image.h - (Bird.image.h // 3),
                Bird.image.w // 5,
                Bird.image.h // 3,
                self.x,
                self.y)
        else:
            Bird.image.clip_composite_draw(
                ((int(self.frame) % 14) % 5) * (Bird.image.w // 5),
                Bird.image.h - (Bird.image.h // 3),
                Bird.image.w // 5,
                Bird.image.h // 3,
                0,
                'h',
                self.x,
                self.y,
                Bird.image.w // 5,
                Bird.image.h // 3)