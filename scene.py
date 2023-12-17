from model import *
from random import randint
import Time

class Scene:
    def __init__(self, app):
        self.app = app
        self.objects = []
        self.load()
        
        #skybox
        self.skybox = AdvancedSkyBox(app)
        
    def add_object(self, obj):
        self.objects.append(obj)
        
    def load(self):
        app = self.app
        add = self.add_object
        
        n, s = 80, 2
        
        for x in range(-n, n, s):
            for z in range(-n, n, s):
                add(Cube(app, pos = (x, -s, z)))
                
        add(Sphere(app, pos = (0, 10, 0)))
        add(Jellyfish(app, pos = (-2, 8.5, 2)))
        
        self.jelly = Jellyfish(app, pos = (-2, 1, 2))
        add(self.jelly)
        
        self.a = Cube(app, pos = [0, 1, -5])
        add(self.a)
        
        self.b = Plane(app, pos = (0, 1, 0), rot = (-90, 0, 0))
        add(self.b)
        
        self.c = Plane(app, pos = (5, 1, 0), rot = (-90, 0, 0), scale = (1, 1, 2), tex_id = 'minju')
        add(self.c)
        '''
        add(Cube(app))
        add(Cube(app, pos = (-2.5, 0, 0), rot = (45, 0, 0), scale = (1, 2, 1)))
        add(Cube(app, pos = (-5, 0, 0), rot = (0, 45, 0), scale = (2, 1, 1)))
        '''
        
    def render(self):
        for obj in self.objects:
            obj.render()
        self.skybox.render()
        
    def update(self):
        self.a.rot[0] = self.app.time
        self.b.rot[2] = self.app.time * 2
        self.c.pos[0] += Time.deltaTime
        self.jelly.rot[1] = self.app.time * 2
        #self.a.pos = self.app.camera.position