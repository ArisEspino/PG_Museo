import pygame as pg
import moderngl as mgl
import sys
from model import *
from camera import Camera
from light import Light
from mesh import Mesh
from scene import Scene
from scene_renderer import SceneRenderer


class GraphicsEngine:
    def __init__(self, win_size=(600, 600)):
        # modulos de pygame
        pg.init()
        # tamaño de la ventana
        self.WIN_SIZE = win_size
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
        pg.display.set_mode(self.WIN_SIZE, flags=pg.OPENGL | pg.DOUBLEBUF)
        # configuraciones de mouse
        pg.event.set_grab(True)
        pg.mouse.set_visible(False)
        # contenido de opengl
        self.ctx = mgl.create_context()
        # self.ctx.front_face = 'cw'
        self.ctx.enable(flags=mgl.DEPTH_TEST | mgl.CULL_FACE)
        # creacion de un objeto
        self.clock = pg.time.Clock()
        self.time = 0
        self.delta_time = 0
        # luz
        self.light = Light()
        # Array models
        self.positions_monument = []
        # camara
        self.camera = Camera(self)
        # mesh part
        self.mesh = Mesh(self)
        # scene part
        self.scene = Scene(self)
        # renderer part
        self.scene_renderer = SceneRenderer(self)
        # Configuración de mixer para la música
        pg.mixer.init()

        # Lista de nombres de archivo de música
        self.music_files = [
            "music/Hijo De La Luna.mp3",
            "music/Mariage d Amour.mp3",
            "music/Sparkle - Your Name.mp3"
        ]

        # Variables para control de reproducción de música
        self.current_music_index = 0
        self.music_playing = False
    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.mesh.destroy()
                self.scene_renderer.destroy()
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    self.change_music(0)  # First track
                elif event.key == pg.K_DOWN:
                    self.change_music(1)  # Second track
                elif event.key == pg.K_RIGHT:
                    self.change_music(2)  # Third track

    def render(self):
        # limpiar la pantalla y color de ella
        self.ctx.clear(color=(0.08, 0.16, 0.18))
        # render scene
        self.scene_renderer.render()
        pg.display.flip()
    def play_music_sequence(self):
        if not self.music_playing:
            self.music_playing = True
            pg.mixer.music.load(self.music_files[self.current_music_index])
            pg.mixer.music.play()

    def stop_music(self):
        pg.mixer.music.stop()
        self.music_playing = False

    def update_music(self):
        if self.music_playing and not pg.mixer.music.get_busy():
            self.current_music_index = (self.current_music_index + 1) % len(self.music_files)
            pg.mixer.music.load(self.music_files[self.current_music_index])
            pg.mixer.music.play()

    def change_music(self, index):
        if 0 <= index < len(self.music_files):
            self.current_music_index = index
            pg.mixer.music.load(self.music_files[self.current_music_index])
            pg.mixer.music.play()
    def get_time(self):
        self.time = pg.time.get_ticks() * 0.001

    def render(self):
        self.ctx.clear(color=(0.08, 0.16, 0.18))
        self.scene_renderer.render()

        pg.display.flip()
    def run(self):
        self.play_music_sequence()  # Iniciar la reproducción de música al inicio
        while True:
            self.get_time()
            self.check_events()
            self.camera.update()
            self.update_music()
            self.render()
            self.delta_time = self.clock.tick(60)

if __name__ == '__main__':
    app = GraphicsEngine()
    app.run()






