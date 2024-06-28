import pygame
import sys
import OpenGL.GL as gl
import OpenGL.GLU as glu

def display_menu(textures, selected_index):
    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
    gl.glLoadIdentity()

    y_offset = 5
    x_offset = 5
    for i, texture in enumerate(textures):
        gl.glPushMatrix()
        gl.glTranslatef(x_offset, y_offset, 0)
        draw_texture(texture, 30, 30)
        if i == selected_index:
            draw_border(30, 30)
        gl.glPopMatrix()
        y_offset += 84

    pygame.display.flip()

def display_audio_list(audio_files_display, selected_index, back_texture):
    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
    gl.glLoadIdentity()

    # Draw back button
    gl.glPushMatrix()
    gl.glTranslatef(5, 5, 0)
    draw_texture(back_texture, 30, 30)
    gl.glPopMatrix()

    font = pygame.font.Font(None, 36)
    y_offset = 60

    for i, option in enumerate(audio_files_display):
        label = font.render(option, True, (255, 255, 255), (0, 0, 0))
        label = pygame.transform.flip(label, False, True)  # Flip the surface vertically
        label_texture = create_texture(label)
        label_width, label_height = label.get_size()
        gl.glPushMatrix()
        gl.glTranslatef(80, y_offset, 0)
        draw_texture(label_texture, label_width, label_height)
        if i == selected_index:
            draw_border(label_width, label_height)
        gl.glPopMatrix()
        y_offset += label_height + 10

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
    gl.glColor3f(0.0, 0.0, 0.0)  # Black color for border
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
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600), pygame.OPENGL | pygame.DOUBLEBUF)
    pygame.display.set_caption('Menú Principal')

    gl.glClearColor(0.0, 0.0, 0.0, 0.0)
    gl.glMatrixMode(gl.GL_PROJECTION)
    gl.glLoadIdentity()
    glu.gluOrtho2D(0, 800, 600, 0)
    gl.glMatrixMode(gl.GL_MODELVIEW)
    gl.glLoadIdentity()

    icon_surface = pygame.image.load("sound.png")
    back_icon_surface = pygame.image.load("flecha1.png")
    icons = [create_texture(icon_surface)]
    back_texture = create_texture(back_icon_surface)

    selected_index = 0
    in_main_menu = True

    audio_files = [
        "Hijo De La Luna.mp3",
        "Sparkle - Your Name.mp3",
        "Mariage d'Amour.mp3"
    ]

    audio_files_display = [
        "Hijo De La Luna",
        "Your Name",
        "Mariage d'Amour"
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
                        y_offset = 5
                        for i, icon in enumerate(icons):
                            rect = pygame.Rect(5, y_offset, 30, 30)
                            if rect.collidepoint(mouse_pos):
                                in_main_menu = False
                                selected_index = 0
                                break
                            y_offset += 84
                    else:
                        back_rect = pygame.Rect(5, 5, 30, 30)
                        if back_rect.collidepoint(mouse_pos):
                            in_main_menu = True
                            selected_index = 0
                        else:
                            y_offset = 60
                            for i in range(len(audio_files_display)):
                                label = pygame.font.Font(None, 36).render(audio_files_display[i], True, (255, 255, 255), (0, 0, 0))
                                label_width, label_height = label.get_size()
                                rect = pygame.Rect(80, y_offset, label_width, label_height)
                                if rect.collidepoint(mouse_pos):
                                    play_audio(audio_files[i])
                                    selected_index = i
                                    break
                                y_offset += label_height + 10

        if pygame.mixer.music.get_busy() == 0:  # Si la música ha terminado de reproducirse
            selected_index = (selected_index + 1) % len(audio_files_display)  # Avanza al siguiente índice circularmente
            play_audio(audio_files[selected_index])

        pygame.time.Clock().tick(10)

if __name__ == "__main__":
    main()
