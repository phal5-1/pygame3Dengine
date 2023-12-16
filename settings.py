import numpy
import typing

pi: typing.Final = 3.14159265358979323846264338327950288419716939937510582097494459230781640
EulerianToRadian: typing.Final = pi / 180

screen_width = 1920
screen_height = 1080
screen_dimensions = (screen_width, screen_height)
screen_aspect_ratio = screen_width / screen_height
reciprocal_screen_width = 1 / screen_width
reciprocal_screen_height = 1 / screen_height

FOV_V = 60 * EulerianToRadian
FOV_H = numpy.arctan(numpy.tan(FOV_V) * screen_height * reciprocal_screen_width)
FOV = (FOV_H, FOV_V)

gravity = (0.0, -9.81, 0.0)

numSubSteps = 15
paused = True