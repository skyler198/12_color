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

color_sensor = ColorSensor(Port.S3) #Inicialice el sensor de color en el puerto 3

X = Motor(Port.A)
Y = Motor(Port.C)

while color_sensor.color()!=Color.RED: #Mientras el sensor no detecte rojo
    X.run(200) #Gira el motor X a 100 grados por segundo
    Y.run(200)
    wait(10)

while color_sensor.color()==Color.RED: #Mientras el sensor no detecte rojo
    X.run(-200) #Gira el motor X a 100 grados por segundo
    Y.run(-200)
    wait(2100)
    X.stop()
    Y.stop()