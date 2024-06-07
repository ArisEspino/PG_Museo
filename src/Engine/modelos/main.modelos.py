import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from PIL import Image

# Posición de la cámara
camera_pos = [0.0, 0.0, 5.0]
camera_speed = 0.1

def load_texture(texture_file):
    image = Image.open(texture_file)
    image = image.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
    img_data = image.convert("RGBA").tobytes()
    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image.width, image.height, 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    return texture_id

def load_obj(filename):
    vertices = []
    texcoords = []
    faces = []

    with open(filename) as f:
        for line in f:
            if line.startswith('v '):
                vertices.append(list(map(float, line.strip().split()[1:])))
            elif line.startswith('vt '):
                texcoords.append(list(map(float, line.strip().split()[1:])))
            elif line.startswith('f '):
                face = []
                tex_face = []
                for vert in line.strip().split()[1:]:
                    values = vert.split('/')
                    v = int(values[0]) - 1
                    t = int(values[1]) - 1 if len(values) > 1 and values[1] else 0
                    face.append(vertices[v])
                    tex_face.append(texcoords[t])
                faces.append((face, tex_face))
    return faces

def draw_model(faces, texture_id):
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glBegin(GL_TRIANGLES)
    for face, tex_face in faces:
        for i in range(len(face)):
            glTexCoord2fv(tex_face[i])
            glVertex3fv(face[i])
    glEnd()
    glDisable(GL_TEXTURE_2D)

def main():
    pygame.init()
    pygame.display.set_mode((800, 600), DOUBLEBUF | OPENGL)
    gluPerspective(45, (800/600), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)  # Iniciar la cámara un poco lejos
    glClearColor(0.2, 0.3, 0.3, 1.0)

    # Cargar el modelo 3D
    try:
        faces = load_obj('cubo2.obj')
        print("Model loaded successfully")
    except Exception as e:
        print(f"Error loading model: {e}")
        return

    # Cargar la textura
    global texture_id
    texture_id = load_texture('OIP.jpg')

    # Inicializar el módulo de sonido y cargar el sonido
    # pygame.mixer.init()
    # sound = pygame.mixer.Sound('ambiente.mp3')
    # sound.play()

    global camera_pos

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        keys = pygame.key.get_pressed()
        if keys[K_w]:
            glTranslatef(0, 0, camera_speed)
        if keys[K_s]:
            glTranslatef(0, 0, -camera_speed)
        if keys[K_a]:
            glTranslatef(camera_speed, 0, 0)
        if keys[K_d]:
            glTranslatef(-camera_speed, 0, 0)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_model(faces, texture_id)
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
