#!/usr/bin/env python

import RPi.GPIO as GPIO
import time


def main():

    print "executing script"

    # tell the GPIO module that we want 
    # to use the chip's pin numbering scheme
    GPIO.setmode(GPIO.BCM)
    # setup pin 25 as an output
    GPIO.setup(25,GPIO.OUT)

    # turn pin on 
    GPIO.output(25,True)
    # sleep for 3 seconds
    time.sleep(3)
    # turn the pin off
    GPIO.output(25,False)

    GPIO.cleanup()

if __name__=="__main__":
    main()
