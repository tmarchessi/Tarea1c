from Snake import transformations as tr
from Snake import  basic_shapes as bs
from Snake import  scene_graph as sg
from Snake import  easy_shaders as es

class Ekans(object):

    def __init__(self):
        # Figuras basicas

        gpu_head_quad = es.toGPUShape(bs.createColorQuad(1, 0, 1)) # morado
        gpu_eye_quad = es.toGPUShape(bs.createColorQuad(1, 1, 0)) # amarillo
        gpu_neck_quad = es.toGPUShape(bs.createColorQuad(1, 1, 0))  # amarillo
        gpu_body_quad = es.toGPUShape(bs.createColorQuad(1, 0, 1))  # morado
        gpu_tail_quad = es.toGPUShape(bs.createColorQuad(1, 1, 0))  # amarillo

        # Creamos la cabeza

        head = sg.SceneGraphNode('head')
        head.transform = tr.scale(0.125, 0.125, 1)
        head.childs += [gpu_head_quad]

        # Creamos los ojos

        eye = sg.SceneGraphNode('eye') # ojo generico
        eye.transform = tr.scale(0.0225, 0.0225, 1)
        eye.childs += [gpu_eye_quad]

        # Izquierdo

        eye_izq = sg.SceneGraphNode("eyeLeft")
        eye_izq.transform = tr.translate(-0.04, -0.02, 0)
        eye_izq.childs += [eye]

        # Derecho

        eye_der = sg.SceneGraphNode("eyeRight")
        eye_der.transform = tr.translate(0.04, -0.02, 0)
        eye_der.childs += [eye]

        # Creamos el cuello

        neck = sg.SceneGraphNode('neck')
        neck.transform = tr.scale(0.125, 0.0625, 1)
        neck.childs += [gpu_neck_quad]

        fneck = sg.SceneGraphNode("fneck")
        fneck.transform = tr.translate(0, -0.085, 0)
        fneck.childs += [neck]

        # Creamos el cuerpo

        body = sg.SceneGraphNode('body')
        body.transform = tr.scale(0.125, 0.125, 1)
        body.childs += [gpu_body_quad]

        fbody = sg.SceneGraphNode("fbody")
        fbody.transform = tr.translate(0, -0.175, 0)
        fbody.childs += [body]

        # Creamos la cola

        tail = sg.SceneGraphNode('tail')
        tail.transform = tr.scale(0.125, 0.125, 1)
        tail.childs += [gpu_tail_quad]

        ftail = sg.SceneGraphNode("ftail")
        ftail.transform = tr.translate(0, -0.275, 0)
        ftail.childs += [tail]

        # Armamos la serpiente

        cuerpo = sg.SceneGraphNode ('ekans')
        cuerpo.childs += [head, fneck, eye_izq, eye_der, ftail, fbody]

        transform_cuerpo = sg.SceneGraphNode('ekansTR')
        transform_cuerpo.childs += [cuerpo]

        self.model = transform_cuerpo

    def draw(self, pipeline):
        sg.drawSceneGraphNode(self.model, pipeline, "transform")

import random

class Apple(object):

    def __init__(self):
        gpu_apple = es.toGPUShape(bs.createColorQuad(1, 0, 0))

        apple = sg.SceneGraphNode('apple')
        apple.transform = tr.scale(0.060, 0.060, 1)
        apple.childs += [gpu_apple]

        self.pos_y = 1.25
        self.pos_x = 1.25
        self.model = apple

    def draw(self, pipeline):
        sg.drawSceneGraphNode(self.model, pipeline, "transform")