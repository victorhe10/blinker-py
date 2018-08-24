# -*- coding: utf-8 -*-

"""
"""

__author__ = 'stao'

from Blinker import Blinker, BlinkerButton, BlinkerNumber
from Blinker import BLINKER_LOG, BLINKER_WIFI

Blinker.setMode(BLINKER_WIFI)
Blinker.begin()

button1 = BlinkerButton("btn-abc")
number1 = BlinkerNumber("num-abc")

counter = 0


def button1_callback(btn, state):
    BLINKER_LOG("get button state: ", state)


button1.attach(button1_callback)

if __name__ == '__main__':

    while True:
        Blinker.run()

        if Blinker.available() is True:
            BLINKER_LOG("Blinker.readString(): ", Blinker.readString())
            counter += 1
            number1.print(counter)