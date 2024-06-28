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

 # aca cambiamos la escala del museo
class Cat(ExtendedBaseModel): #este es el museo
    def __init__(self, app, vao_name='cat', tex_id='cat',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(0.3, 0.3, 0.3)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)



#ahora para la fuente
class Fuente(ExtendedBaseModel):      #modelo de la estatua
    def __init__(self, app, vao_name='fuente', tex_id='fuente',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(0.5, 0.5, 0.5)): #cambiar la escala del obj
        super().__init__(app, vao_name, tex_id, pos, rot, scale)

#mesa
class Mesa(ExtendedBaseModel):
    def __init__(self, app, vao_name='mesa', tex_id='mesa',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(0.6, 0.6, 0.6)): #cambiar la escala del obj
        super().__init__(app, vao_name, tex_id, pos, rot, scale)

#modelo de contenido de mesa face 1
class Face1(ExtendedBaseModel):
    def __init__(self, app, vao_name='cara', tex_id='cara',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(0.04, 0.04, 0.04)): #cambiar la escala del obj
        super().__init__(app, vao_name, tex_id, pos, rot, scale)


#modelo cara2
class Face2(ExtendedBaseModel):
    def __init__(self, app, vao_name='face', tex_id='face',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(0.03, 0.03, 0.03)):  # cambiar la escala del obj
        super().__init__(app, vao_name, tex_id, pos, rot, scale)


#choza modelo
class Choza(ExtendedBaseModel):
    def __init__(self, app, vao_name='choza', tex_id='choza',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(0.9, 0.9, 0.9)):  # cambiar la escala del obj
        super().__init__(app, vao_name, tex_id, pos, rot, scale)




#herkules
class Her(ExtendedBaseModel):
    def __init__(self, app, vao_name='her', tex_id='her',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(0.1, 0.1, 0.1)):  # cambiar la escala del obj
        super().__init__(app, vao_name, tex_id, pos, rot, scale)


#mujer
class Mujer(ExtendedBaseModel):
    def __init__(self, app, vao_name='mujer', tex_id='mujer',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(0.03, 0.03, 0.03)):  # cambiar la escala del obj
        super().__init__(app, vao_name, tex_id, pos, rot, scale)


#CABEZA soldado
class Sol(ExtendedBaseModel):
    def __init__(self, app, vao_name='sol', tex_id='sol',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(0.1, 0.1, 0.1)):  # cambiar la escala del obj
        super().__init__(app, vao_name, tex_id, pos, rot, scale)


#cabeza2
class Cab(ExtendedBaseModel):
    def __init__(self, app, vao_name='cab', tex_id='cab',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(0.03, 0.03, 0.03)):  # cambiar la escala del obj
        super().__init__(app, vao_name, tex_id, pos, rot, scale)





#leon 1/8
class Leon(ExtendedBaseModel):
    def __init__(self, app, vao_name='leon', tex_id='leon',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(0.3, 0.3, 0.3)):  # cambiar la escala del obj
        super().__init__(app, vao_name, tex_id, pos, rot, scale)

#m1mu
class M1(ExtendedBaseModel):
    def __init__(self, app, vao_name='m1', tex_id='m1',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(0.09, 0.09, 0.09)):  # cambiar la escala del obj
        super().__init__(app, vao_name, tex_id, pos, rot, scale)

#m2sol
class M2(ExtendedBaseModel):
    def __init__(self, app, vao_name='m2', tex_id='m2',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(0.09, 0.09, 0.09)):  # cambiar la escala del obj
        super().__init__(app, vao_name, tex_id, pos, rot, scale)

#m3di
class M3(ExtendedBaseModel):
    def __init__(self, app, vao_name='m3', tex_id='m3',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(0.05, 0.05, 0.05)):  # cambiar la escala del obj
        super().__init__(app, vao_name, tex_id, pos, rot, scale)


#m4c
class M4(ExtendedBaseModel):
    def __init__(self, app, vao_name='m4', tex_id='m4',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(0.09, 0.09, 0.09)):  # cambiar la escala del obj
        super().__init__(app, vao_name, tex_id, pos, rot, scale)


#m5c

class M5(ExtendedBaseModel):
    def __init__(self, app, vao_name='m5', tex_id='m5',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(0.04, 0.04, 0.04)):  # cambiar la escala del obj
        super().__init__(app, vao_name, tex_id, pos, rot, scale)



#ahora para los arboles
class Tree(ExtendedBaseModel):  # modelo de la estatua
    def __init__(self, app, vao_name='tree', tex_id='tree',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(0.4, 0.4, 0.4)):  # cambiar la escala del obj
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



















