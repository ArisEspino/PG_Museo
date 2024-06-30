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

        # floor
        n, s = 40, 2
        for x in range(-n, n, s):
            for z in range(-n, n, s):
                add(Cube(app, pos=(x, -s, z)))

        add(Modelo(app, pos=(1, -1, -1)))
        add(Statue1(app, pos=(6, -0.6, -6)))
        self.app.positions_monument.append((1, -1))
        self.app.positions_monument.append((6, -6))
        add(Zeus(app, pos=(1, -0.6, -1)))
        # moving cube
        #self.moving_cube = MovingCube(app, pos=(0, 6, 8), scale=(3, 3, 3), tex_id=1)
        #add(self.moving_cube)
