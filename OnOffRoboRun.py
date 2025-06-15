from XRPLib.defaults import *
import time

kp = 0.25

# initial ramp
drivetrain.straight(20, (0.5))
drivetrain.stop()

# wait for gate to close
while rangefinder.distance() > 15:
    pass

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

time.sleep(0.25)

drivetrain.straight(5, (0.5))
drivetrain.stop()

# wait for gate to close
while rangefinder.distance() > 15:
    pass

time.sleep(0.25)

# wait for gate to open
while rangefinder.distance() < 15:
    pass

drivetrain.stop()

# drive through gate
time.sleep(1)
drivetrain.straight(40, (0.5))