#!/usr/bin/env python
# coding=UTF-8
#
#use to drive some device connect with gpio port on the raspberry pi.
# 
#author:chenke
#mail:lingqi1818@gmail.com

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)


#RP5 tank drive
#p1 p2 dirve the left motor
#p3 p4 drive the right motor
rp5_port=(11,12,13,15)

class RP5_CH2:
    def __init__(self,ports):
        self.ports=ports
        for port in ports:
            GPIO.setup(port, GPIO.OUT)

    def forward(self):
        self.left_forward()
        self.right_forward()


    def back(self):
        self.left_back()
        self.right_back()

    def right(self):
        self.left_back()
        self.right_forward()

    def left(self):
        self.left_forward()
        self.right_back()

    def stop(self):
       for port in self.ports:
            GPIO.output(port,GPIO.HIGH)
     
    def left_forward(self):
        GPIO.output(self.ports[0],GPIO.LOW)
        GPIO.output(self.ports[1],GPIO.HIGH)

    def right_forward(self):
        GPIO.output(self.ports[3],GPIO.LOW)
        GPIO.output(self.ports[2],GPIO.HIGH)

    def left_back(self):
        GPIO.output(self.ports[1],GPIO.LOW)
        GPIO.output(self.ports[0],GPIO.HIGH)
        
    def right_back(self):
        GPIO.output(self.ports[2],GPIO.LOW)
        GPIO.output(self.ports[3],GPIO.HIGH)

rp5=RP5_CH2(rp5_port)
