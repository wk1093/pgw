from pgw.__version import *
print(version)
import pygame
pygame.init()

################## GLOBALS ##################

width, height, clock, win = None, None, None, None

################## CONSTANTS ##################

QUIT = pygame.QUIT
from pgw.__keys import *

################## CUSTOM METHODS ##################

def setup(t, w, h):
    global win, width, height, clock
    width = w
    height = h
    win = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    pygame.display.set_caption(version+" - "+t)

def should_run():
    for event in event_get():
        if event.type == QUIT:
            return False
    return True

def load_animation(prefix, frames, suffix):
    tmp = []
    for el in frames:
        tmp.append(load_image(prefix+str(el)+suffix))
    return tmp

################## WRAPPER METHODS ##################

def system_font(a, b, c=None):
    if c is None:
        return pygame.font.SysFont(a, b)
    else:
        return pygame.font.SysFont(a, b, c)

def load_sound(sound):
    return pygame.mixer.Sound(sound)

def load_music(music):
    return pygame.mixer.music.load(music)

def play_music(num):
    return pygame.mixer.music.play(num)

def tick(n):
    clock.tick(n)

def draw(img, x, y):
    return win.blit(img, (x, y))

def clear_screen(r, g, b):
    return win.fill((r, g, b))

def load_image(filename):
    return pygame.image.load(filename)

def key_pressed(key):
    return pygame.key.get_pressed()[key]

def wait_ms(ms):
    return pygame.time.delay(ms)

def event_get():
    return pygame.event.get()

def draw_rect(color, rect, c=None):
    if c is None:
        return pygame.draw.rect(win, color, rect)
    else:
        return pygame.draw.rect(win, color, rect, c)

def draw_circle(a, b, c):
    return pygame.draw.circle(win, a, b, c)

def update():
    return pygame.display.update()

def quit():
    return pygame.quit()

################## END ##################
