import pygame
import sys

def main():
    #  Pygame
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption('Greek Museum')

    # imagen de fondo
    background_image = pygame.image.load('objects/god3.jpg')

    #  colores
    WHITE = (255, 255, 255)

    # fuente y tamaño del texto
    font = pygame.font.Font(None, 50)
    font1 = pygame.font.Font(None, 25)

    # Crear objetos  texto
    text = font.render('¡Bienvenido a Greek Museum!', True, WHITE)
    text1 = font1.render('Presiona enter para continuar>>', True, WHITE)

    # rectángulos de  textos
    text_rect = text.get_rect()
    text_rect.center = (300, 300)
    text1_rect = text1.get_rect()
    text1_rect.center = (300, 550)

    # Bucle
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(background_image, (0, 0))

        #  textos en la pantalla
        screen.blit(text, text_rect)
        screen.blit(text1, text1_rect)

        pygame.display.flip()
    # Salir
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
