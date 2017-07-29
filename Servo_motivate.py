from Raspi_PWM_Servo_Driver import PWM
import time
import sys
pwm = PWM(0x6F, debug=True)

if sys.argv:
  channel = sys.argv[1]
  low = sys.argv[2]
  high = sys.argv[3]
  pwm.setPWM(channel, low, high)
else:
  print 'no argv for servo'