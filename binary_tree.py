#二叉树

import math
import pyglet

width = 800
height = 600
delta_angle = math.pi/12
init_angle = math.pi/2
branch_length = 50
vertex = []

def draw_branch(number, direction, previous_vertex, previous_angle):
    if number > 0:
        current_angle = 0
        if direction == 'left':
            current_angle = previous_angle + delta_angle
        else:
            current_angle = previous_angle - delta_angle

        current_vertex = []
        current_vertex.append(previous_vertex[0] + branch_length * math.cos(current_angle))
        current_vertex.append(previous_vertex[1] + branch_length * math.sin(current_angle))
        vertex.append(previous_vertex)
        vertex.append(current_vertex)
        draw_branch(number - 1, 'left', current_vertex, current_angle)
        draw_branch(number - 1, 'right', current_vertex, current_angle)
    
def draw_tree(number):
    #初始位置
    init_vertex_start = [width/2, height/2]
    init_vertex_end = [init_vertex_start[0] + branch_length * math.cos(init_angle),
                       init_vertex_start[1] + branch_length * math.sin(init_angle)]
    vertex.append(init_vertex_start)
    vertex.append(init_vertex_end)
    draw_branch(number, 'left', init_vertex_end, init_angle)
    draw_branch(number, 'right', init_vertex_end, init_angle)



draw_tree(5)
vertex_list = []
for v in vertex:
    vertex_list.extend(v)
    
window = pyglet.window.Window(width=width, height=height)

@window.event
def on_draw():
    window.clear()
    pyglet.graphics.draw(len(vertex_list)//2,
                         pyglet.gl.GL_LINES,
                         ('v2f', vertex_list))
pyglet.app.run()



#to add some random factors 
