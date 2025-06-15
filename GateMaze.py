from XRPLib.defaults import *

# available variables from defaults: left_motor, right_motor, drivetrain,
#      imu, rangefinder, reflectance, servo_one, board, webserver
# Write your code Here

# Import libraries first
from XRPLib.defaults import *
import time

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
differentialDrive.straight(25, 0.8)
differentialDrive.turn((-90), 0.8)
differentialDrive.straight(50, 0.8)