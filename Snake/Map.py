import glfw
from OpenGL.GL import *
import sys

from Snake import easy_shaders as es
from  Snake import  Forms

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

    # Conecting the callback function 'on_key' to handle keyboard events
    # glfw.set_key_callback(window, controller.on_key)

    # Assembling the shader program(pipeline) with both shaders
    pipeline = es.SimpleTransformShaderProgram()

    # Telling Opengl to use our shader program
    glUseProgram(pipeline.shaderProgram)

    # setting up the clear screen color
    glClearColor(0.85, 0.85, 0.85, 1.0)

    # Our shapes here are always full painted
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

    ekans = Forms.Ekans()
    apple = Forms.Apple()

    while not glfw.window_should_close(window):

        # Using GLFW to check for inputs events
        glfw.poll_events()

        # Clearing  the screen in both, color and depth
        glClear(GL_COLOR_BUFFER_BIT)

        # Dibujamos la serpiente
        ekans.draw(pipeline)
        apple.draw(pipeline)

        # Once the render is done, buffers are swapped showing only the complete one
        glfw.swap_buffers(window)

    glfw.terminate()
