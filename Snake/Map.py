from Snake import transformations as tr
from Snake import  basic_shapes as bs
from Snake import  scene_graph as sg
from Snake import  easy_shaders as es
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

class Grasp:
    N = Map.N

    def __init__(self):
        gpu_grasp_quad = es.toGPUShape(bs.createColorQuad(0, 1, 0))  # verde

        # Creamos el pasto

        grasp = sg.SceneGraphNode('grasp')
        grasp.transform = tr.scale(1 / self.N, 1 / self.N, 1)
        grasp.childs += [gpu_grasp_quad]

        grasp_tr = sg.SceneGraphNode("graspTR")
        grasp_tr.childs += [grasp]

        self.model = grasp_tr

        # Creamos el pasto

    def draw(self, pipeline):
        for px in np.arange(-1 + 1 / self.N, 1 - 1 / self.N, 1 / self.N):
            for py in (-1, 1):
                self.model.transform = tr.translate(px, py, 0)
                sg.drawSceneGraphNode(self.model, pipeline, "transform")

        for py in np.arange(-1 + 1 / self.N, 1 - 1 / self.N, 1 / self.N):
            for px in (-1, 1):
                self.model.transform = tr.translate(px, py, 0)
                sg.drawSceneGraphNode(self.model, pipeline, "transform")