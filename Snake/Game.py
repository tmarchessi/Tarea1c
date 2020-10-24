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
    tale = Formas.Tale()
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
        k = ekans.k

        # Using GLFW to check for inputs events
        glfw.poll_events()

        # Clearing  the screen in both, color and depth
        glClear(GL_COLOR_BUFFER_BIT)
        if ti > f:
            ekans.update(ti)
            k = 1
            f += 0.1
        ekans.loose()
        if k == 1:
            ekans.eat(pos_x, pos_y)
        if x == 1:
            pos_x = random.choice(np.arange(-1 + 1/N, 1 - 1/N, 1/N))
            pos_y = random.choice(np.arange(-1 + 1/N, 1 - 1/N, 1/N))
            if (pos_x == ekans.posicion_x or pos_x == tale.p_x):
                if(pos_y == ekans.posicion_y or pos_y == tale.p_y):
                    pos_x = random.choice(np.arange(-1 + 1 / N, 1 - 1 / N, 1 / N))
                    pos_y = random.choice(np.arange(-1 + 1 / N, 1 - 1 / N, 1 / N))
        if ekans.taleList.__len__() == 1:
            ekans.draw_tale(pipeline)

        else:
            for j in ekans.taleList:
                if ekans.direc == tale.tale_direc:
                    ekans.draw_tale(pipeline)

                else:
                    p = ekans.direc
                    ekans.direc = tale.tale_direc
                    ekans.draw_tale(pipeline)
                    ekans.direc = p
                    tale.tale_direc = p

        # Dibujamos
        apple.draw(pipeline, pos_x, pos_y)
        ekans.draw(pipeline)
        limit.draw(pipeline)

        # Once the render is done, buffers are swapped showing only the complete one
        glfw.swap_buffers(window)

    glfw.terminate()
