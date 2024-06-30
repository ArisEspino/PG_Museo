import glm
import pygame as pg
from collisions import Collisions

FOV = 50  # deg
NEAR = 0.1
FAR = 100
SPEED = 0.005
SENSITIVITY = 0.08


class Camera:
    def __init__(self, app, position=(20, 2, -10), yaw=-90, pitch=0):
        # position before: (43.62, 1, 27.42)
        self.app = app
        self.aspect_ratio = app.WIN_SIZE[0] / app.WIN_SIZE[1]
        self.position = glm.vec3(position)
        self.up = glm.vec3(0, 1, 0)
        self.right = glm.vec3(1, 0, 0)
        self.forward = glm.vec3(0, 0, -1)
        self.limit = glm.vec2(200, -200)
        self.yaw = yaw
        self.pitch = pitch
        # view matrix
        self.m_view = self.get_view_matrix()
        # projection matrix
        self.m_proj = self.get_projection_matrix()
        #collisions
        self.x = 0
        self.z = 0
        self.collisions = Collisions(self)


    def rotate(self):
        rel_x, rel_y = pg.mouse.get_rel()
        self.yaw += rel_x * SENSITIVITY
        self.pitch -= rel_y * SENSITIVITY
        self.pitch = max(-89, min(89, self.pitch))

    def update_camera_vectors(self):
        yaw, pitch = glm.radians(self.yaw), glm.radians(self.pitch)
        self.forward.x = glm.cos(yaw) * glm.cos(pitch)
        self.forward.y = glm.sin(pitch)
        self.forward.z = glm.sin(yaw) * glm.cos(pitch)
        self.forward = glm.normalize(self.forward)
        self.right = glm.normalize(glm.cross(self.forward, glm.vec3(0, 1, 0)))
        self.up = glm.normalize(glm.cross(self.right, self.forward))

    def update(self):
        self.move()
        self.rotate()
        self.update_camera_vectors()
        self.m_view = self.get_view_matrix()

    def move(self):
        velocity = SPEED * self.app.delta_time
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.x = self.position[0] + self.forward[0] * velocity
            self.z = self.position[2] + self.forward[2] * velocity
            bool_collisions = self.collisions.check_limits()
            if self.limit[0] > self.z > self.limit[1] and self.limit[0] > self.x > self.limit[1] and self.verify():
                self.position[0] = self.x
                self.position[2] = self.z
        if keys[pg.K_s]:
            self.x = self.position[0] - self.forward[0] * velocity
            self.z = self.position[2] - self.forward[2] * velocity
            bool_collisions = self.collisions.check_limits()
            if self.limit[0] > self.z > self.limit[1] and self.limit[0] > self.x > self.limit[1] and self.verify():
                self.position[0] = self.x
                self.position[2] = self.z
        if keys[pg.K_a]:
            self.x = self.position[0] - self.right[0] * velocity
            self.z = self.position[2] - self.right[2] * velocity
            bool_collisions = self.collisions.check_limits()
            if self.limit[0] > self.z > self.limit[1] and self.limit[0] > self.x > self.limit[1] and self.verify():
                self.position[0] = self.x
                self.position[2] = self.z
        if keys[pg.K_d]:
            self.x = self.position[0] + self.right[0] * velocity
            self.z = self.position[2] + self.right[2] * velocity
            bool_collisions = self.collisions.check_limits()
            if self.limit[0] > self.z > self.limit[1] and self.limit[0] > self.x > self.limit[1] and self.verify():
                self.position[0] = self.x
                self.position[2] = self.z
        if keys[pg.K_w] or keys[pg.K_s] or keys[pg.K_a] or keys[pg.K_d]:
            print(self.position)
            self.verify()

    def get_view_matrix(self):
        return glm.lookAt(self.position, self.position + self.forward, self.up)

    def get_projection_matrix(self):
        return glm.perspective(glm.radians(FOV), self.aspect_ratio, NEAR, FAR)

    def verify(self):
        vertices = ([
            [20.4, 9.29],
            [3.72, -0.79],
            [3.47, -19.76],
            [20.15, -29.22],
            [36.78, -19.48],
            [36.94, 0.35],
            [38.39, -0.12],
            [38.114, -20.06],
            [19.96, -31.10],
            [1.74, -20.23],
            [1.80, 0.52],
            [19.48, 11.28]
        ])

        # Definir el punto a verificar
        P = ([self.x, self.z])

        # Función para verificar si un punto está dentro de un polígono
        def is_point_in_polygon(point, vertices):
            n = len(vertices)
            inside = False
            x, z = point
            p1x, p1z = vertices[0]
            for i in range(n + 1):
                p2x, p2z = vertices[i % n]
                if z > min(p1z, p2z):
                    if z <= max(p1z, p2z):
                        if x <= max(p1x, p2x):
                            if p1z != p2z:
                                xinters = (z - p1z) * (p2x - p1x) / (p2z - p1z) + p1x
                            if p1x == p2x or x <= xinters:
                                inside = not inside
                p1x, p1z = p2x, p2z
            return inside

        # Verificar si el punto está dentro del hexágono en el plano 'xz'
        if is_point_in_polygon(P, vertices):
            return False
        else:
            return True