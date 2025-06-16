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
mA = Motor(Port.A)
mC = Motor(Port.C)
color_sensor = ColorSensor(Port.S3)

Color_texto = {
    #Color.NONE: "Ninguno",
    Color.BLACK: "Negro",
    Color.BLUE: "Azul",
    Color.GREEN: "Verde",
    Color.YELLOW: "Amarillo",
    Color.RED: "Rojo",
    Color.WHITE: "Blanco",
    Color.BROWN: "Marrón"
}
while True:
    color = color_sensor.color()
    nombre_color = Color_texto.get(color, "Desconocido")
    ev3.screen.clear()
    ev3.screen.draw_text(10, 20, "Color detectado:")
    wait(3000)  # Espera 3 segundos para que el texto se muestre
    ev3.screen.draw_text(10, 60, nombre_color)
    wait(3000)  # Espera 3 segundos para que el texto se muestre
    ev3.screen.clear()  # Limpia la pantalla antes de la siguiente iteración
    wait(100)  # Espera un poco antes de la siguiente lectura del color
  
