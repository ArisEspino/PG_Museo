import pygame
import sys

def main():
    #  Pygame
    pygame.init()

    #  pantalla
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Greek Museum')

    #  colores
    PINK = (255, 192, 203)
    WHITE = (255, 255, 255)

    #  fuente y tamaño del texto
    font = pygame.font.Font(None, 74)

    # objeto de texto
    text = font.render('¡Bienvenido a Greek Museum!', True, WHITE)

    #  rectángulo del objeto de texto
    text_rect = text.get_rect()
    text_rect.center = (400, 300)

    # Bucle
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #  color rosa
        screen.fill(PINK)

        # texto en la pantalla
        screen.blit(text, text_rect)

        # Actualiza
        pygame.display.flip()

    # Salir
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
