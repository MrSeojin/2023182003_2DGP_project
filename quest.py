from pico2d import load_font
import random

import game_world
import play_mode
from back_ground import Fever
from prince import Prince


class Quest:
    def __init__(self):
        self.font = load_font('ENCR10B.TTF', 35)
        self.num = 0
        self.type = 1
        #self.type = random.randint(1,3)
        if self.type == 0:
            self.goalNum = 0
            self.quest_story = None
        elif self.type == 1:
            self.goalNum = random.randint(10, 15)
            self.quest_story = f'jump   {self.goalNum}'
        elif self.type == 2:
            self.goalNum = random.randint()
            self.quest_story = f'double jump    {self.goalNum}'
        elif self.type == 3:
            self.goalNum = random.randint()
            self.quest_story = f'mob    {self.goalNum}'
        elif self.type == 4:
            self.goalNum = random.randint()
            self.quest_story = f'run    {self.goalNum}'


        # X, 점프 n번, 2단 점프 n번, 적 잡기 n번, 몇 거리 달리기..?,

    def draw(self):
        if self.type > 0:
            self.font.draw(400, 30, self.quest_story + f' : {self.num}', (5, 5, 5))

    def update(self):
        if self.goalNum == self.num and self.type!=0:
            self.num = 0
            self.type = 0
            play_mode.fever_time = True
            play_mode.princess.state_machine.add_event(('FLY_ITEM', 0))