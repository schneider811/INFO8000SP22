#this is a class

from cmath import pi


class CylinderBucket:
    def __init__(self,height_cm,radius_cm):
        # Input: height of the cylinder and the radius of the cylinder
        # output: an initialized cylinder, with properties height and radius
        #self.cylinder = [height_cm,radius_cm]
        self.height = height_cm
        self.radius = radius_cm # his answer
        self._currentheight = 0
        self._quantity = 0
        self._area = self.height * pi * (self.radius**2)

    def fill(self,quantity_cm3):
        #input volume of water to fill the bucket with
        #output: the amount of water put in, less any that spilled over
        height = quantity_cm3/self._area
        if self._currentheight + height > self.height:
            height_over = self._currentheight + height - self.height
            volume_over = height_over*self._area
            return quantity_cm3 - volume_over
        else:
            self._currentheight += height
            return quantity_cm3
        
        
        # self._quantity = quantity_cm3
        # volume_cylinder = self.height * pi * (self.radius**2)
        # if quantity_cm3 - volume_cylinder > 0:
        #     water_fill = volume_cylinder
        #     return water_fill
        # else:
        #     return quantity_cm3

    def fill_level(self):
        #input: none
        #output: height of water so far
        
        return self._currentheight
    