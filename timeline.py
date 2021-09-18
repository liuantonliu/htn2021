from maps_api import *

class Timeline(): 
    """
    Timeline Object to organize map route/schedule and related details for user. 
    """

    # takes in start_location
    def __init__(self, start_address: str=None, start_coor: dict=None, end_address: str=None, end_coor: dict=None):
        """
        Initializes start and end locations, total trip time, and array corresponding to the order of locations.

        start_address: str
            Full starting address in a string seperated by commas. e.g. 280 Lester St., Waterloo, ON
        start_coor: dict
            dictionary containing coordiates of start location in the following format. Keys must be the same.
            e.g. {'lat': 43.4756084, 'lng': -80.53572779999999}
        end_address: str
            Full ending address in a string seperated by commas. e.g. 280 Lester St., Waterloo, ON
        end_coor: dict
            dictionary containing coordiates of end location in the following format. Keys must be the same.
            e.g. {'lat': 43.4756084, 'lng': -80.53572779999999}

        returns : None
        """
        self.total_trip_time = 0
        self.items = []

        if start_coor is None:
            start_coor = geocode_address(start_address)

        if end_coor is None:
            end_coor = geocode_address(end_address)

        self.set_start_location(start_coor)
        self.end_coor = end_coor

    def set_start_location(self, location):
        self.start_coor = location
        self.items[0:0] = [location]
        if len(self.items) != 1:
            #TODO:
            #recalculate directions from start location to second location
    
    def peek_end_coor(self):
        temp = self.items[:]
        temp.append(self.end_coor)
        self.items[len(temp)-2]["route_details"] = #get route details with new destination

        

    
