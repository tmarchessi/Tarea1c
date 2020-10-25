from Snake import transformations as tr
from Snake import  basic_shapes as bs
from Snake import  scene_graph as sg
from Snake import  easy_shaders as es
from Snake import Map
import numpy as np
from typing import List
from OpenGL.GL import *

class Tale(object):
    N = Map.Map.N

    def __init__(self, p_x, p_y):
        self.o = 1
        gpu_tale_quad = es.toGPUShape(
            bs.createTextureQuad('cuerpo.new.png'), GL_REPEAT, GL_NEAREST)  # celeste

        # Creamos la cola
        tale = sg.SceneGraphNode('tale')
        tale.transform = tr.scale(1 / self.N, 1 / self.N, 1)
        tale.childs += [gpu_tale_quad]

        tale_tr = sg.SceneGraphNode("taleTR")
        tale_tr.childs += [tale]

        self.p_x = p_x
        self.p_y = p_y
        self.model = tale_tr

    def draw(self, pipeline):
        self.model.transform = tr.translate(self.p_x, self.p_y, 0)
        sg.drawSceneGraphNode(self.model, pipeline, "transform")

    def tale_direc(self):
        self.tale_direc = 1

class Ekans(object):
    N = Map.Map.N
    taleList: List['Tale']

    def __init__(self):
        self.h = 1
        self.k = 1
        self.x = 0
        self.taleList = []
        # Figuras basicas

        gpu_head_quad = es.toGPUShape(
            bs.createTextureQuad('caeza.png'), GL_REPEAT, GL_NEAREST)  # morado


        # Creamos la cabeza

        head = sg.SceneGraphNode('head')
        head.transform = tr.scale(1/self.N, 1/self.N, 1)
        head.childs += [gpu_head_quad]

        # Armamos la serpiente

        ekans = sg.SceneGraphNode ('ekans')
        self.transform_ekans = sg.SceneGraphNode('ekansTR')
        self.transform_ekans.childs += [head]


        self.posicion_x = 1/self.N
        self.posicion_y = 1/self.N
        self.model = self.transform_ekans

    def direc(self):
        self.direc = 1


    def draw(self, pipeline):
        px = self.posicion_x
        py = self.posicion_y
        self.model.transform = tr.translate(px, py, 0)
        sg.drawSceneGraphNode(self.model, pipeline, "transform")


    def update(self, ti):

        if self.direc == 1:

            self.posicion_y += 1/self.N

        elif self.direc == -1:

            self.posicion_y -= 1/self.N

        elif self.direc == 0:

            self.posicion_x -= 1/self.N

        elif self.h == 0:
            self.posicion_x += 0
            self.posicion_y += 0

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
            self. h = 0

        for h in self.taleList:
            if (self.posicion_x >= h.p_x - self.N / 1000 and self.posicion_x <= h.p_x + self.N / 1000):
                if (self.posicion_y >= h.p_y - self.N / 1000 and self.posicion_y <= h.p_y + self.N / 1000):
                    print("perdiste")
                    self.h = 0


    def eat(self, pos_x, pos_y):
        self.x = 0
        if(self.posicion_x >= pos_x - self.N/1000 and self.posicion_x <= pos_x + self.N/1000):
            if(self.posicion_y >= pos_y - self.N/1000 and self.posicion_y <= pos_y + self.N/1000):
                self.x = 1
                if len(self.taleList) == 0:
                    self.taleList.append((Tale(self.posicion_x, self.posicion_y)))
                    self.k += 1

                else:
                    q = self.taleList[len(self.taleList) - 1]
                    self.taleList.append((Tale(q.p_x, q.p_y)))
        self.k = 0
        return self.x


    def replace(self, ti):
        x = self.posicion_x
        y = self.posicion_y
        self.update(ti)
        for j in range(0, len(self.taleList)):
            save_x = self.taleList[j].p_x
            save_y = self.taleList[j].p_y
            self.taleList[j].p_x = x
            self.taleList[j].p_y = y
            x = save_x
            y = save_y

    def draw_tale(self, pipeline):
        for j in self.taleList:
            j.draw(pipeline)

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





