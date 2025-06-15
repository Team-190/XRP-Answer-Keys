# Import libraries first
from XRPLib.defaults import *
import time

def is_left_over_line():
    return reflectance.get_left() > 0.9

def is_right_over_line():
    return reflectance.get_right() > 0.9

def check_intersection():
    return is_left_over_line() and is_right_over_line()

# Define variables here
# available variables from XRP Library: left_motor, right_motor, drivetrain,
#imu, rangefinder, reflectance, servo_one, board, webserver
# Create a variable name "board" and define it as the default board from XRPLib
board = Board.get_default_board()

# Create a variable name "differentialDrive" and define it as
# the default Differential Drive from XRPLib
differentialDrive = DifferentialDrive.get_default_differential_drive()

#Define functions here
# We don't have any functions yet but when we do we will write them here
# Write your code Here
board.wait_for_button()

differentialDrive.straight(50, (0.8))
differentialDrive.turn((90), 0.8)
differentialDrive.straight(20, 0.8)
differentialDrive.turn((-90), 0.8)
differentialDrive.straight(50, 0.8)




kp = 0.25

# initial ramp
drivetrain.straight(10, (0.5))
drivetrain.stop()

# wait for gate to close
while rangefinder.distance() > 15:
    pass

time.sleep(0.25)

# wait for gate to open
while rangefinder.distance() < 15:
    error = rangefinder.distance() - 5
    effort = error * kp
    drivetrain.set_effort(effort, effort)

drivetrain.stop()

# drive through gate
time.sleep(1)
drivetrain.straight(38.5, (0.5))


# stop
drivetrain.stop()

# turn 90 degrees
drivetrain.turn(90)

# wait for gate to close
while rangefinder.distance() > 15:
    pass

# wait for gate to open
while rangefinder.distance() < 15:
    error = rangefinder.distance() - 5
    effort = error * kp
    drivetrain.set_effort(effort, effort)
drivetrain.stop()

# drive through gate
time.sleep(1)
drivetrain.straight(30, (0.5))

# turn 90 degrees
drivetrain.turn(90)

time.sleep(0.25)

drivetrain.straight(5, (0.5))
drivetrain.stop()

# wait for gate to close
while rangefinder.distance() > 15:
    pass

time.sleep(0.25)

# wait for gate to open
while rangefinder.distance() < 15:
    error = rangefinder.distance() - 5
    effort = error * kp
    drivetrain.set_effort(effort, effort)

drivetrain.stop()

time.sleep(1)
drivetrain.straight(40, (0.5))

drivetrain.stop()

kp = 1.25
intersection_count = 0
intersection_detected = False
debounce_time = 1  # seconds
last_detection_time = 0  # timestamp of last intersection

def is_left_over_line():
    return reflectance.get_left() > 0.9

def is_right_over_line():
    return reflectance.get_right() > 0.9

def check_intersection():
    return is_left_over_line() and is_right_over_line()

while intersection_count < 3:
    current_time = time.time()

    left = reflectance.get_left()
    right = reflectance.get_right()

    if check_intersection():
        if not intersection_detected and (current_time - last_detection_time) > debounce_time:
            intersection_count += 1
            intersection_detected = True
            last_detection_time = current_time
            print("intersection!")
    else:
        intersection_detected = False  # Reset for next detection

    # Line following logic
    error = left - right
    base_speed = 0.25
    correction = kp * error

    left_speed = base_speed - correction
    right_speed = base_speed + correction

    drivetrain.set_effort(left_speed, right_speed)

drivetrain.stop()
    
drivetrain.turn(180)
drivetrain.straight(5, (-0.5))
servo_one.set_angle(0)
drivetrain.straight(5, (-0.5))
servo_one.set_angle(40)
drivetrain.turn(-180)

board.wait_for_button()

imu.calibrate(5)

drivetrain.straight(45, (0.5))

kp = 0.25

# initial ramp
drivetrain.straight(10, (0.5))
drivetrain.stop()

# wait for gate to close
while rangefinder.distance() > 15:
    pass

time.sleep(0.25)

# wait for gate to open
while rangefinder.distance() < 15:
    error = rangefinder.distance() - 5
    effort = error * kp
    drivetrain.set_effort(effort, effort)

drivetrain.stop()

# drive through gate
time.sleep(1)
drivetrain.straight(38.5, (0.5))


# stop
drivetrain.stop()

# turn 90 degrees
drivetrain.turn(-90)

# wait for gate to close
while rangefinder.distance() > 15:
    pass

# wait for gate to open
while rangefinder.distance() < 15:
    error = rangefinder.distance() - 5
    effort = error * kp
    drivetrain.set_effort(effort, effort)
drivetrain.stop()

# drive through gate
time.sleep(1)
drivetrain.straight(32, (0.5))

# turn 90 degrees
drivetrain.turn(-90)

time.sleep(0.25)

drivetrain.straight(5, (0.5))
drivetrain.stop()

# wait for gate to close
while rangefinder.distance() > 15:
    pass

time.sleep(0.25)

# wait for gate to open
while rangefinder.distance() < 15:
    error = rangefinder.distance() - 5
    effort = error * kp
    drivetrain.set_effort(effort, effort)

drivetrain.stop()

# drive through gate
time.sleep(1)
drivetrain.straight(40, (0.5))


differentialDrive.straight(50, (0.8))
differentialDrive.turn((90), 0.8)
differentialDrive.straight(20, 0.8)
differentialDrive.turn((-90), 0.8)
differentialDrive.straight(50, 0.8)