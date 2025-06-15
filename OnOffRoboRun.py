from XRPLib.defaults import *
import time

# Kp variable, this will need to be tuned
kp = 0.25

# Drives forward 20 cm at 50% power to get up the ramp and then stops
drivetrain.straight(20, (0.5))
drivetrain.stop()

# wait for gate to close
while rangefinder.distance() > 15:
    pass

# Small delay to prevent issues with the gate being half opened and half closed
time.sleep(0.25)

# wait for gate to open
while rangefinder.distance() < 15:
    pass

drivetrain.stop()

# drive through gate
time.sleep(1)
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

# drive through gate
time.sleep(1)
drivetrain.straight(30, (0.5))

# turn 90 degrees
drivetrain.turn(90)

# Small delay to prevent issues with the gate being half opened and half closed
time.sleep(0.25)

drivetrain.straight(5, (0.5))
drivetrain.stop()

# wait for gate to close
while rangefinder.distance() > 15:
    pass

# Small delay to prevent issues with the gate being half opened and half closed
time.sleep(0.25)

# wait for gate to open
while rangefinder.distance() < 15:
    pass

drivetrain.stop()

# drive through gate
time.sleep(1)
drivetrain.straight(40, (0.5))
