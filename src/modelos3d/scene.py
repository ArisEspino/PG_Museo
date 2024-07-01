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

        #aca se edita la pos donde estara el obj
        add(Cat(app, pos=(0, -1, -10)))
        add(Fuente(app, pos=(-5, -1, -4)))
        add(Mesa(app, pos=(0.1, -1, -15))) #esta es de las mesas
        add(Face1(app, pos=(0.1, 0.05, -15)))#esta es la first cara sobre la mesa y aca tambien esta la escala
        add(Mesa(app, pos=(-4.5, -1, -12.5)))  # esta es de las mesas
        add(Face2(app, pos=(-4.6, 0, -12.5)))  # esta es la 2da cara
        add(Mesa(app, pos=(-4.5, -1, -7.2)))  # esta es de las mesas
        add(Sol(app, pos=(-4.5, 0, -7.2)))  # soldado a reparar
        add(Mesa(app, pos=(4.5, -1, -12.2)))  # esta es de las mesas
        add(Cab(app, pos=(4.5, 0.2, -12.5))) #cabeza2
        #aca van los otros modelos internos

        add(Her(app, pos=(-2, -1, -14))) #cuadro
        add(Mujer(app, pos=(-4.6, 0, -8.5)))#mujer
        #leon 1/8
        add(Leon(app, pos=(2, 0, -13.5)))
        add(M2(app, pos=(-2, -1, -6))) #al lado del sol
        add(M3(app, pos=(4, -1, -10))) #al lado del dios
        add(M1(app, pos=(-4.6, -1, -10.5)))#al lado de la mujer
        #centro del museo
        add(M4(app, pos=(-1, -1, -9.5)))
        add(M5(app, pos=(2, -1, -10)))

        add(Tree(app, pos=(-6, -1, -3)))
        add(Tree(app, pos=(12, -1, -3)))#dm
        add(Tree(app, pos=(-8, -1, 1)))
        add(Tree(app, pos=(14, -1, 1)))
        add(Tree(app, pos=(-3, -1, -3))) #1
        add(Tree(app, pos=(16, -1, -3)))
        add(Tree(app, pos=(-4.5, -1, 1.5)))#2
        add(Tree(app, pos=(18, -1, 1)))
        add(Tree(app, pos=(19, -1, -4)))
        add(Tree(app, pos=(-1, -1, 1)))
        add(Choza(app, pos=(-9, -1, -6)))#chozaa
        add(Choza(app, pos=(9.8, -1, -6)))  # chozaa

        #x,y,z


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

