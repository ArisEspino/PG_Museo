import pygame
import sys
import OpenGL.GL as gl
import OpenGL.GLUT as glut
import OpenGL.GLU as glu

def display_menu(textures, selected_index):
    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
    gl.glLoadIdentity()

    y_offset = 5
    x_offset = 5
    for i, texture in enumerate(textures):
        gl.glPushMatrix()
        gl.glTranslatef(x_offset, y_offset, 0)
        draw_texture(texture, 20, 20)  # Ajustar tamaño de textura
        if i == selected_index:
            draw_border(20, 20)
        gl.glPopMatrix()
        y_offset += 84  # 64 (icon height) + 20 (spacing)

    pygame.display.flip()

def display_audio_list(audio_files_display, selected_index, back_texture):
    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
    gl.glLoadIdentity()

    # Draw back button
    gl.glPushMatrix()
    gl.glTranslatef(5, 5, 0)
    draw_texture(back_texture, 20, 20)  # Ajustar tamaño de textura
    gl.glPopMatrix()

    font = pygame.font.Font(None, 20)  # Smaller font size for better visibility
    y_offset = 40  # Initial y position for the text

    for i, option in enumerate(audio_files_display):
        label = font.render(option, True, (255, 255, 255), (0, 0, 0, 0))  # Fondo transparente
        label_texture = create_texture(label)
        label_width, label_height = label.get_size()
        gl.glPushMatrix()
        gl.glTranslatef(80, 120 - y_offset - label_height, 0) # Keep the original y position
        draw_texture(label_texture, label_width, label_height)
        gl.glPopMatrix()
        y_offset += label_height + 10  # Adjust spacing

    pygame.display.flip()

def draw_texture(texture, width, height):
    gl.glEnable(gl.GL_TEXTURE_2D)
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture)
    gl.glBegin(gl.GL_QUADS)
    gl.glTexCoord2f(0.0, 0.0)
    gl.glVertex2f(0.0, 0.0)
    gl.glTexCoord2f(1.0, 0.0)
    gl.glVertex2f(width, 0.0)
    gl.glTexCoord2f(1.0, 1.0)
    gl.glVertex2f(width, height)
    gl.glTexCoord2f(0.0, 1.0)
    gl.glVertex2f(0.0, height)
    gl.glEnd()
    gl.glDisable(gl.GL_TEXTURE_2D)

def draw_border(width, height):
    gl.glColor3f(0.0, 0.0, 0.0)  # Red color for border
    gl.glBegin(gl.GL_LINE_LOOP)
    gl.glVertex2f(0.0, 0.0)
    gl.glVertex2f(width, 0.0)
    gl.glVertex2f(width, height)
    gl.glVertex2f(0.0, height)
    gl.glEnd()
    gl.glColor3f(1.0, 1.0, 1.0)  # Reset color to white

def create_texture(surface):
    texture_data = pygame.image.tostring(surface, "RGBA", True)
    width, height = surface.get_size()
    texture = gl.glGenTextures(1)
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)
    gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGBA, width, height, 0, gl.GL_RGBA, gl.GL_UNSIGNED_BYTE, texture_data)
    return texture

def play_audio(file_path):
    pygame.mixer.music.stop()
    if not pygame.mixer.get_init():
        pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play(-1)

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600), pygame.OPENGL | pygame.DOUBLEBUF)
    pygame.display.set_caption('Menú Principal')

    gl.glClearColor(0.0, 0.0, 0.0, 0.0)
    gl.glMatrixMode(gl.GL_PROJECTION)
    gl.glLoadIdentity()
    glu.gluOrtho2D(0, 400, 300, 0)  # Adjusted the projection to match Pygame's coordinate system
    gl.glMatrixMode(gl.GL_MODELVIEW)
    gl.glLoadIdentity()

    icon_surface = pygame.image.load("sound.png")
    back_icon_surface = pygame.image.load("flecha1.png")
    icons = [create_texture(icon_surface)]
    back_texture = create_texture(back_icon_surface)

    selected_index = 0
    in_main_menu = True

    audio_files = [
        "Beethoven  - Silencio (320).mp3",
        "Beethoven - Für Elise (320).mp3",
        "Vivaldi_SoundBackground.mp3"
    ]

    audio_files_display = [
        "Silencio",
        "Fur Elise",
        "Vivaldi"
    ]

    play_audio(audio_files[selected_index])

    while True:
        if in_main_menu:
            display_menu(icons, selected_index)
        else:
            display_audio_list(audio_files_display, selected_index, back_texture)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = event.pos
                    if in_main_menu:
                        y_offset = 10
                        for i, icon in enumerate(icons):
                            rect = pygame.Rect(10, y_offset, 64, 64)
                            if rect.collidepoint(mouse_pos):
                                in_main_menu = False
                                selected_index = 0
                                break
                            y_offset += 84
                    else:
                        back_rect = pygame.Rect(10, 10, 64, 64)
                        if back_rect.collidepoint(mouse_pos):
                            in_main_menu = True
                            selected_index = 0
                        else:
                            y_offset = 50
                            for i in range(len(audio_files_display)):
                                rect = pygame.Rect(50, y_offset, 300, 40)
                                if rect.collidepoint(mouse_pos):
                                    pygame.mixer.music.fadeout(500)
                                    play_audio(audio_files[i])
                                    selected_index = i
                                    break
                                y_offset += 40

        pygame.time.Clock().tick(10)

if __name__ == "__main__":
    main()
