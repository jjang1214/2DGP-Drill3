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
