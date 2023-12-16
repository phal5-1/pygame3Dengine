import pygame
import moderngl

import settings

class Texture:
    def __init__(self, ctx):
        self.ctx = ctx
        self.textures = {}
        self.textures[0] = self.get_texture(path = './Image/Textures/floorTileNa.png')
        self.textures['skybox'] = self.get_texture_cube(path = './Image/Textures/Skybox/', ext = 'png')
        self.textures['depth_texture'] = self.get_depth_texture()
        
    def get_texture_cube(self, path, ext = 'png'):
        faces = ['right', 'left', 'top', 'bottom', 'back', 'front']
        textures = []
        for face in faces:
            texture = pygame.image.load(path + f'{face}.{ext}').convert()
            if face in ['right', 'left', 'front', 'back']:
                texture = pygame.transform.flip(texture, flip_x = True, flip_y = False)
            else:
                texture = pygame.transform.flip(texture, flip_x = False, flip_y = True)
            textures.append(texture)
        
        size = textures[0].get_size()
        texture_cube = self.ctx.texture_cube(size = size, components = 3, data = None)
        
        for i in range(6):
            texture_data = pygame.image.tostring(textures[i], 'RGB')
            texture_cube.write(face = i, data = texture_data)
            
        return texture_cube
        
    def get_depth_texture(self):
        depth_texture = self.ctx.depth_texture((settings.screen_dimensions[0] * 2, settings.screen_dimensions[1] * 2))
        return depth_texture
        
    def get_texture(self, path):
        texture = pygame.image.load(path).convert()
        texture = pygame.transform.flip(texture, flip_x = False, flip_y = True)
        texture = self.ctx.texture(size = texture.get_size(), components = 3,
                                   data = pygame.image.tostring(texture, 'RGB'))
        
        texture.filter = (moderngl.LINEAR_MIPMAP_LINEAR, moderngl.LINEAR)
        texture.build_mipmaps()
        
        texture.anisotropy = 32.0
        return texture
    
    def destroy(self):
        [tex.release() for tex in self.textures.values()]