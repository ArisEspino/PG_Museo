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

        # cat
        add(Cat(app, pos=(0, -1, -10)))
##        add(Cesped(app, pos=(0, 1, -10)))
##        add(detalles(app, pos=(0, -1, -10)))
##
