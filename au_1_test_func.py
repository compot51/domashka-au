#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math  # импортируем библиотеку с мат. функциями
import numpy  # импортируем библиотеку numpy
import matplotlib.pyplot as mpp  # импортируем matplotlib.pyplot как mpp

# Эта программа рисует график функции, заданной выражением ниже

if __name__ == '__main__':  # проверка, запускается ли программа как основная 
    arguments = numpy.arange(0, 200, 0.1)  # передаем в arguments значения от 0 до 200 с шагом 0.1
    mpp.plot(
        arguments,  # передаем значения для построения графика
        [math.sin(a) * math.sin(a / 20.0) for a in arguments]  # сама функция графика
    )
    mpp.show()  # показ графика
