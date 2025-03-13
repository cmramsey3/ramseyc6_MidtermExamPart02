# File Name : main.py
# Student Name: Colton Ramsey
# email: ramseyc6@mail.uc.edu
# Assignment Number: Midterm Exam Part 02
# Due Date: 03/12/2025
# Course #/Section: IS 4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: Midterm exam where we are editing a visual studio projetc

# Brief Description of what this module does: This module runs the given method to us by professor Nicholson 100 times and counts
# the amount of cars that cross the bridge and the amount of times the bridge was closed.
# Citations: None
# Anything else that's relevant: None

from bridgePackage.bridge import *

if __name__ == "__main__":
    print("ramseyc6@mail.uc.edu")

    bridge_crossings = BridgeMonitor()
    
    count_cars = 0
    closings = 0

    for i in range(0, 100):
        try:
            count_cars = count_cars + bridge_crossings.getVehicleCount()
        except:
            closings = closings + 1
    print("Total Vehicles: ", count_cars)
    print("Total Closings: ", closings)
