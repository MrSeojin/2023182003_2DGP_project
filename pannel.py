from pico2d import *

import game_framework
import play_mode
import title_mode

sound_names = ['play', 'mute']

class Pannel:
    bgm_image = {}
    sound_image = {}
    def __init__(self):
        self.click = 3
        self.hand = load_image("click.png")
        self.image = load_image('menu_frame.png')
        for state in sound_names:
            Pannel.bgm_image[state] = load_image("bgm_" + state + ".png")
            Pannel.sound_image[state] = load_image("sound_" + state + ".png")

    def draw(self):
        self.image.draw(600, 300)
        Pannel.bgm_image[play_mode.bgm_play].draw(400, 500)
        Pannel.sound_image[play_mode.sound_play].draw(800, 500)
        if self.click == 0:
            self.hand.draw(450, 450)
        elif self.click == 1:
            self.hand.draw(850, 450)
        elif self.click == 2:
            self.hand.draw(550, 200)
        elif self.click == 3:
            self.hand.draw(650, 200)
        elif self.click == 4:
            self.hand.draw(750, 200)

    def update(self):
        pass

    def handle_event(self, event):
        if event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
            self.click = (self.click - 1) % 5
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
            self.click = (self.click + 1) % 5
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            if self.click == 0:
                if play_mode.bgm_play=='play':
                    play_mode.bgm_play = 'mute'
                    play_mode.background.sound.set_volume(0)
                else:
                    play_mode.bgm_play = 'play'
                    play_mode.background.sound.set_volume(32)
            elif self.click == 1:
                if play_mode.sound_play == 'play':
                    play_mode.sound_play = 'mute'
                else:
                    play_mode.sound_play = 'play'
            elif self.click == 2:
                game_framework.pop_mode()
            elif self.click == 3:
                game_framework.change_mode(play_mode)
            elif self.click == 4:
                game_framework.change_mode(title_mode)
