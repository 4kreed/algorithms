#from numpy import sqrt
import math

class Point3D:

    #A point is defined by 3 coordinates
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


    #Commit 1: __init__(constructor), setters, getters and __str__ (tostring)
    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_z(self):
        return self.z

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def set_z(self, z):
        self.z = z

    def __str__(self):
        return 'Punto 3D (x=' + str(self.get_x()) + ',y=' + str(self.get_y()) + ',z=' + str(self.get_z()) + ')'
    
    
    #Commit 2: Distance to origin.
    def distance_to_origin(self):
        return math.sqrt((pow(self.get_x()) + pow(self.get_y()) + pow(self.get_z()))


    #Commit 3: Distance between 2 points.
    def calculate_distance(self, point_2):
        return math.sqrt(pow(self.get_x() - point_2.get_x(), 2) + pow(self.get_y() - point_2.get_y(), 2) + pow(self.get_z() - point_2.get_z(), 2))
        

    #Commit 4: Determine quadrant
    def calculate_quadrant(self):
        if self.get_x() == 0 or self.get_y() == 0 or self.get_z() == 0:
            return 0
        if self.get_x() > 0 and self.get_y() > 0:
            return 1
        if self.get_x() < 0 and self.get_y() > 0:
            return 2
        if self.get_x() < 0 and self.get_y() < 0:
            return 3
        if self.get_x() > 0 and self.get_y() < 0:
            return 4

    #Commit 5: Given a list of Points, determine which of them is closer to *self*
    def get_closest_point(self, points):
        closest_distance = 99999
        output = None
        for point in points:
            distance = self.calculate_distance(point)
            if distance < closest_distance:
                output = point
                closest_distance = distance
        return cantidato

if __name__ == "__main__":
    pass
