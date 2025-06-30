#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


ev3 = EV3Brick()
mA = Motor(Port.A)
mC = Motor(Port.C)
sensor_color = ColorSensor(Port.S3)

robot = DriveBase(mA, mC, 55.5, 104)

guardavalores = []

sensor_sobre_linea_negro = False
tiempo = 0
limitetiempoms = 150  

robot.drive(20, 0)

while len(guardavalores) < 16:  
    color_detectado = sensor_color.color()

    if color_detectado == Color.BLACK:
        if  not sensor_sobre_linea_negro:
            sensor_sobre_linea_negro = True
            tiempo = 0
        else:
            tiempo += 10
    else:
        if sensor_sobre_linea_negro:
            if tiempo >= limitetiempoms:
                guardavalores.append(1)
            else:
                guardavalores.append(0)
            sensor_sobre_linea_negro = False

    ev3.screen.clear()
    ev3.screen.draw_text(10, 50, guardavalores)

    wait(10)

robot.stop()
ev3.speaker.beep()

