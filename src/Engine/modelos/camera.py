import glm
import pygame as pg
from math import sqrt

FOV = 50  # deg
NEAR = 0.1
FAR = 100
SPEED = 0.005
SENSITIVITY = 0.08

class Camera:
    def __init__(self, app, position=(0, 0, 4), yaw=-90, pitch=0):
        self.app = app
        self.aspect_ratio = app.WIN_SIZE[0] / app.WIN_SIZE[1]
        self.position = glm.vec3(position)
        self.up = glm.vec3(0, 1, 0)
        self.right = glm.vec3(1, 0, 0)
        self.forward = glm.vec3(0, 0, -1)
        self.limit = glm.vec2(40, -40)
        self.positions_monument = glm.vec2(3, 2)
        self.dis = 0

        self.yaw = yaw
        self.pitch = pitch
        # view matrix
        self.m_view = self.get_view_matrix()
        # projection matrix
        self.m_proj = self.get_projection_matrix()

        # Load sound
        self.sound = pg.mixer.Sound('sounds/Zeus.mp3')
        self.sound_playing = False

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
        self.dis = sqrt((self.positions_monument[0] - self.position[0]) ** 2 + (self.positions_monument[1] - self.position[2]) ** 2)
        print(self.dis)

        if self.dis < 5:
            if keys[pg.K_p]:
                self.play_sound()
        else:
            self.stop_sound()

        if keys[pg.K_w]:
            x_aux = self.position[0] + self.forward[0] * velocity
            z_aux = self.position[2] + self.forward[2] * velocity
            if self.limit[0] > z_aux > self.limit[1] and self.limit[0] > x_aux > self.limit[1]:
                self.position[0] = x_aux
                self.position[2] = z_aux
        if keys[pg.K_s]:
            x_aux = self.position[0] - self.forward[0] * velocity
            z_aux = self.position[2] - self.forward[2] * velocity
            if self.limit[0] > z_aux > self.limit[1] and self.limit[0] > x_aux > self.limit[1]:
                self.position[0] = x_aux
                self.position[2] = z_aux
        if keys[pg.K_a]:
            x_aux = self.position[0] - self.right[0] * velocity
            z_aux = self.position[2] - self.right[2] * velocity
            if self.limit[0] > z_aux > self.limit[1] and self.limit[0] > x_aux > self.limit[1]:
                self.position[0] = x_aux
                self.position[2] = z_aux
        if keys[pg.K_d]:
            x_aux = self.position[0] + self.right[0] * velocity
            z_aux = self.position[2] + self.right[2] * velocity
            if self.limit[0] > z_aux > self.limit[1] and self.limit[0] > x_aux > self.limit[1]:
                self.position[0] = x_aux
                self.position[2] = z_aux

    def get_view_matrix(self):
        return glm.lookAt(self.position, self.position + self.forward, self.up)

    def get_projection_matrix(self):
        return glm.perspective(glm.radians(FOV), self.aspect_ratio, NEAR, FAR)

    def play_sound(self):
        if not self.sound_playing:
            self.sound.play()
            self.sound_playing = True

    def stop_sound(self):
        if self.sound_playing:
            self.sound.stop()
            self.sound_playing = False
