from XRPLib.defaults import *
import time

# kp, this will need to be tuned
kp = 1.25

# variable to keep track of the number of intersections
intersection_count = 0

# variable to keep track of when an insersection is reached
intersection_detected = False

# variable time in seconds to wait before rechecking
debounce_time = 1

# function to keep track of if the left reflectance sensor sees a dark color
def is_left_over_line():
    # returns true if the left reflectance sensor value is over 0.9
    return reflectance.get_left() > 0.9

# function to keep track of if the right reflectance sensor sees a dark color
def is_right_over_line():
    # returns true if the right reflectance sensor value is over 0.9
    return reflectance.get_right() > 0.9

# function to keep track of if the left AND right reflectance sensors see dark colors, meaning the robot sees an intersection
def check_intersection():
    # returns true if both reflectance sensors see dark colors
    return is_left_over_line() and is_right_over_line()

# while the robot has seen fewer than 3 intersections
while intersection_count < 3:
    # get the left reflectance sensor value
    left = reflectance.get_left()

    # get the right reflectance sensor value
    right = reflectance.get_right()

    # checks if the robot sees an intersection
    if check_intersection():
        if not intersection_detected:
            # increment the number of intersections the robot has seen
            intersection_count += 1

            # sets that the robot just saw an intersection
            intersection_detected = True
            
    # if the robot does not see an intersection
    else:
        if intersection_detected
            # wait one second so the robot doesn't see the same intersection twice
            time.sleep(debounce_time) 

        # set the intersection_detected variable to False
        intersection_detected = False

    # calculates the error, which is left sensor value minus the right sensor value
    error = left - right

    # defines the base speed of the robot when the error is 0
    base_speed = 0.25

    # defines the effort to be added to the right side and removed from the left side
    effort = kp * error

    # calculates the speed for the left wheeel
    left_speed = base_speed - effort

    # calculates the speed for the left wheeel
    right_speed = base_speed + effort

    # sets the effort of the left and right sides of the robot
    drivetrain.set_effort(left_speed, right_speed)
