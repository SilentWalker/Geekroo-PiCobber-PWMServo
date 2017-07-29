#!/usr/bin/python

from Raspi_PWM_Servo_Driver import PWM
import time
import sys
# ===========================================================================
# Example Code
# ===========================================================================

# Initialise the PWM device using the default address
# bmp = PWM(0x40, debug=True)
pwm = PWM(0x6F, debug=True)

#servoMin = 150  # Min pulse length out of 4096
#servoMax = 600  # Max pulse length out of 4096
#默认频率是60Hz
freq = 60
#如果传入了新的频率, 则使用指定数值
if sys.argv[1]:
  freq =  sys.argv[1]

pwm.setPWMFreq(freq)                        # Set frequency to 60 Hz




