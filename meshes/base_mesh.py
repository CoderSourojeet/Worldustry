import numpy as np

class BaseMesh:
    def __init__(self):
        self.ctx = None # opengl context
        self.program = None # shader prgm
        self.vbo_format = None # '3f 3f'; format
        self.attrs: tuple[str, ...] = None # attributes
        self.vao = None # vertex array object

    def get_vertex_data(self) -> np.array: ...

    def get_vao(self):
        vertex_data = self.get_vertex_data()
        vbo = self.ctx.buffer(vertex_data)
        vao = self.ctx.vertex_array(
            self.program, [(vbo, self.vbo_format, *self.attrs)], skip_errors = True
        )
        return vao
    
    def render(self):
        self.vao.render()