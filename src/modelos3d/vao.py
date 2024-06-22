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

        #  gradas vao
        self.vaos['cat'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['cat'])

        # gradas cat vao
        self.vaos['shadow_cat'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['cat'])
        ##        # cesped
        ##        self.vaos['cesped'] = self.get_vao(
        ##            program=self.program.programs['default'],
        ##            vbo=self.vbo.vbos['cesped'])
        ##
        ##        # shadow cesped vao
        ##        self.vaos['shadow_cesped'] = self.get_vao(
        ##            program=self.program.programs['shadow_map'],
        ##            vbo=self.vbo.vbos['cesped'])
        ##
        ####        # cesped
        ##        self.vaos['Detalles'] = self.get_vao(
        ##            program=self.program.programs['default'],
        ##            vbo=self.vbo.vbos['Detalles'])
        ##
        ##        # shadow cesped vao
        ##        self.vaos['shadow_Detalles'] = self.get_vao(
        ##            program=self.program.programs['shadow_map'],
        ##            vbo=self.vbo.vbos['Detalles'])
        ##

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
