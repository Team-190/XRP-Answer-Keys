from XRPLib.defaults import *
import time

# kp, this will be tuned
kp = 0.25

# drive forward 20 cm at 50% power
drivetrain.straight(20, (0.5))

# stop 
drivetrain.stop()

# wait for gate to close
while rangefinder.distance() > 15:
    pass

# wait 1/4 seconds to make sure the gate is fully down
time.sleep(0.25)

# while the gate is closed:
while rangefinder.distance() < 15:
    # calculate how far the robot is from the gate
    error = rangefinder.distance() - 5

    # calculate the effort, which is error times kp
    effort = error * kp

    # send the effort to the motor
    drivetrain.set_effort(effort, effort)

# stop
drivetrain.stop()

# wait for 1 second so the gate is fully out of the way
time.sleep(1)

# drive forward 40 cm
drivetrain.straight(40, (0.5))

# stop
drivetrain.stop()

# turn 90 degrees
drivetrain.turn(90)

# wait for gate to close
while rangefinder.distance() > 15:
    pass

# while the gate is closed:
while rangefinder.distance() < 15:
    # calculate how far the robot is from the gate
    error = rangefinder.distance() - 5

    # calculate the effort, which is error times kp
    effort = error * kp

    # send the effort to the motor
    drivetrain.set_effort(effort, effort)

# stop
drivetrain.stop()

# wait for 1 second so the gate is fully out of the way
time.sleep(1)

# drive forward 30 cm
drivetrain.straight(30, (0.5))

# turn 90 degrees
drivetrain.turn(90)

# wait 1/4 seconds to make sure the gate is fully down
time.sleep(0.25)

# drive forward 5 cm
drivetrain.straight(5, (0.5))

# stop
drivetrain.stop()

# wait for gate to close
while rangefinder.distance() > 15:
    pass

# wait 1/4 seconds to make sure the gate is fully down
time.sleep(0.25)

# wait for gate to open
while rangefinder.distance() < 15:
    # calculate how far the robot is from the gate
    error = rangefinder.distance() - 5

    # calculate the effort, which is error times kp
    effort = error * kp

    # send the effort to the motor
    drivetrain.set_effort(effort, effort)

# stop
drivetrain.stop()

# wait for 1 second so the gate is fully out of the way
time.sleep(1)

# drive forward 40 cm
drivetrain.straight(40, (0.5))
