#이벤트 체크 함수 정의
from sdl2 import SDL_KEYDOWN, SDLK_SPACE, SDLK_c

def start_event(e):
    return e[0] == 'START'

def time_out(e):
    return e[0] == 'TIME_OUT'

def space_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_SPACE

def c_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_c

def hit_object(e):
    return e[0] == 'HIT'

def jump(e):
    return e[0] == 'JUMP'

def death(e):
    return e[0] == 'DEATH'

def fall(e):
    return e[0] == 'FALL'

def fly_item(e):
    return e[0] == 'FLY_ITEM'

class StateMachine:
    def __init__(self, obj):
        self.obj = obj
        self.event_q = []
    def start(self, state):
        self.cur_state = state
        self.cur_state.enter(self.obj, ('START', 0))
    def update(self):
        self.cur_state.do(self.obj)
        if self.event_q:
            e = self.event_q.pop(0)
            for check_event, next_state in self.transitions[self.cur_state].items():
                if check_event(e):
                    self.cur_state.exit(self.obj, e)
                    self.cur_state = next_state
                    self.cur_state.enter(self.obj, e)
                    return
    def draw(self):
        self.cur_state.draw(self.obj)
    def add_event(self, e):
        self.event_q.append(e)
    def set_transitions(self, transitions):
        self.transitions = transitions