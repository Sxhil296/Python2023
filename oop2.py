class Room:
    length = 0.0
    breadth = 0.0

    # method to calculate area
    def calculate_area(self):
        print("Area of Room = ", self.length * self.breadth)

# create object of Room class
study_room = Room()

# assign values to all the attributes
study_room.length = 42.5
study_room.breadth = 30.8
study_room.calculate_area()


#create another object of Room class
bed_room = Room()
bed_room.length = 45.5
bed_room.breadth = 35
bed_room.calculate_area()