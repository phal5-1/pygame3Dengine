import pygame
import moderngl
import sys
#import glm

from model import *

import settings
import Time

from camera import Camera
from light import Light
from mesh import Mesh
from scene import Scene

from scene_renderer import SceneRenderer

class GraphicsEngine:
    initiated = False
    def __init__(self, windowDimensions = settings.screen_dimensions):
        if not GraphicsEngine.initiated:
            #WIN_SIZE
            self.screenDimensions = windowDimensions
            
            #openGL attr
            pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MAJOR_VERSION, 4)
            pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MINOR_VERSION, 5)
            pygame.display.gl_set_attribute(pygame.GL_CONTEXT_PROFILE_MASK, pygame.GL_CONTEXT_PROFILE_CORE)
            
            #openGL context
            pygame.display.set_mode(self.screenDimensions, flags=pygame.OPENGL | pygame.DOUBLEBUF)
            
            self.ctx = moderngl.create_context()
            #self.ctx.front_face = 'cw'
            #use depth
            self.ctx.enable(flags = moderngl.DEPTH_TEST | moderngl.CULL_FACE)
            
            self.clock = pygame.time.Clock()
            self.time = 0
            
            self.light = Light()
            
            self.camera = Camera(self)
            
            self.mesh = Mesh(self)
            
            self.scene = Scene(self)
            
            self.sceneRenderer = SceneRenderer(self)
            
            GraphicsEngine.initiated = True
        else: del self
        
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.mesh.destroy()
                pygame.quit()
                sys.exit()
                
    def render(self):
        self.ctx.clear(color = (0.08, 0.16, 0.18))
        
        self.sceneRenderer.render()
        
        pygame.display.flip()
        
    def get_time(self):
        self.time = pygame.time.get_ticks() * 0.001
        
    def run(self):
        self.get_time()
        self.check_events()
        self.camera.update()
        self.render()
        self.clock.tick(Time.framerate)
            
pygame.init()
pygame.event.set_grab(True)
pygame.mouse.set_visible(False)
app = GraphicsEngine()
while True:
    app.run()