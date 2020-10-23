from Snake import transformations as tr
from Snake import  basic_shapes as bs
from Snake import  scene_graph as sg
from Snake import  easy_shaders as es
from Snake import Map
import numpy as np
from typing import List

class Ekans(object):
    N = Map.Map.N

    def __init__(self):
        extend: List['Ekans']
        self.x = 0

        self.body = []
        # Figuras basicas

        gpu_head_quad = es.toGPUShape(bs.createColorQuad(1, 0, 1))  # morado
        gpu_body_quad = es.toGPUShape(bs.createColorQuad(1, 0, 1))  # amarillo

        # Creamos la cabeza

        head = sg.SceneGraphNode('head')
        head.transform = tr.scale(1/self.N, 1/self.N, 1)
        head.childs += [gpu_head_quad]

        # Creamos el cuerpo

        body = sg.SceneGraphNode('body')
        body.transform = tr.scale(1/self.N, 1/self.N, 1)
        body.childs += [gpu_body_quad]

        # Armamos la serpiente

        ekans = sg.SceneGraphNode ('ekans')

        transform_ekans = sg.SceneGraphNode('ekansTR')
        transform_ekans.childs += [head]

        self.posicion_x = 1/self.N
        self.posicion_y = 1/self.N
        self.model = transform_ekans

    def direc(self):
        self.direc = 1


    def draw(self, pipeline):
        self.model.transform = tr.translate(self.posicion_x, self.posicion_y, 0)
        sg.drawSceneGraphNode(self.model, pipeline, "transform")


    def update(self, ti):

        if self.direc == 1:

            self.posicion_y += 1/self.N

        elif self.direc == -1:

            self.posicion_y -= 1/self.N

        elif self.direc == 0:

            self.posicion_x -= 1/self.N

        else:
            self.posicion_x += 1/self.N

    def move_up(self):
        self.direc = 1

    def move_down(self):
        self.direc = -1

    def move_left(self):
        self.direc = 0

    def move_right(self):
        self.direc = 2

    def loose(self):
        if(self.posicion_x <= -1 or self.posicion_x >= 1 or
           self.posicion_y <= -1 or self.posicion_y >= 1):
            print("perdiste")

    def eat(self, pos_x, pos_y):
        self.x = 0
        apples = Apple()
        if(self.posicion_x >= pos_x - 0.02 and self.posicion_x <= pos_x + 0.02):
            if(self.posicion_y >= pos_y - 0.02 and self.posicion_y <= pos_y + 0.02):
                print("comer")
                self.x = 1
        else:
            print (self.posicion_x, self.posicion_y, 's')
            print (apples.pos_x, apples.pos_y, 'm')

        print (self.x, 'xx')
        return self.x

import random

class Apple(object):

    N = Map.Map.N

    def __init__(self):
        gpu_apple = es.toGPUShape(bs.createColorQuad(1, 0, 0))  # rojo

        # Creamos las manzana

        apple = sg.SceneGraphNode('apple')
        apple.transform = tr.scale(1/self.N, 1/self.N, 1)
        apple.childs += [gpu_apple]

        apple_tr = sg.SceneGraphNode("appleTR")
        apple_tr.childs += [apple]

        self.pos_y = random.choice(np.arange(-1 + 1/self.N, 1 - 1/self.N, 1/self.N))
        self.pos_x = random.choice(np.arange(-1 + 1/self.N, 1 - 1/self.N, 1/self.N))
        self.model = apple_tr

    def draw(self, pipeline, pos_x, pos_y):
        self.model.transform = tr.translate(pos_x, pos_y, 0)
        sg.drawSceneGraphNode(self.model, pipeline, "transform")

