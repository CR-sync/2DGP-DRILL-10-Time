from pico2d import *

from boy import Boy
from grass import Grass
from bird import Bird, RUN_SPEED_PPS
import game_world

import game_framework
import random


boy = None


def handle_events():
    global running

    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            boy.handle_event(event)


def init():
    global boy
    global running

    running = True
    grass = Grass()
    game_world.add_object(grass, 0)

    boy = Boy()
    game_world.add_object(boy, 1)

    # 새 10마리 생성: 화면 너비 800, 높이 600을 기준으로 랜덤 위치 및 속도
    for i in range(10):
        x = random.randint(50, 750)
        y = random.randint(120, 520)
        b = Bird(x=x, y=y, left=50, right=750)
        # 랜덤 초기 방향과 약간의 속도 변동을 준다
        b.face_dir = random.choice([-1, 1])
        b.speed = RUN_SPEED_PPS * b.face_dir * random.uniform(0.8, 1.2)
        game_world.add_object(b, 1)


def update():
    game_world.update()
    #delay(0.1) #강제로 딜레이 추가


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()


def finish():
    game_world.clear()


def pause(): pass
def resume(): pass
