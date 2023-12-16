import glm
import pygame
import typing

import Time
import settings

#you can install glm through 'pip install PyGLM'.

NEAR: typing.Final = 0.1
FAR: typing.Final = 100
SPEED = 10
SENSITIVITY = 0.1

class Camera:
    def __init__(self, app, position = (0, 0, 4), yaw = -90, pitch = 0):
        self.app = app
        self.aspect_ratio = settings.screen_aspect_ratio
        self.position = glm.vec3(position)
        self.up = glm.vec3(0, 1, 0)
        self.right = glm.vec3(1, 0, 0)
        self.forward = glm.vec3(0, 0, -1)
        self.yaw = yaw
        self.pitch = pitch
        #view matrix
        self.m_view = self.get_view_matrix()
        #projrction matrix
        self.m_proj = self.get_projection_matrix()
        
    def update(self):
        self.move()
        self.rotate()
        self.update_camera_vectors()
        self.m_view = self.get_view_matrix()
        
    def rotate(self):
        rel_x, rel_y = pygame.mouse.get_rel()
        self.yaw += rel_x * SENSITIVITY
        self.pitch -= rel_y * SENSITIVITY
        self.pitch = max(-89, min(89, self.pitch))
        pygame.mouse.set_pos((1920 * 0.5, 1080 * 0.5))
        
    def update_camera_vectors(self):
        yaw, pitch = glm.radians(self.yaw), glm.radians(self.pitch)
        
        self.forward.x = glm.cos(yaw) * glm.cos(pitch)
        self.forward.y = glm.sin(pitch)
        self.forward.z = glm.sin(yaw) * glm.cos(pitch)
        
        self.forward = glm.normalize(self.forward)
        self.right = glm.normalize(glm.cross(self.forward, glm.vec3(0, 1, 0)))
        self.up = glm.cross(self.right, self.forward)
        #self.up = glm.normalize(glm.cross(self.right, self.forward))
        
    def move(self):
        speed = SPEED * Time.deltaTime
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_w]:
            self.position += self.forward * speed
        if keys[pygame.K_s]:
            self.position -= self.forward * speed
        if keys[pygame.K_d]:
            self.position += self.right * speed
        if keys[pygame.K_a]:
            self.position -= self.right * speed
        if keys[pygame.K_SPACE]:
            self.position += self.up * speed
        if keys[pygame.K_LSHIFT]:
            self.position -= self.up * speed
        
    def get_view_matrix(self):
        return glm.lookAt(self.position, self.position + self.forward, self.up)
        
    def get_projection_matrix(self):
        return glm.perspective(settings.FOV_H, settings.screen_aspect_ratio, NEAR, FAR)
    