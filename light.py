import glm

class Light:
    def __init__(self, position = (50, 30, -50), color = (1, 1, 1)):
        self.position = glm.vec3(position)
        self.color = glm.vec3(color)
        self.direction = glm.vec3(0, 0, 0)
        #intensities
        self.Ia = 0.1 * self.color #ambient
        self.Id = 0.8 * self.color #diffuse
        self.Is = 0.0 * self.color #specular
        #view matrix
        #self.m_view_light = self.get_view_matrix(self.direction)
        
    def get_view_matrix(self, tgt):
        return glm.lookAt(self.position, tgt, glm.vec3(0, 1, 0))