import time

import glm
import pygame as pg
from math import sqrt
from collisions import Collisions
from collisions import Collisions_two

FOV = 50  # deg
NEAR = 0.1
FAR = 100
SPEED = 0.005
SENSITIVITY = 0.08


class Camera:
    def __init__(self, app, position=(-0.06, 0, 2.72), yaw=-90, pitch=0):
        self.app = app
        self.aspect_ratio = app.WIN_SIZE[0] / app.WIN_SIZE[1]
        self.position = glm.vec3(position)
        self.up = glm.vec3(0, 1, 0)
        self.right = glm.vec3(1, 0, 0)
        self.forward = glm.vec3(0, 0, -1)
        self.limit = glm.vec2(20, -20)
        self.dis = 0

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
        self.collisions_two = Collisions_two(self)

        # Load sound
        self.sound = pg.mixer.Sound('voices/Afrodita.mp3')
        self.sound_playing = False
        self.bool = [False, False, False, False, False, False, False, False]
        self.pauseOn = 2
        self.playList = ['Hera.mp3', 'Hercules.mp3', 'Afrodita.mp3', 'Apolo.wav', 'Escultura.wav',
                         'Démeter.wav', 'Atenea.wav', 'Zeus.mp3']

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
        for i in range(0, len(self.app.positions_monument)):
            self.dis = sqrt((self.app.positions_monument[i][0] - self.position[0]) ** 2 + (
                        self.app.positions_monument[i][1] - self.position[2]) ** 2)
            #print(self.dis)
            if self.dis < 1:
                self.bool[i] = True
            if self.dis < 1 and self.bool[i]:
                if keys[pg.K_p]:
                    if not pg.mixer.Channel(0).get_busy() and self.pauseOn == 2:
                        self.play_sound(i)
                        print('PlayVoice', i)
                        self.pauseOn = 1
                    else:
                        self.pause_sound()


            elif self.dis > 1 and self.bool[i]:
                self.stop_sound()
                self.bool[i] = False

        if keys[pg.K_w]:
            self.x = self.position[0] + self.forward[0] * velocity
            self.z = self.position[2] + self.forward[2] * velocity
            bool_collisions = self.collisions.check_limits()
            bool_collisions_two = self.collisions_two.check_limits()
            if self.limit[0] > self.z > self.limit[1] and self.limit[0] > self.x > self.limit[1] and bool_collisions and bool_collisions_two and self.verify():
                self.position[0] = self.x
                self.position[2] = self.z
        if keys[pg.K_s]:
            self.x = self.position[0] - self.forward[0] * velocity
            self.z = self.position[2] - self.forward[2] * velocity
            bool_collisions = self.collisions.check_limits()
            bool_collisions_two = self.collisions_two.check_limits()
            if self.limit[0] > self.z > self.limit[1] and self.limit[0] > self.x > self.limit[1] and bool_collisions and bool_collisions_two and self.verify():
                self.position[0] = self.x
                self.position[2] = self.z
        if keys[pg.K_a]:
            self.x = self.position[0] - self.right[0] * velocity
            self.z = self.position[2] - self.right[2] * velocity
            bool_collisions = self.collisions.check_limits()
            bool_collisions_two = self.collisions_two.check_limits()
            if self.limit[0] > self.z > self.limit[1] and self.limit[0] > self.x > self.limit[1] and bool_collisions and bool_collisions_two and self.verify():
                self.position[0] = self.x
                self.position[2] = self.z
        if keys[pg.K_d]:
            self.x = self.position[0] + self.right[0] * velocity
            self.z = self.position[2] + self.right[2] * velocity
            bool_collisions = self.collisions.check_limits()
            bool_collisions_two = self.collisions_two.check_limits()
            if self.limit[0] > self.z > self.limit[1] and self.limit[0] > self.x > self.limit[1] and bool_collisions and bool_collisions_two and self.verify():
                self.position[0] = self.x
                self.position[2] = self.z
        if keys[pg.K_w] or keys[pg.K_s] or keys[pg.K_a] or keys[pg.K_d]:
            print(self.position)


    def get_view_matrix(self):
        return glm.lookAt(self.position, self.position + self.forward, self.up)

    def get_projection_matrix(self):
        return glm.perspective(glm.radians(FOV), self.aspect_ratio, NEAR, FAR)

    def play_sound(self, indexSong):
        if not self.sound_playing:
            self.sound = pg.mixer.Sound(f'voices/{self.playList[indexSong]}')
            self.sound.play()
            self.sound_playing = True

    def stop_sound(self):
        if self.sound_playing:
            self.sound.stop()
            self.pauseOn = 2
            self.sound_playing = False

    def pause_sound(self):
        if self.pauseOn == 1:
            pg.mixer.Channel(0).pause()
            self.pauseOn = False
            time.sleep(1)
            self.pauseOn = 0
        else:
            pg.mixer.Channel(0).unpause()
            self.pauseOn = True
            time.sleep(1)

    def verify(self):
        vertices = ([
            [-1.07, 2.5],
            [-2.77, 2.51],
            [-2.53, 7.31],
            [2.80, 7.26],
            [2.67, 2.51],
            [0.97, 2.59],
            [0.93, -1.89],
            [0.0, -1.87],
            [0.39, -2.14],
            [2.89, -2.12],
            [2.82, -7.84],
            [-2.91, -7.86],
            [-2.93, -2.07],
            [-0.405, -2.08],
            [-0.38, -1.78],
            [-1.072, -1.78]
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
            return True
        else:
            return False