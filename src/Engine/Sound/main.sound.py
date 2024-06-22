import pygame
import sys

def display_menu(screen, icons, selected_index):
    screen.fill((0, 0, 0))

    y_offset = 10
    x_offset = 10
    for i, icon in enumerate(icons):
        rect = icon.get_rect(topleft=(x_offset, y_offset))
        if i == selected_index:
            pygame.draw.rect(screen, (255, 0, 0), rect, 2)  # Resaltar opción seleccionada

        screen.blit(icon, (x_offset, y_offset))
        y_offset += icon.get_height() + 20

    pygame.display.flip()

def display_audio_list(screen, audio_files_display, selected_index, back_icon):
    screen.fill((0, 0, 0))  # Limpiar pantalla

    # Dibujar el icono de regresar
    screen.blit(back_icon, (10, 10))

    font = pygame.font.Font(None, 20)  # Fuente más pequeña
    y_offset = 40

    for i, option in enumerate(audio_files_display):
        if i == selected_index:
            label = font.render(f"{option}", True, (255, 255, 255))
        else:
            label = font.render(option, True, (255, 255, 255))
        screen.blit(label, (50, y_offset))
        y_offset += 40

    pygame.display.flip()

def play_audio(file_path):
    # Inicializar pygame mixer
    pygame.mixer.init()

    # Cargar el archivo de audio
    pygame.mixer.music.load(file_path)
    # Reproducir el archivo de audio
    pygame.mixer.music.play()

def main():
    # Inicializar pygame y crear la pantalla
    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption('Menú Principal')

    # Cargar imagen de icono para el menú
    icons = [pygame.image.load("sound.png")]
    back_icon = pygame.image.load("flecha1.png")  # Cargar imagen de la flecha

    selected_index = 0
    in_main_menu = True

    audio_files = [
        "Beethoven  - Silencio (320).mp3",
        "Beethoven - Für Elise (320).mp3",
        "Vivaldi_SoundBackground.mp3"
    ]

    # Lista de nombres para mostrar sin extensión de archivo
    audio_files_display = [
        "Silencio",
        "Fur Elise",
        "Vivaldi"
    ]
    play_audio(audio_files[selected_index])


    while True:
        if in_main_menu:
            display_menu(screen, icons, selected_index)
        else:
            display_audio_list(screen, audio_files_display, selected_index, back_icon)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if in_main_menu:
                    if event.key == pygame.K_DOWN:
                        selected_index = (selected_index + 1) % len(icons)
                    elif event.key == pygame.K_UP:
                        selected_index = (selected_index - 1) % len(icons)
                    elif event.key == pygame.K_RETURN:
                        in_main_menu = False
                        selected_index = 0  # Reset selection for audio list
                else:
                    if event.key == pygame.K_DOWN:
                        selected_index = (selected_index + 1) % len(audio_files_display)
                    elif event.key == pygame.K_UP:
                        selected_index = (selected_index - 1) % len(audio_files_display)
                    elif event.key == pygame.K_RETURN:
                        play_audio(audio_files[selected_index])

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Clic izquierdo
                    mouse_pos = event.pos
                    if in_main_menu:
                        y_offset = 10
                        for i, icon in enumerate(icons):
                            rect = icon.get_rect(topleft=(10, y_offset))
                            if rect.collidepoint(mouse_pos):
                                in_main_menu = False
                                selected_index = 0  # Reset selection for audio list
                                break
                            y_offset += icon.get_height() + 20
                    else:
                        back_rect = back_icon.get_rect(topleft=(10, 10))
                        if back_rect.collidepoint(mouse_pos):
                            in_main_menu = True
                            selected_index = 0  # Reset selection for main menu
                        else:
                            y_offset = 40
                            for i, _ in enumerate(audio_files_display):
                                rect = pygame.Rect(10, y_offset, 300, 40)
                                if rect.collidepoint(mouse_pos):
                                    play_audio(audio_files[i])  # Reproducir archivo seleccionado
                                    break
                                y_offset += 40

        # Verificar si la música ha terminado de reproducirse
        if not pygame.mixer.music.get_busy() and not in_main_menu:
            selected_index = (selected_index + 0) % len(audio_files)
            play_audio(audio_files[selected_index])

        pygame.time.Clock().tick(10)  # Actualizar cada 100ms

if __name__ == "__main__":
    main()
