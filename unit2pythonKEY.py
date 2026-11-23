from XRPLib.differential_drive import DifferentialDrive
from XRPLib.rangefinder import Rangefinder

# initalize variables
count = None
dist = None

#initalize sensors and motors
differentialDrive = DifferentialDrive.get_default_differential_drive()
rangefinder = Rangefinder.get_default_rangefinder()

# first section of course, 3 point turn in first corner to be able to round the corner easier. 
differentialDrive.straight(39, 0.5)
differentialDrive.turn(45, 1)
differentialDrive.straight(8, 0.5)
differentialDrive.turn(25, 0.5)
differentialDrive.straight(8, 0.5)
differentialDrive.turn(16, 0.5)
differentialDrive.straight(7, 0.5)
differentialDrive.straight((-1), 0.5)

# repeating until we get 3 readings that are below the threshold to reduce error
count = 0
while not count > 2:
  dist = rangefinder.distance()
  print(dist)
  if 20 > dist and 30000 > dist: # in testing, found that sensor will sometimes output a number around 60000 when an error occurs, guarding against this affecting the count.
    count = count + 1

# repeating until we get 3 readings that are above the threshold to reduce error
count = 0
while not count > 2:
  dist = rangefinder.distance()
  print(dist)
  if 20 < dist and 30000 > dist: # in testing, found that sensor will sometimes output a number around 60000 when an error occurs, guarding against this affecting the count.
    count = count + 1

# Drive through the next section of the course
differentialDrive.straight(54, 1)
differentialDrive.turn(45, 0.5)
differentialDrive.straight(17, 0.5)
differentialDrive.turn(48, 0.5)
differentialDrive.straight(7, 0.5)

# repeating until we get 3 readings that are below the threshold to reduce error
count = 0
while not count > 2:
  dist = rangefinder.distance()
  print(dist)
  if 20 > dist and 30000 > dist: # in testing, found that sensor will sometimes output a number around 60000 when an error occurs, guarding against this affecting the count.
    count = count + 1

# repeating until we get 3 readings that are above the threshold to reduce error
count = 0
while not count > 2:
  dist = rangefinder.distance()
  print(dist)
  if 20 < dist and 30000 > dist: # in testing, found that sensor will sometimes output a number around 60000 when an error occurs, guarding against this affecting the count.
    count = count + 1

# driving through the final stretch
differentialDrive.straight(54, 0.5)
differentialDrive.turn(90, (-0.5))
differentialDrive.straight(60, 0.5)

