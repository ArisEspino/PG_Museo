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
            vbo = self.vbo.vbos['cube'])

        # shadow cube vao
        self.vaos['shadow_cube'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo = self.vbo.vbos['cube'])

        # Modelo vao
        self.vaos['modelo'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['modelo'])

        # shadow Modelo vao
        self.vaos['shadow_modelo'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['modelo'])

        # Statue1 vao
        self.vaos['statue1'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['statue1'])

        # shadow Statue1 vao
        self.vaos['shadow_statue1'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['statue1'])

        # Zeus vao
        self.vaos['zeus'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['zeus'])

        # shadow Zeus vao
        self.vaos['shadow_zeus'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['zeus'])

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