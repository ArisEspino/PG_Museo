import pygame
import sys

def display_menu(screen, icons, selected_index):
    screen.fill((0, 0, 0))

    y_offset = 50
    x_offset = 50
    for i, icon in enumerate(icons):
        rect = icon.get_rect(topleft=(x_offset, y_offset))
        if i == selected_index:
            pygame.draw.rect(screen, (255, 0, 0), rect, 2)  # Resaltar opción seleccionada

        screen.blit(icon, (x_offset, y_offset))
        y_offset += icon.get_height() + 20

    pygame.display.flip()

def display_audio_list(screen, audio_files, selected_index):
    screen.fill((0, 0, 0))  # Limpiar pantalla

    font = pygame.font.Font(None, 15)  # Fuente
    y_offset = 50

    for i, option in enumerate(audio_files):
        if i == selected_index:
            label = font.render(f"{option}", True, (255, 255, 255))
        else:
            label = font.render(option, True, (255, 255, 255))
        screen.blit(label, (50, y_offset))
        y_offset += 50

    pygame.display.flip()

def play_audio(file_path):
    # Inicializar pygame mixer
    pygame.mixer.init()

    # Cargar el archivo de audio
    pygame.mixer.music.load(file_path)
    # Reproducir el archivo de audio
    pygame.mixer.music.play()

    # Esperar a que termine de reproducirse
    while pygame.mixer.music.get_busy():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                pygame.quit()
                sys.exit()

        pygame.time.Clock().tick(10)  # Actualizar cada 100ms

def main():
    # Inicializar pygame y crear la pantalla
    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption('Menú Principal')

    # Cargar imagen de icono para el menú
    icons = [pygame.image.load("sonido.png")]

    selected_index = 0
    in_main_menu = True

    audio_files = [
        "Vivaldi_SoundBackground.mp3",
        "condor_pasa.wav",
        "bridgerton.mp3"
    ]


    while True:
        if in_main_menu:

            display_menu(screen, icons, selected_index)
        else:
            display_audio_list(screen, audio_files, selected_index)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if in_main_menu: True

            elif event.type == pygame.MOUSEBUTTONDOWN:
                 if event.button == 1:  # Clic izquierdo
                    mouse_pos = event.pos
                    if in_main_menu:
                        y_offset = 50
                        for i, icon in enumerate(icons):
                            rect = icon.get_rect(topleft=(50, y_offset))
                            if rect.collidepoint(mouse_pos):
                                in_main_menu = False
                                selected_index = 0  # Reset selection for audio list
                                break
                            y_offset += icon.get_height() + 20
                    else:
                        y_offset = 50
                        for i, _ in enumerate(audio_files):
                            rect = pygame.Rect(50, y_offset, 300, 40)
                            if rect.collidepoint(mouse_pos):
                                play_audio(audio_files[i])  # Reproducir archivo seleccionado
                                in_main_menu = True  # Volver al menú principal después de reproducir
                                selected_index = 0  # Reset selection for main menu
                                break
                            y_offset += 50

        pygame.time.Clock().tick(10)  # Actualizar cada 100ms

if __name__ == "__main__":
    main()
