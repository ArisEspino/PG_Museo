from model import *
import glm


class Scene:
    def __init__(self, app):
        self.app = app
        self.objects = []
        self.load()
        # skybox
        self.skybox = AdvancedSkyBox(app)

    def add_object(self, obj):
        self.objects.append(obj)

    def load(self):
        app = self.app
        add = self.add_object

        # forrr cube/piso
        n, s = 15, 2
        for x in range(-n, n, s):
            for z in range(-n, n, s):
                add(Cube(app, pos=(x, -s, z)))

#aca se edita la pos donde estara el obj
        add(Cat(app, pos=(0, -0.9, -5)))
        add(Head(app, pos=(0, -0.3, -5)))
        add(Mesa(app, pos=(-0.3, -0.9, -4.3)))
        add(Herku(app, pos=(-2.5, -0.25, -7.6)))
        add(Woman(app, pos=(2.5, -0.90, -7.6)))
        add(Man(app, pos=(0, -0.90, -7.6)))
        add(Jarra(app, pos=(-0.5, -0.53, -4.4)))
        add(Plato(app, pos=(0.5, -0.52, -4.4)))
        add(Orar(app, pos=(-2.5, -0.80, -4.5)))
        add(Mujer(app, pos=(2.5, -0.90, -4.5)))
        add(Ate(app, pos=(2.5, -0.2, -2.5)))
        add(Zeus(app, pos=(-2.5, -0.90, -2.5)))
