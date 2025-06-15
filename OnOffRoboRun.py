from XRPLib.defaults import *
import time

# kp variable, this will need to be tuned
kp = 0.25

# drive forward 20 cm at 50% power
drivetrain.straight(20, (0.5))

# stop
drivetrain.stop()

# wait for gate to close
while rangefinder.distance() > 15:
    pass

# Small delay to prevent issues with the gate being half opened and half closed
time.sleep(0.25)

# wait for gate to open
while rangefinder.distance() < 15:
    pass

# stop
drivetrain.stop()

# wait for the gate to be fully out of the way
time.sleep(1)

# drive forward 45 cm
drivetrain.straight(45, (0.5))

# stop
drivetrain.stop()

# turn 90 degrees
drivetrain.turn(90)

# wait for gate to close
while rangefinder.distance() > 15:
    pass

# wait for gate to open
while rangefinder.distance() < 15:
    pass

drivetrain.stop()

# wait for the gate to be fully out of the way
time.sleep(1)

# drive forward 30 cm
drivetrain.straight(30, (0.5))

# turn 90 degrees
drivetrain.turn(90)

# Small delay to prevent issues with the gate being half opened and half closed
time.sleep(0.25)

# drive forward 5 cm
drivetrain.straight(5, (0.5))

# stop
drivetrain.stop()

# wait for gate to close
while rangefinder.distance() > 15:
    pass

# Small delay to prevent issues with the gate being half opened and half closed
time.sleep(0.25)

# wait for gate to open
while rangefinder.distance() < 15:
    pass

# stop
drivetrain.stop()

# wait for the gate to be fully out of the way
time.sleep(1)

# drive forward 40 cm
drivetrain.straight(40, (0.5))
