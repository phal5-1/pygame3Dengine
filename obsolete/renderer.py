# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 19:38:25 2023

@author: phlnx

"""

import pygame
import numpy
import settings

pygame.init()

screen = pygame.display.set_mode(settings.screen_dimensions)
surface = pygame.surface.Surface(settings.screen_dimensions)

run = True



clock = pygame.time.Clock()