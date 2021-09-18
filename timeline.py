
class Timeline():
    def __init__(self):
        #array of stuff
        self.total_trip_time = 0
        self.items = []

        self.start_location = None
        self.end_location = None

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def empty(self):
        return not self.items

    def set_start_location(self, location):
        self.start_location = None
        if empty():
            #get start location details, then push
            #TO DO: Reference location details function
            self.push(location)
        
        