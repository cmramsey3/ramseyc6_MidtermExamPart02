# bridgeMonitor.py
# Bill Nicholson
# nicholdw@ucmail.uc.edu

import random


class BridgeMonitor():
    """
    Simulate the system that monitors a vehicle bridge 
    """
    def __init__(self):
        pass
    
    def getVehicleCount(self):
        """
        Get the count of cars that passed over the bridge
        @return int: The number of cars called since the last time this method was invoked. 
        @raise an exception if the bridge is currently closed.
        """
        if random.randint(100, 200) % 10 == 0:
            raise Exception("Bridge is closed")
        return random.randint(0, 100)
