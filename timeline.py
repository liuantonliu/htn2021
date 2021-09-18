from maps_api import *

class Timeline(): 
    """
    Timeline Object to organize map route/schedule and related details for user. 
    """

    # takes in start_location
    def __init__(self, start_address: str=None, end_address: str=None, start_time: str, end_time: str):
        """
        Initializes start and end locations, total trip time, and array corresponding to the order of locations.

        start_address: str
            Full starting address in a string seperated by commas. e.g. 280 Lester St., Waterloo, ON
        end_address: str
            Full ending address in a string seperated by commas. e.g. 280 Lester St., Waterloo, ON
        
        returns : None
        """
        self.total_trip_time = 0
        self.items = []

        self.start_address = start_address
        self.end_address = end_address
        
        self.set_start_location(start_coor)
        self.end_coor = end_coor

    def set_start_location(self, location):
        self.start_coor = location
        self.items[0:0] = [location]
        if len(self.items) != 1:
            #TODO:
            #recalculate directions from start location to second location
            self.items[0]["route_details"] = #new route details
        else:
            self.items[0]["route_details"] = None
    
    def peek_end_coor(self):
        temp = self.items[:]
        temp.append(self.end_coor)
        temp[len(temp)-2]["route_details"] = #get route details with new destination
        return temp

        

    
