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

        #  museo pt1
        self.vaos['cat'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['cat'])

        self.vaos['shadow_cat'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['cat'])

     #head
        self.vaos['head'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['head'])

        self.vaos['shadow_head'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['head'])

        #mesa
        self.vaos['mesa'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['mesa'])

        self.vaos['shadow_mesa'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['mesa'])

        #herkules
        self.vaos['herku'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['herku'])

        self.vaos['shadow_herku'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['herku'])



        #woman
        self.vaos['woman'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['woman'])

        self.vaos['shadow_woman'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['woman'])

        #man
        self.vaos['man'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['man'])

        self.vaos['shadow_man'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['man'])

        #jarra

        self.vaos['jarra'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['jarra'])

        self.vaos['shadow_jarra'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['jarra'])

        #plato

        self.vaos['plato'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['plato'])

        self.vaos['shadow_plato'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['plato'])

        #orar

        self.vaos['orar'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['orar'])

        self.vaos['shadow_orar'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['orar'])

        #mujer
        self.vaos['mujer'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['mujer'])

        self.vaos['shadow_mujer'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['mujer'])



       #atenea
        self.vaos['ate'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['ate'])

        self.vaos['shadow_ate'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['ate'])
        #zeus
        self.vaos['zeus'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['zeus'])

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
