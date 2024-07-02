from model import *
import glm
import math
import random


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

        # aca se edita la pos donde estara el obj
        add(Cat(app, pos=(0, -0.9, -5)))
        add(Jarra(app, pos=(-0.5, -0.53, -4.4)))
        add(Plato(app, pos=(0.5, -0.52, -4.4)))
        add(Mesa(app, pos=(-0.3, -0.9, -4.3)))

        # Estatuas
        add(Head(app, pos=(0, -0.3, -5)))
        self.app.positions_monument.append((0, -5))             # 0
        add(Herku(app, pos=(-2.5, -0.25, -7.6)))
        self.app.positions_monument.append((-2.5, -7.6))        # 1
        add(Woman(app, pos=(2.5, -0.90, -7.6)))
        self.app.positions_monument.append((2, -7.6))           # 2
        add(Man(app, pos=(0, -0.90, -7.6)))
        self.app.positions_monument.append((0, -7.6))           # 3
        add(Orar(app, pos=(-2.5, -0.80, -4.5)))
        self.app.positions_monument.append((-2.5, -4.5))        # 4
        add(Mujer(app, pos=(2.5, -0.90, -4.5)))
        self.app.positions_monument.append((2.5, -4.5))         # 5
        add(Ate(app, pos=(2.5, 0.48, -2.5)))
        self.app.positions_monument.append((2.5, -2.5))         # 6
        add(Zeus(app, pos=(-2.5, -0.90, -2.5)))
        self.app.positions_monument.append((-2.5, -2.5))        # 7

        #garden part
        add(Wall(app, pos=(0, -1, 5)))
        add(Statue(app, pos=(0, -1, 5)))
        add(Rose(app, pos=(0, -1, 5)))
        #garden pt2
        add(Pool(app, pos=(0, -1.3, 5)))
        add(Col(app, pos=(2.3, -1, 6.5)))
        add(Col(app, pos=(-2, -1, 6.5)))
        add(Mari(app, pos=(-2, -0.4, 6.5)))
        add(Mari(app, pos=(2.3, -0.4, 6.5)))
        num_objects = 10
        radius = 1

        # Calcular la posición de cada objeto en el círculo
        for i in range(num_objects):
            angle = (2 * math.pi / num_objects) * i
            x = radius * math.cos(angle)
            z = 5 + radius * math.sin(angle)
            y = -1
            angle = random.choice([90, 180, 120])
            add(Stigma(app, pos=(x, -1, z), rot=(0, angle, 0)))
            add(Stem(app, pos=(x, -1, z), rot=(0, angle, 0)))
            add(Grass(app, pos=(x, -1, z), rot=(0, angle, 0)))
            add(Leaf(app, pos=(x, -1, z), rot=(0, angle, 0)))
            add(Petal(app, pos=(x, -1, z), rot=(0, angle, 0)))

            add(Ground(app, pos=(0, -1, 6.5)))
            z = 7
        for i in range(4):
            add(Trunk(app, pos=(0, -1, z)))
            add(LeavesTree(app, pos=(0, -1, z)))
            z -= 1
