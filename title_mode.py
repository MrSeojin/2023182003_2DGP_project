import game_framework
from pico2d import*

import play_mode

def init():
    global image
    global title_sound
    image = load_image('title.png')
    title_sound = load_music('title_sound.mp3')
    title_sound.set_volume(32)
    title_sound.repeat_play()

def finish():
    global image
    global title_sound
    del image
    del title_sound

def update():
    pass

def draw():
    clear_canvas()
    image.draw(600, 300)
    update_canvas()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.change_mode(play_mode)

def pause():
    pass

def resume():
    pass