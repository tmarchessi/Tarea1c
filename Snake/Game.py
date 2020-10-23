import glfw
from OpenGL.GL import *
import sys
import random
import numpy as np

from Snake import easy_shaders as es
from Snake import Formas
from Snake import Controller
from Snake import Map

if __name__ == "__main__":

    # Initialize glfw
    if not glfw.init():
        sys.exit()

    width = 800
    height = 800

    window = glfw.create_window(width, height, "Snake", None, None)

    if not window:
        sys.exit()

    glfw.make_context_current(window)

    controlador = Controller.controller()

    # Conecting the callback function 'on_key' to handle keyboard events
    glfw.set_key_callback(window, controlador.on_key)

    # Assembling the shader program(pipeline) with both shaders
    pipeline = es.SimpleTransformShaderProgram()

    # Telling Opengl to use our shader program
    glUseProgram(pipeline.shaderProgram)

    # setting up the clear screen color
    glClearColor(0.85, 0.85, 0.85, 1.0)

    # Our shapes here are always full painted
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

    ekans = Formas.Ekans()
    apple = Formas.Apple()
    limit = Map.Limit()

    controlador.set_model(ekans)
    t0 = 0
    f = 0.1
    pos_x = apple.pos_x
    pos_y = apple.pos_y

    while not glfw.window_should_close(window):
        # Calculamos dt
        ti = glfw.get_time()
        N = Map.Map.N
        x = ekans.x

        # Using GLFW to check for inputs events
        glfw.poll_events()

        # Clearing  the screen in both, color and depth
        glClear(GL_COLOR_BUFFER_BIT)
        if ti > f:
            ekans.update(ti)
            f += 0.1
            print ('f')
            print(apple.pos_x, 'm')
            print(apple.pos_y, 'm')
            print(ekans.posicion_x)
            print(ekans.posicion_y)

        ekans.loose()
        ekans.eat(pos_x, pos_y)
        print(x, 'xxx')
        if x == 1:
            pos_x = random.choice(np.arange(-1 + 1/N, 1 - 1/N, 1/N))
            pos_y = random.choice(np.arange(-1 + 1/N, 1 - 1/N, 1/N))
            print(pos_x, 'x')
            print(pos_y, 'y')

        # Dibujamos
        apple.draw(pipeline, pos_x, pos_y)
        ekans.draw(pipeline)
        limit.draw(pipeline)
        print(x, 'x')

        # Once the render is done, buffers are swapped showing only the complete one
        glfw.swap_buffers(window)

    glfw.terminate()
