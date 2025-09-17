from pico2d import *

open_canvas()

grass=load_image('grass.png')
character=load_image('character.png')

character_x=400
character_y=90

character_width=40
character_height=80

character_speed=2



character.draw_now(character_x, character_y)
grass.draw_now(400, 30)

def move_rectangle():
    if character_x + character_width/2 < 800 and character_y == 90:
        #clear_canvas_now()
        pass

    elif character_x + character_width/2 == 800 and character_y + character_height/2 < 600:
        #clear_canvas_now()
        pass

    elif character_x - character_width/2 > 0 and character_y + character_height/2 == 600:
        #clear_canvas_now()
        pass

    elif character_x - character_width/2 == 0 and character_y > 90:
        #clear_canvas_now()
        pass




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
