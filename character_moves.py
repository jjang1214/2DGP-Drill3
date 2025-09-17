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



character.draw_now(character_x, character_y)
grass.draw_now(glass_x, glass_y)

def clear_and_draw():
    clear_canvas_now()
    grass.draw_now(glass_x, glass_y)
    character.draw_now(character_x, character_y)
    delay(0.01)

def move_rectangle():
    global character_x, character_y

    if character_x + character_width/2 < 800 and character_y == 90:
        character_x += character_speed

        clear_and_draw()

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



def move_circle():
    #clear_canvas_now()
    pass




while True:
    move_rectangle()
    move_triangle()
    move_circle()
