from XRPLib.defaults import *
import time

kp = 1.25
intersection_count = 0
intersection_detected = False  # Track intersection state
debounce_time = 1  # Time in seconds to wait before rechecking

def is_left_over_line():
    return reflectance.get_left() > 0.9

def is_right_over_line():
    return reflectance.get_right() > 0.9

def check_intersection():
    return is_left_over_line() and is_right_over_line()

while intersection_count < 3:
    left = reflectance.get_left()
    right = reflectance.get_right()

    if check_intersection():
        if not intersection_detected:
            intersection_count += 1
            intersection_detected = True
            print("intersection!")
    else:
        if intersection_detected:
            time.sleep(debounce_time)  # debounce before allowing next detection
        intersection_detected = False

    error = left - right
    base_speed = 0.25
    correction = kp * error

    left_speed = base_speed - correction
    right_speed = base_speed + correction

    drivetrain.set_effort(left_speed, right_speed)
