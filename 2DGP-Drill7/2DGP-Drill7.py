from pico2d import *
import random


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(400, 30)


class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


class Ball:
    def __init__(self):
        self.x = random.randint(50, 750)
        self.y = 599
        self.speed = random.randint(5, 15)
        if random.choice([True, False]):
            self.image = load_image('ball21x21.png')
            self.size = 21
        else:
            self.image = load_image('ball41x41.png')
            self.size = 41

    def update(self):
        if self.y > 30 + self.size // 2:
            self.y -= self.speed
        else:
            self.y = 30 + self.size // 2

    def draw(self):
        self.image.draw(self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def update_world():
    grass.update()
    for boy in team:
        boy.update()
    for ball in balls:
        ball.update()


def render_world():
    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    for ball in balls:
        ball.draw()
    update_canvas()


def reset_world():
    global running, grass, team, balls
    running = True
    grass = Grass()
    team = [Boy() for _ in range(11)]
    balls = [Ball() for _ in range(20)]


open_canvas()
reset_world()

while running:
    handle_events()
    update_world()
    render_world()
    delay(0.016)

close_canvas()
