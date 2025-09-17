from pico2d import *

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
    global character_x, character_y, move_rect

    if character_x + character_width/2 < 800 and character_y == 90:
        character_x += character_speed

        clear_and_draw()

        if character_x == 400:
            move_rect=True

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



move_cir=False

def move_circle():
    global character_x, character_y, move_cir, angle




while True:
    if not move_rect:
        move_rectangle()

    # move_triangle()
    # move_circle()
