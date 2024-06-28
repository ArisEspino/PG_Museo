from vbo import VBO
from shader_program import ShaderProgram


class VAO:
    def __init__(self, ctx):
        self.ctx = ctx
        self.vbo = VBO(ctx)
        self.program = ShaderProgram(ctx)
        self.vaos = {}

        # cube vao
        self.vaos['cube'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['cube'])

        # shadow cube vao
        self.vaos['shadow_cube'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['cube'])

        #  museo vao
        self.vaos['cat'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['cat'])

        # gradas cat vao
        self.vaos['shadow_cat'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['cat'])


        # modelo fuente vao
        self.vaos['fuente'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['fuente'])

        # modelo fuente vao
        self.vaos['shadow_fuente'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['fuente'])
        #modelo mesa
        self.vaos['mesa'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['mesa'])

        # modelo mesa vao
        self.vaos['shadow_mesa'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['mesa'])

        #modelos cara sobre mesas
        self.vaos['cara'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['cara'])

        # modelo cara vao
        self.vaos['shadow_cara'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['cara'])

        #modelo cara2 mesa
        self.vaos['face'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['face'])

        # modelo cara2 vao
        self.vaos['shadow_face'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['face'])

        #choza modelo
        self.vaos['choza'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['choza'])

        # modelo choza vao
        self.vaos['shadow_choza'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['choza'])


  #herkules

        self.vaos['her'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['her'])

        # modelo col vao
        self.vaos['shadow_her'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['her'])
#mujer

        self.vaos['mujer'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['mujer'])


        self.vaos['shadow_mujer'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['mujer'])


        #soldado

        self.vaos['sol'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['sol'])

        self.vaos['shadow_sol'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['sol'])


        #cabeza2
        self.vaos['cab'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['cab'])

        self.vaos['shadow_cab'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['cab'])


 #leon
        self.vaos['leon'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['leon'])

        self.vaos['shadow_leon'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['leon'])


#m1
        self.vaos['m1'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['m1'])

        self.vaos['shadow_m1'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['m1'])



#m2
        self.vaos['m2'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['m2'])

        self.vaos['shadow_m2'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['m2'])


#m3

        self.vaos['m3'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['m3'])

        self.vaos['shadow_m3'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['m3'])


#m4

        self.vaos['m4'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['m4'])

        self.vaos['shadow_m4'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['m4'])





#m5

        self.vaos['m5'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['m5'])

        self.vaos['shadow_m5'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['m5'])


        #modelo de arboles

        self.vaos['tree'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['tree'])

        # modelo arboles vao
        self.vaos['shadow_tree'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['tree'])

        # skybox vao
        self.vaos['skybox'] = self.get_vao(
            program=self.program.programs['skybox'],
            vbo=self.vbo.vbos['skybox'])

        # advanced_skybox vao
        self.vaos['advanced_skybox'] = self.get_vao(
            program=self.program.programs['advanced_skybox'],
            vbo=self.vbo.vbos['advanced_skybox'])

    def get_vao(self, program, vbo):
        vao = self.ctx.vertex_array(program, [(vbo.vbo, vbo.format, *vbo.attribs)], skip_errors=True)
        return vao

    def destroy(self):
        self.vbo.destroy()
        self.program.destroy()
