import pygame as pg
import sys

class GraphicsEngine:
    def __init__(self, win_size=(600, 400)):
        pg.init()
        self.WIN_SIZE = win_size
        pg.display.set_mode(self.WIN_SIZE, pg.OPENGL | pg.DOUBLEBUF)

        # Configuraciones de mixer para la música
        pg.mixer.init()

        # Lista de nombres de archivo de música
        self.music_files = [
            "Hijo De La Luna.mp3",
            "Sparkle - Your Name.mp3",
            "Mariage d'Amour.mp3"
        ]

        # Variables para control de reproducción de música
        self.current_music_index = 0
        self.music_playing = False

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.stop_music()
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    self.change_music(0)  # Primera pista
                elif event.key == pg.K_DOWN:
                    self.change_music(1)  # Segunda pista
                elif event.key == pg.K_RIGHT:
                    self.change_music(2)  # Tercera pista

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

    def run(self):
        self.play_music_sequence()  # Iniciar la reproducción de música al inicio
        while True:
            self.check_events()
            self.update_music()  # Actualizar la reproducción de música
            pg.time.Clock().tick(10)

if __name__ == '__main__':
    app = GraphicsEngine()
    app.run()
