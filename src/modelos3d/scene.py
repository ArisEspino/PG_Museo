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

