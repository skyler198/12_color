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

sensor_color = ColorSensor(Port.S3)

while True:
    color = sensor_color.color()
    if color == sensor_color.color(): 
        motorA.run(70)
        motorC.run(70)
        if sensor_color.color() == Color.WHITE:
            motorA.run(200)
            motorC.run(30)
    else:
        motorA.run(0)
        motorC.run(0)