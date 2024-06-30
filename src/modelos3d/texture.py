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
        self.textures['cat'] = self.get_texture(path='objects/museo_op.jpeg')
        self.textures['fuente'] = self.get_texture(path='objects/fuente/Root_baseColor.png')
        self.textures['mesa'] = self.get_texture(path='objects/table/lambert1_baseColor.png')
        self.textures['cara'] = self.get_texture(path='objects/cara1/Material_0_baseColor.jpeg')
        self.textures['face'] = self.get_texture(path='objects/cara2/Material_0_baseColor.jpeg')
        self.textures['choza'] = self.get_texture(path='objects/banca/Steel_-_Satin_baseColor.jpeg')

        #aca los de adentro
        self.textures['her'] = self.get_texture(path='objects/cuadro/chica.jpeg')
        self.textures['mujer'] = self.get_texture(path='objects/mujer/default_baseColor.jpeg')
        self.textures['sol'] = self.get_texture(path='objects/head/sol.png')
        self.textures['cab'] = self.get_texture(path='objects/dios/dios.png')

        self.textures['leon'] = self.get_texture(path='objects/leon/ropa.jpeg')
        self.textures['m1'] = self.get_texture(path='objects/m1mu/man.jpeg')
        self.textures['m2'] = self.get_texture(path='objects/m2sol/afro.jpeg')
        self.textures['m3'] = self.get_texture(path='objects/m3di/dog.jpeg')
        self.textures['m4'] = self.get_texture(path='objects/m4c/pray.jpeg')
        self.textures['m5'] = self.get_texture(path='objects/m5c/afrodita.jpeg')

        self.textures['tree'] = self.get_texture(path='objects/arboles/cafe.jpeg')
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
