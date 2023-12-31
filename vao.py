from vbo import VBO
from shader_program import ShaderProgram

class VAO:
    def __init__(self, ctx):
        self.ctx = ctx
        self.vbo = VBO(ctx)
        self.program = ShaderProgram(ctx)
        self.vaos = {}
        
        #cube
        self.vaos['cube'] = self.get_vao(
            program = self.program.programs['default'],
            vbo = self.vbo.vbos['cube'])
        
        self.vaos['shadow_cube'] = self.get_vao(
            program = self.program.programs['shadow_map'],
            vbo = self.vbo.vbos['cube'])
        
        self.vaos['plane'] = self.get_vao(
            program = self.program.programs['default'],
            vbo = self.vbo.vbos['plane'])
        
        self.vaos['shadow_plane'] = self.get_vao(
            program = self.program.programs['shadow_map'],
            vbo = self.vbo.vbos['plane'])
        
        self.vaos['sphere'] = self.get_vao(
            program = self.program.programs['default'],
            vbo = self.vbo.vbos['sphere'])
        
        self.vaos['shadow_sphere'] = self.get_vao(
            program = self.program.programs['shadow_map'],
            vbo = self.vbo.vbos['sphere'])
        
        self.vaos['jellyfish'] = self.get_vao(
            program = self.program.programs['default'],
            vbo = self.vbo.vbos['jellyfish'])
        
        self.vaos['shadow_jellyfish'] = self.get_vao(
            program = self.program.programs['shadow_map'],
            vbo = self.vbo.vbos['jellyfish'])
        
        
        
        self.vaos['skybox'] = self.get_vao(
            program = self.program.programs['skybox'],
            vbo = self.vbo.vbos['skybox'])
        
        self.vaos['advanced_skybox'] = self.get_vao(
            program = self.program.programs['advanced_skybox'],
            vbo = self.vbo.vbos['advanced_skybox'])
        
    def get_vao(self, program, vbo):
        vao = self.ctx.vertex_array(program, [(vbo.vbo, vbo.format, *vbo.attribs)], skip_errors = True)
        return vao
    
    def destroy(self):
        self.vbo.destroy()
        self.program.destroy()