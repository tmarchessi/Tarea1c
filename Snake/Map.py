from Snake import transformations as tr
from Snake import  basic_shapes as bs
from Snake import  scene_graph as sg
from Snake import  easy_shaders as es
from OpenGL.GL import *
import numpy as np

class Map:
    N = input("Valor de N")
    N = int(N)

class Limit:
    N = Map.N

    def __init__(self):
        gpu_limit_quad = es.toGPUShape(bs.createColorQuad(0, 0, 0))  # negro

        # Creamos el limite

        limit = sg.SceneGraphNode('grasp')
        limit.transform = tr.scale(1/self.N, 1/self.N, 1)
        limit.childs += [gpu_limit_quad]

        limit_tr = sg.SceneGraphNode("limitTR")
        limit_tr.childs += [limit]

        self.model = limit_tr

    def draw(self, pipeline):
        for px in np.arange(-1, 1 + 1/self.N, 1/self.N):
            for py in (-1, 1):
                self.model.transform = tr.translate(px, py, 0)
                sg.drawSceneGraphNode(self.model, pipeline, "transform")

        for py in np.arange(-1, 1 , 1/self.N):
            for px in (-1, 1):
                self.model.transform = tr.translate(px, py, 0)
                sg.drawSceneGraphNode(self.model, pipeline, "transform")


class Defeat:
    N = Map.N
    def __init__(self):
        gpu_defeat_quad = es.toGPUShape(
            bs.createTextureQuad('gameover.png'), GL_REPEAT, GL_NEAREST)

        # Creamos el cartel

        defeat = sg.SceneGraphNode('grasp')
        defeat.transform = tr.scale(10/self.N, 10/self.N, 1)
        defeat.childs += [gpu_defeat_quad]

        defeat_tr = sg.SceneGraphNode("limitTR")
        defeat_tr.childs += [defeat]

        self.model = defeat_tr


    def draw(self, pipeline):
        self.model.transform = tr.translate(0, 0, 0)
        sg.drawSceneGraphNode(self.model, pipeline, "transform")