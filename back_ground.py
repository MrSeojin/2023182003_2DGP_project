from pico2d import load_image, load_music

import game_framework
import game_world
import play_mode
import random

# princess Run Speed
PIXEL_PER_METER = (100.0 / 20)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

class Background:
    sound = None
    def __init__(self):
        self.image = load_image('map_background_snow.png')
        self.count = 0
        self.x = 0
        Background.sound = load_music('background_sound.mp3')
        Background.sound.set_volume(32)
        Background.sound.repeat_play()

    def update(self):
        if play_mode.princess.stop:
            pass
        else:
            if play_mode.princess.action >= 5:
                self.x += 2 * RUN_SPEED_PPS * game_framework.frame_time
                play_mode.distance += 2 * RUN_SPEED_PPS * game_framework.frame_time
            else:
                self.x += RUN_SPEED_PPS * game_framework.frame_time
                play_mode.distance += RUN_SPEED_PPS * game_framework.frame_time
            if self.x >= 2000:
                self.x = 0

    def draw(self):
        if self.x > 800:
            self.image.clip_draw(int(self.x), 0, 2000 - int(self.x), 600, (2000 - int(self.x)) / 2, 300)
            self.image.clip_draw(0, 0, int(self.x) - 800, 600, 1200 - (int(self.x) - 800) / 2, 300)
        else:
            self.image.clip_draw(int(self.x), 0, 1200, 600, 600, 300)

class Fever:
    def __init__(self):
        self.image = load_image('map_background_fever.png')
        self.logo_image = load_image('kick_the_prince.png')
        self.time_count = 0

    def update(self):
        self.time_count += game_framework.frame_time
        if self.time_count > 10:
            play_mode.quest.type = random.randint(1,5)
            if play_mode.quest.type == 1:
                play_mode.quest.goalNum = random.randint(10, 15)
                play_mode.quest.quest_story = f'점프       {play_mode.quest.goalNum}'
            elif play_mode.quest.type == 2:
                play_mode.quest.goalNum = random.randint(5, 10)
                play_mode.quest.quest_story = f'더블 점프  {play_mode.quest.goalNum}'
            elif play_mode.quest.type == 3:
                play_mode.quest.goalNum = random.randint(15, 20)
                play_mode.quest.quest_story = f'적 처치    {play_mode.quest.goalNum}'
            elif play_mode.quest.type == 4:
                play_mode.quest.goalNum = random.randint(200,350)
                play_mode.quest.quest_story = f'달리기     {play_mode.quest.goalNum}'
            elif play_mode.quest.type == 5:
                play_mode.quest.goalNum = 1
                play_mode.quest.quest_story = f'날기       {play_mode.quest.goalNum}'
            play_mode.fever_time = False
            game_world.remove_object(self)

    def draw(self):
        self.image.clip_draw(0, 0, 1200, 600, 600, 300)
        if play_mode.princess.action >= 5 and play_mode.fever_time:
            self.logo_image.clip_draw(0, 0, 600, 300, 600, 300)

