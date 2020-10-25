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

    # Assembling the shader program (pipeline2) with both shaders
    pipeline2 = es.SimpleTextureTransformShaderProgram()

    # setting up the clear screen color
    glClearColor(0.85, 0.85, 0.85, 1.0)

    # Our shapes here are always full painted
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

    ekans = Formas.Ekans()
    defeat = Map.Defeat()
    apple = Formas.Apple()
    limit = Map.Limit()
    grasp = Map.Grasp()

    controlador.set_model(ekans)
    t0 = 0
    f = 0.1
    pos_x = apple.pos_x
    pos_y = apple.pos_y

    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    while not glfw.window_should_close(window):
        # Telling Opengl to use our shader program
        glUseProgram(pipeline.shaderProgram)

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
            k = 1
            ekans.loose()
            if k == 1:
                ekans.eat(pos_x, pos_y)
            if x == 1:
                pos_x = random.choice(np.arange(-1 + 1/N, 1 - 1/N, 1/N))
                pos_y = random.choice(np.arange(-1 + 1/N, 1 - 1/N, 1/N))
                for v in ekans.taleList:
                    if (pos_x == ekans.posicion_x or pos_x == v.p_x):
                        if(pos_y == ekans.posicion_y or pos_y == v.p_y):
                            pos_x = random.choice(np.arange(-1 + 1 / N, 1 - 1 / N, 1 / N))
                            pos_y = random.choice(np.arange(-1 + 1 / N, 1 - 1 / N, 1 / N))
            if len(ekans.taleList) >= 0:
                ekans.replace(ti)
            f += 0.1

        # Dibujamos
        apple.draw(pipeline, pos_x, pos_y)
        limit.draw(pipeline)
        print(ekans.h)

        glUseProgram(pipeline2.shaderProgram)
        ekans.draw_tale(pipeline2)
        ekans.draw(pipeline2)
        if ekans.h == 0:
            defeat.draw(pipeline2)


        # Once the render is done, buffers are swapped showing only the complete one
        glfw.swap_buffers(window)

    glfw.terminate()
