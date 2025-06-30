#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()


# Write your program here.
ev3.speaker.beep()

motorA = Motor(Port.A)
motorC = Motor(Port.C)

seguidorlinea = ColorSensor(Port.S3)


robot = DriveBase(motorA, motorC, wheel_diameter=55.5, axle_track=104)

while True:
    color = seguidorlinea.color()
    if color == Color.BLACK:
        robot.drive(30, 0)  # se mueve hacia adelante
    elif color == Color.WHITE:
        robot.drive(30, 30)  # se mueve hacia la derecha
    else:
        robot.drive(30, -30)  # se mueve a la izquierda

    wait(10) 