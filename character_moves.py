from pico2d import *
from math import *

open_canvas()

grass=load_image('grass.png')
character=load_image('character.png')

glass_x=400
glass_y=30

character_x=400
character_y=90

character_width=40
character_height=80

character_speed=2


center_x=400
center_y=300
angle=270
r=center_y-character_y


character.draw_now(character_x, character_y)
grass.draw_now(glass_x, glass_y)

def clear_and_draw():
    clear_canvas_now()
    grass.draw_now(glass_x, glass_y)
    character.draw_now(character_x, character_y)
    delay(0.01)


move_rect=False

def move_rectangle():
    global character_x, character_y, move_rect, move_cir

    if character_x + character_width/2 < 800 and character_y == 90:
        character_x += character_speed

        clear_and_draw()

        if character_x == 400:
            move_rect=True
            move_cir=False

    elif character_x + character_width/2 == 800 and character_y + character_height/2 < 600:
        character_y += character_speed

        clear_and_draw()

    elif character_x - character_width/2 > 0 and character_y + character_height/2 == 600:
        character_x -= character_speed

        clear_and_draw()

    elif character_x - character_width/2 == 0 and character_y > 90:
        character_y -= character_speed

        clear_and_draw()




def move_triangle():
    #clear_canvas_now()
    pass



move_cir=True

def move_circle():
    global character_x, character_y, move_rect, move_cir, angle

    character_x = center_x + r * cos(radians(angle))
    character_y = center_y + r * sin(radians(angle))

    angle -= character_speed / 2
    if angle <= 0:
        angle = 360

    clear_and_draw()

    if angle == 270:
        move_rect = False
        move_cir = True

        character_x = 400
        character_y = 90




while True:
    if not move_rect and move_cir:
        move_rectangle()

    # move_triangle()

    elif move_rect and not move_cir:
        move_circle()
