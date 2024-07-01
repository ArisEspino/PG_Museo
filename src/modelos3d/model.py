import moderngl as mgl
import numpy as np
import glm


class BaseModel:
    def __init__(self, app, vao_name, tex_id, pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        self.app = app
        self.pos = pos
        self.vao_name = vao_name
        self.rot = glm.vec3([glm.radians(a) for a in rot])
        self.scale = scale
        self.m_model = self.get_model_matrix()
        self.tex_id = tex_id
        self.vao = app.mesh.vao.vaos[vao_name]
        self.program = self.vao.program
        self.camera = self.app.camera

    def update(self): ...

    def get_model_matrix(self):
        m_model = glm.mat4()
        # translacion
        m_model = glm.translate(m_model, self.pos)
        # rotacion
        m_model = glm.rotate(m_model, self.rot.z, glm.vec3(0, 0, 1))
        m_model = glm.rotate(m_model, self.rot.y, glm.vec3(0, 1, 0))
        m_model = glm.rotate(m_model, self.rot.x, glm.vec3(1, 0, 0))
        # scalacion
        m_model = glm.scale(m_model, self.scale)
        return m_model

    def render(self):
        self.update()
        self.vao.render()

class ExtendedBaseModel(BaseModel):
    def __init__(self, app, vao_name, tex_id, pos, rot, scale):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()

    def update(self):
        self.texture.use(location=0)
        self.program['camPos'].write(self.camera.position)
        self.program['m_view'].write(self.camera.m_view)
        self.program['m_model'].write(self.m_model)

    def update_shadow(self):
        self.shadow_program['m_model'].write(self.m_model)

    def render_shadow(self):
        self.update_shadow()
        self.shadow_vao.render()

    def on_init(self):
        self.program['m_view_light'].write(self.app.light.m_view_light)
        # resolucion
        self.program['u_resolution'].write(glm.vec2(self.app.WIN_SIZE))
        # textura
        self.depth_texture = self.app.mesh.texture.textures['depth_texture']
        self.program['shadowMap'] = 1
        self.depth_texture.use(location=1)
        # sombras
        self.shadow_vao = self.app.mesh.vao.vaos['shadow_' + self.vao_name]
        self.shadow_program = self.shadow_vao.program
        self.shadow_program['m_proj'].write(self.camera.m_proj)
        self.shadow_program['m_view_light'].write(self.app.light.m_view_light)
        self.shadow_program['m_model'].write(self.m_model)
        # textura pt2
        self.texture = self.app.mesh.texture.textures[self.tex_id]
        self.program['u_texture_0'] = 0
        self.texture.use(location=0)
        # mvp
        self.program['m_proj'].write(self.camera.m_proj)
        self.program['m_view'].write(self.camera.m_view)
        self.program['m_model'].write(self.m_model)
        # luz
        self.program['light.position'].write(self.app.light.position)
        self.program['light.Ia'].write(self.app.light.Ia)
        self.program['light.Id'].write(self.app.light.Id)
        self.program['light.Is'].write(self.app.light.Is)

   #monteee
class Cube(ExtendedBaseModel):
    def __init__(self, app, vao_name='cube', tex_id=0, pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)

class MovingCube(Cube):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def update(self):
        self.m_model = self.get_model_matrix()
        super().update()

 #museo

class Cat(ExtendedBaseModel): #este es el museo
    def __init__(self, app, vao_name='cat', tex_id='cat',
                pos=(0, 0, 0), rot=(0, 0, 0), scale=(0.6, 0.6, 0.6)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
#head
class Head(ExtendedBaseModel):
    def __init__(self, app, vao_name='head', tex_id='head',
                pos=(0, 0, 0), rot=(0, 0, 0), scale=(0.02, 0.02, 0.02)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)

#mesa
class Mesa(ExtendedBaseModel):
    def __init__(self, app, vao_name='mesa', tex_id='mesa',
                pos=(0, 0, 0), rot=(0, 0, 0), scale=(0.3, 0.3, 0.3)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)

#herkules
class Herku(ExtendedBaseModel):
    def __init__(self, app, vao_name='herku', tex_id='herku',
                pos=(0, 0, 0), rot=(0, 0, 0), scale=(3.2, 3.2, 3.2)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)

#woman
class Woman(ExtendedBaseModel):
    def __init__(self, app, vao_name='woman', tex_id='woman',
                pos=(0, 0, 0), rot=(0, 0, 0), scale=(0.1, 0.1, 0.1)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)

#man
class Man(ExtendedBaseModel):
    def __init__(self, app, vao_name='man', tex_id='man',
                pos=(0, 0, 0), rot=(0, 0, 0), scale=(1.2, 1.2, 1.2)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)


#jarra
class Jarra(ExtendedBaseModel):
    def __init__(self, app, vao_name='jarra', tex_id='jarra',
                pos=(0, 0, 0), rot=(0, 0, 0), scale=(0.4, 0.4, 0.4)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)

#plato
class Plato(ExtendedBaseModel):
    def __init__(self, app, vao_name='plato', tex_id='plato',
                pos=(0, 0, 0), rot=(0, 0, 0), scale=(0.007, 0.007, 0.007)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)

#orando

class Orar(ExtendedBaseModel):
    def __init__(self, app, vao_name='orar', tex_id='orar',
                pos=(0, 0, 0), rot=(0, 0, 0), scale=(0.2, 0.2, 0.2)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)


#mujer
class Mujer(ExtendedBaseModel):
    def __init__(self, app, vao_name='mujer', tex_id='mujer',
                pos=(0, 0, 0), rot=(0, 0, 0), scale=(0.001, 0.001, 0.001)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)




#atenea
class Ate(ExtendedBaseModel):
    def __init__(self, app, vao_name='ate', tex_id='ate',
                pos=(0, 0, 0), rot=(0, 0, 0), scale=(0.001, 0.001, 0.001)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)

#zeus
class Zeus(ExtendedBaseModel):
    def __init__(self, app, vao_name='zeus', tex_id='zeus',
                pos=(0, 0, 0), rot=(0, 0, 0), scale=(0.1, 0.1, 0.1)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)

class SkyBox(BaseModel):
    def __init__(self, app, vao_name='skybox', tex_id='skybox',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()

    def update(self):
        self.program['m_view'].write(glm.mat4(glm.mat3(self.camera.m_view)))

    def on_init(self):
        # texture
        self.texture = self.app.mesh.texture.textures[self.tex_id]
        self.program['u_texture_skybox'] = 0
        self.texture.use(location=0)
        # mvp
        self.program['m_proj'].write(self.camera.m_proj)
        self.program['m_view'].write(glm.mat4(glm.mat3(self.camera.m_view)))


class Wall(ExtendedBaseModel): #este es el museo
    def __init__(self, app, vao_name='wall', tex_id='wall',
                pos=(0, 0, 0), rot=(0, 0, 0), scale=(0.7, 0.7, 0.7)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)


# Garden

class Leaf(ExtendedBaseModel): #este es el museo
    def __init__(self, app, vao_name='leaf', tex_id='leaf',
                pos=(0, 0, 0), rot=(0, 0, 0), scale=(0.7, 0.7, 0.7)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)

class Statue(ExtendedBaseModel): #este es el museo
    def __init__(self, app, vao_name='statue', tex_id='statue',
                pos=(0, 0, 0), rot=(0, 180, 0), scale=(0.7, 0.7, 0.7)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)

class Rose(ExtendedBaseModel): #este es el museo
    def __init__(self, app, vao_name='roses', tex_id='roses',
                pos=(0, 0, 0), rot=(0, 0, 0), scale=(0.7, 0.7, 0.7)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)

class Stigma(ExtendedBaseModel): #este es el museo
    def __init__(self, app, vao_name='stigma', tex_id='stigma',
                pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)

class Petal(ExtendedBaseModel): #este es el museo
    def __init__(self, app, vao_name='petals', tex_id='petals',
                pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)

class Ground(ExtendedBaseModel): #este es el museo
    def __init__(self, app, vao_name='ground', tex_id='ground',
                pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)

class Trunk(ExtendedBaseModel): #este es el museo
    def __init__(self, app, vao_name='trunk', tex_id='trunk',
                pos=(0, 0, 0), rot=(0, 0, 0), scale=(0.8, 0.8, 0.8)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)

class LeavesTree(ExtendedBaseModel): #este es el museo
    def __init__(self, app, vao_name='leavesTree', tex_id='leavesTree',
                pos=(0, 0, 0), rot=(0, 0, 0), scale=(0.8, 0.8, 0.8)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)

class Stem(ExtendedBaseModel): #este es el museo
    def __init__(self, app, vao_name='steam', tex_id='steam',
                pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)

class Grass(ExtendedBaseModel): #este es el museo
    def __init__(self, app, vao_name='grass', tex_id='grass',
                pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)

#garden pt2
class Pool(ExtendedBaseModel): #este es el museo
    def __init__(self, app, vao_name='pool', tex_id='pool',
                pos=(0, 0, 0), rot=(0, 0, 0), scale=(0.4, 0.4, 0.4)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)


#columna

class Col(ExtendedBaseModel):  # este es el museo
     def __init__(self, app, vao_name='col', tex_id='col',
                pos=(0, 0, 0), rot=(0, 0, 0), scale=(0.05, 0.05, 0.05)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)

#mariposa

class Mari(ExtendedBaseModel):  # este es el museo
     def __init__(self, app, vao_name='mari', tex_id='mari',
                pos=(0, 0, 0), rot=(0, 0, 0), scale=(0.005, 0.005, 0.005)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)


#skybox part


class AdvancedSkyBox(BaseModel):
    def __init__(self, app, vao_name='advanced_skybox', tex_id='skybox',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()

    def update(self):
        m_view = glm.mat4(glm.mat3(self.camera.m_view))
        self.program['m_invProjView'].write(glm.inverse(self.camera.m_proj * m_view))

    def on_init(self):
        # texture
        self.texture = self.app.mesh.texture.textures[self.tex_id]
        self.program['u_texture_skybox'] = 0
        self.texture.use(location=0)



















