import glfw

class controller():
    model = 'Ekans'

    def __init__(self):
        self.model = None

    def set_model(self, m):
        self.model = m

    def on_key(self, window, key, scancode, action, mods):
        if not(action ==glfw.PRESS or action == glfw.RELEASE):
            return

        elif key == glfw.KEY_W or key == glfw.KEY_UP:
            print("move up")
            self.model.move_up()

        elif key == glfw.KEY_D or key == glfw.KEY_RIGHT:
            print("move right")
            self.model.move_right()

        elif key == glfw.KEY_S or key == glfw.KEY_DOWN:
            print("move down")
            self.model.move_down()

        elif key == glfw.KEY_A or key == glfw.KEY_LEFT:
            print("move left")
            self.model.move_left()

        else:
            print("Unknow key")

