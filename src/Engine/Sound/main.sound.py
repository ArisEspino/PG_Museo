import pygame as pg
import sys
from OpenGL.GL import *
from OpenGL.GLU import *

class GraphicsEngine:
    def __init__(self, win_size=(600, 400)):
        pg.init()
        self.screen = pg.display.set_mode(win_size, pg.OPENGL | pg.DOUBLEBUF)
        pg.display.set_caption('Menú Principal')

        self.init_opengl()
        self.icon_surface = pg.image.load("sound.png")
        self.back_icon_surface = pg.image.load("flecha1.png")
        self.icons = [self.create_texture(self.icon_surface)]
        self.back_texture = self.create_texture(self.back_icon_surface)

        self.selected_index = 0
        self.in_main_menu = True

        self.audio_files = [
            "Hijo De La Luna.mp3",
            "Sparkle - Your Name.mp3",
            "Mariage d'Amour.mp3"
        ]

        self.audio_files_display = [
            "Hijo De La Luna",
            "Your Name",
            "Mariage d'Amour"
        ]

        self.play_audio(self.audio_files[self.selected_index])

    def init_opengl(self):
        glClearColor(0.0, 0.0, 0.0, 0.0)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluOrtho2D(0, 800, 600, 0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def display_menu(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        y_offset = 5
        x_offset = 5
        for i, texture in enumerate(self.icons):
            glPushMatrix()
            glTranslatef(x_offset, y_offset, 0)
            self.draw_texture(texture, 30, 30)
            if i == self.selected_index:
                self.draw_border(30, 30)
            glPopMatrix()
            y_offset += 84

        pg.display.flip()

    def display_audio_list(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        glPushMatrix()
        glTranslatef(5, 5, 0)
        self.draw_texture(self.back_texture, 30, 30)
        glPopMatrix()

        font = pg.font.Font(None, 36)
        y_offset = 60

        for i, option in enumerate(self.audio_files_display):
            label = font.render(option, True, (255, 255, 255), (0, 0, 0))
            label = pg.transform.flip(label, False, True)
            label_texture = self.create_texture(label)
            label_width, label_height = label.get_size()
            glPushMatrix()
            glTranslatef(80, y_offset, 0)
            self.draw_texture(label_texture, label_width, label_height)
            if i == self.selected_index:
                self.draw_border(label_width, label_height)
            glPopMatrix()
            y_offset += label_height + 10

        pg.display.flip()

    def draw_texture(self, texture, width, height):
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, texture)
        glBegin(GL_QUADS)
        glTexCoord2f(0.0, 0.0)
        glVertex2f(0.0, 0.0)
        glTexCoord2f(1.0, 0.0)
        glVertex2f(width, 0.0)
        glTexCoord2f(1.0, 1.0)
        glVertex2f(width, height)
        glTexCoord2f(0.0, 1.0)
        glVertex2f(0.0, height)
        glEnd()
        glDisable(GL_TEXTURE_2D)

    def draw_border(self, width, height):
        glColor3f(0.0, 0.0, 0.0)
        glBegin(GL_LINE_LOOP)
        glVertex2f(0.0, 0.0)
        glVertex2f(width, 0.0)
        glVertex2f(width, height)
        glVertex2f(0.0, height)
        glEnd()
        glColor3f(1.0, 1.0, 1.0)

    def create_texture(self, surface):
        texture_data = pg.image.tostring(surface, "RGBA", True)
        width, height = surface.get_size()
        texture = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, texture)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, texture_data)
        return texture

    def play_audio(self, file_path):
        pg.mixer.music.load(file_path)
        pg.mixer.music.play()

    def run(self):
        while True:
            if self.in_main_menu:
                self.display_menu()
            else:
                self.display_audio_list()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

                elif event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mouse_pos = event.pos
                        if self.in_main_menu:
                            y_offset = 5
                            for i in range(len(self.icons)):
                                rect = pg.Rect(5, y_offset, 30, 30)
                                if rect.collidepoint(mouse_pos):
                                    self.in_main_menu = False
                                    self.selected_index = 0
                                    break
                                y_offset += 84
                        else:
                            back_rect = pg.Rect(5, 5, 30, 30)
                            if back_rect.collidepoint(mouse_pos):
                                self.in_main_menu = True
                                self.selected_index = 0
                            else:
                                y_offset = 60
                                for i in range(len(self.audio_files_display)):
                                    label = pg.font.Font(None, 36).render(self.audio_files_display[i], True, (255, 255, 255), (0, 0, 0))
                                    label_width, label_height = label.get_size()
                                    rect = pg.Rect(80, y_offset, label_width, label_height)
                                    if rect.collidepoint(mouse_pos):
                                        self.play_audio(self.audio_files[i])
                                        self.selected_index = i
                                        break
                                    y_offset += label_height + 10

            if pg.mixer.music.get_busy() == 0:
                self.selected_index = (self.selected_index + 1) % len(self.audio_files_display)
                self.play_audio(self.audio_files[self.selected_index])

            pg.time.Clock().tick(10)

if __name__ == "__main__":
    app = GraphicsEngine()
    app.run()
