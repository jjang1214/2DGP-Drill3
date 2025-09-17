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

character_speed=10


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
    global character_x, character_y, move_rect, move_tri

    if character_x + character_width/2 < 800 and character_y == 90:
        character_x += character_speed

        clear_and_draw()

        if character_x == 400:
            move_rect=True
            move_tri=False

    elif character_x + character_width/2 == 800 and character_y + character_height/2 < 600:
        character_y += character_speed

        clear_and_draw()

    elif character_x - character_width/2 > 0 and character_y + character_height/2 == 600:
        character_x -= character_speed

        clear_and_draw()

    elif character_x - character_width/2 == 0 and character_y > 90:
        character_y -= character_speed

        clear_and_draw()



tri_a=[400,500]
tri_b=[200,90]
tri_c=[600,90]

triangle=[tri_a, tri_b, tri_c]
index=1

tri_t=0.05
count=int(1/tri_t)

start_x,start_y=character_x,character_y

move_tri=True

def move_triangle():
    global character_x, character_y, index, tri_t, count, start_x, start_y, move_tri, move_cir

    target_x, target_y = triangle[index]

    character_x=character_x+(target_x-start_x)*tri_t
    character_y=character_y+(target_y-start_y)*tri_t
    count-=1

    clear_and_draw()

    #print(character_x, character_y)


    if count==0:
        count=1/tri_t
        index-=1
        start_x,start_y=character_x,character_y
        #print('도착')

        if index == -1:
            index=2

    if character_x==400 and character_y==90:
        index = 1
        move_tri = True
        move_cir = False





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
    if not move_rect and move_tri and move_cir:
        move_rectangle()

    elif move_rect and not move_tri and move_cir:
        move_triangle()

    elif move_rect and move_tri and not move_cir:
        move_circle()
