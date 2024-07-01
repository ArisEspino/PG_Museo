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

        # Objetos
        add(Cat(app, pos=(0, -0.9, -5)))
        add(Mesa(app, pos=(-0.3, -0.9, -4.3)))
        add(Jarra(app, pos=(-0.5, -0.53, -4.4)))
        add(Plato(app, pos=(0.5, -0.52, -4.4)))

        # Estatuas
        add(Head(app, pos=(0, -0.3, -5)))
        self.app.positions_monument.append((0, -5))         # Ananke 0

        add(Herku(app, pos=(-2.5, -0.25, -7.6)))
        self.app.positions_monument.append((-2.5, -7.6))    # Hercules 1

        add(Woman(app, pos=(2.5, -0.90, -7.6)))
        self.app.positions_monument.append((2.5, -7.6))       # Afrodita 2

        add(Man(app, pos=(0, -0.90, -7.6)))
        self.app.positions_monument.append((0, -7.6))       # Man 3

        add(Orar(app, pos=(-2.5, -0.80, -4.5)))
        self.app.positions_monument.append((-2.5, -4.5))    # statue 4

        add(Mujer(app, pos=(2.5, -0.90, -4.5)))
        self.app.positions_monument.append((2.5, -4.5))    # Mujer 5

        add(Ate(app, pos=(2.5, -0.9, -2.5)))
        self.app.positions_monument.append((2.5, -2.5))    # Atenea 6

        add(Zeus(app, pos=(-2.5, -0.90, -2.5)))
        self.app.positions_monument.append((-2.5, -2.5))    # Zeus 7
