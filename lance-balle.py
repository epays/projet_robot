import time
import termios
import tty
import ev3dev.ev3 as ev3
import sys


motor_a = ev3.MediumMotor('outA')

#==============================================


#==============================================

def fire():
   motor_a.run_timed(time_sp=3000, duty_cycle_sp=100)

#==============================================

def forward():
   motor_left.run_direct(duty_cycle_sp=75)
   motor_right.run_direct(duty_cycle_sp=75)

#==============================================

def back():
   motor_left.run_direct(duty_cycle_sp=-75)
   motor_right.run_direct(duty_cycle_sp=-75)

#==============================================

def left():
   motor_left.run_direct( duty_cycle_sp=-75)
   motor_right.run_direct( duty_cycle_sp=75)

#==============================================

def right():
   motor_left.run_direct( duty_cycle_sp=75)
   motor_right.run_direct( duty_cycle_sp=-75)

#==============================================

def stop():
   motor_left.run_direct( duty_cycle_sp=0)
   motor_right.run_direct( duty_cycle_sp=-0)

#==============================================

while True:
   k = getch()
   print(k)
   if k == 'w':
      forward()
   if k == 's':
      back()
   if k == 'a':
      left()
   if k == 'd':
      right()
   if k == 'f':
      fire()
   if k == ' ':
      stop()
   if k == 'q':
      exit()