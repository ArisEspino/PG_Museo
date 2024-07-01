import pygame as pg
import moderngl as mgl
import glm



class Texture:
    def __init__(self, app):
        self.app = app
        self.ctx = app.ctx
        self.textures = {}
        self.textures[0] = self.get_texture(path='textures/ss.jpg')
        #la textura del museo
        self.textures['cat'] = self.get_texture(path='objects/gallery/otra.png')
        self.textures['head'] = self.get_texture(path='objects/head/head.jpeg')
        self.textures['mesa'] = self.get_texture(path='objects/mesa/mesa.png')
        self.textures['herku'] = self.get_texture(path='objects/herkules/herkules.jpeg')
        self.textures['woman'] = self.get_texture(path='objects/woman/woman.jpeg')
        self.textures['man'] = self.get_texture(path='objects/man/man.jpeg')
        self.textures['jarra'] = self.get_texture(path='objects/jarra/jarra.jpeg')
        self.textures['plato'] = self.get_texture(path='objects/plato/plato.jpeg')
        self.textures['orar'] = self.get_texture(path='objects/orar/orando.jpeg')
        self.textures['mujer'] = self.get_texture(path='objects/mujer/mujer.png')
        self.textures['ate'] = self.get_texture(path='objects/atenea/atenea.jpeg')
        self.textures['zeus'] = self.get_texture(path='objects/zeus/zeus.png')
        #texturas garden part
        self.textures['wall'] = self.get_texture(path='objects/garden/wall.png')
        self.textures['leaf'] = self.get_texture(path='objects/garden/Flower/leaf.jpeg')
        self.textures['stigma'] = self.get_texture(path='objects/garden/Flower/stigma.jpeg')
        self.textures['petals'] = self.get_texture(path='objects/garden/Flower/petals.jpeg')
        self.textures['steam'] = self.get_texture(path='objects/garden/Flower/steam.jpeg')
        self.textures['grass'] = self.get_texture(path='objects/garden/Flower/grass.jpeg')
        self.textures['statue'] = self.get_texture(path='objects/garden/statue.png')
        self.textures['roses'] = self.get_texture(path='objects/garden/flowers.png')
        self.textures['ground'] = self.get_texture(path='objects/garden/ground.jpeg')
        self.textures['trunk'] = self.get_texture(path='objects/garden/trunk.jpg')
        self.textures['leavesTree'] = self.get_texture(path='objects/garden/leaveTree.jpg')
        #garden pt2
        self.textures['pool'] = self.get_texture(path='objects/pis/pool.jpeg')
        self.textures['col'] = self.get_texture(path='objects/col/col.png')
        self.textures['mari'] = self.get_texture(path='objects/mari/mari.jpeg')
        self.textures['skybox'] = self.get_texture_cube(dir_path='textures/skybox1/', ext='png')
        self.textures['depth_texture'] = self.get_depth_texture()

    def get_depth_texture(self):
        depth_texture = self.ctx.depth_texture(self.app.WIN_SIZE)
        depth_texture.repeat_x = False
        depth_texture.repeat_y = False
        return depth_texture

    def get_texture_cube(self, dir_path, ext='png'):
        faces = ['right', 'left', 'top', 'bottom'] + ['front', 'back'][::-1]
        textures = []
        for face in faces:
            texture = pg.image.load(dir_path + f'{face}.{ext}').convert()
            if face in ['right', 'left', 'front', 'back']:
                texture = pg.transform.flip(texture, flip_x=True, flip_y=False)
            else:
                texture = pg.transform.flip(texture, flip_x=False, flip_y=True)
            textures.append(texture)

        size = textures[0].get_size()
        texture_cube = self.ctx.texture_cube(size=size, components=3, data=None)

        for i in range(6):
            texture_data = pg.image.tostring(textures[i], 'RGB')
            texture_cube.write(face=i, data=texture_data)

        return texture_cube

    def get_texture(self, path):
        texture = pg.image.load(path).convert()
        texture = pg.transform.flip(texture, flip_x=False, flip_y=True)
        texture = self.ctx.texture(size=texture.get_size(), components=3,
                                   data=pg.image.tostring(texture, 'RGB'))

        texture.filter = (mgl.LINEAR_MIPMAP_LINEAR, mgl.LINEAR)
        texture.build_mipmaps()
        texture.anisotropy = 32.0
        return texture

    def destroy(self):
        [tex.release() for tex in self.textures.values()]
