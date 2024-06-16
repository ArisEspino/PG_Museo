import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

# Clase para cargar y renderizar un modelo .obj
class OBJ:
    def __init__(self, filename, scale=1.0):
        self.vertices = []
        self.faces = []

        with open(filename, 'r') as f:
            for line in f:
                if line.startswith('v '):
                    self.vertices.append(list(map(float, line.strip().split()[1:4])))
                elif line.startswith('f '):
                    face = []
                    for vert in line.strip().split()[1:]:
                        face.append(int(vert.split('/')[0]) - 1)
                    self.faces.append(face)

        self.vertices = np.array(self.vertices, dtype='float32') * scale

    def render(self):
        glBegin(GL_TRIANGLES)
        for face in self.faces:
            for vertex in face:
                glVertex3fv(self.vertices[vertex])
        glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    obj = OBJ('thismuseo.obj', scale=0.1)  # Ajusta la escala según tus necesidades

    clock = pygame.time.Clock()
    rotation = [0, 0]
    mouse_down = False
    last_mouse_pos = None

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_down = True
                    last_mouse_pos = pygame.mouse.get_pos()
            elif event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    mouse_down = False
            elif event.type == MOUSEMOTION:
                if mouse_down:
                    x, y = pygame.mouse.get_pos()
                    dx = x - last_mouse_pos[0]
                    dy = y - last_mouse_pos[1]
                    rotation[0] += dy
                    rotation[1] += dx
                    last_mouse_pos = (x, y)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
        glTranslatef(0.0, 0.0, -5)
        glRotatef(rotation[0], 1, 0, 0)
        glRotatef(rotation[1], 0, 1, 0)
        obj.render()
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
