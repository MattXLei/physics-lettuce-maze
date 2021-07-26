from turtle import *
from time import sleep

def await_loading(degrees = [0], color = [1.0, 0.0, 0.0]):  # intentionally dangerous default values

    if degrees[0] == 0:
        color.append(color.pop(0))
        loading.color(color)

    loading.tilt(STEP)

    degrees[0] = (degrees[0] + STEP) % 360

    screen.ontimer(await_loading, 10)

STEP = -12  # should be divisor of 360
GAP = 45  # in degrees
PEN_SIZE = 200  # emulated pen width
RADIUS = 250
screen = Screen()
loading = Turtle()
loading.speed('fastest')
loading.backward(RADIUS)
loading.right(90)

loading.begin_poly()
loading.circle(RADIUS, 360 - GAP, 60)
loading.left(90)
loading.forward(PEN_SIZE)
loading.right(90)
loading.circle(RADIUS - PEN_SIZE, GAP - 360, 60)
loading.end_poly()

screen = Screen()
screen.addshape('loading', loading.get_poly())

loading.reset()
loading.shape('loading')

await_loading()
