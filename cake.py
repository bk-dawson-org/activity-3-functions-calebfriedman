import math

height1 = float(input("Height of one layer pls for your first tier "))
radius1 = float(input("radius of one layer pls for your first tier "))
layers1 = float(input("number of layers pls for your first tier "))
height2 = float(input("Height of one layer pls for your 2nd tier "))
radius2 = float(input("radius of one layer pls for your 2nd tier "))
layers2 = float(input("number of layers pls for your 2nd tier "))

def getCylinderVol(height1, radius1, layers1, height2, radius2, layers2):
    vol1 = (math.pi*radius1**2*height1)*layers1 
    vol2 = (math.pi*radius2**2*height2)*layers2
    vol = vol1 + vol2
    return vol

volume = getCylinderVol(height1, radius1, layers1, height2, radius2, layers2)

def getFrosting(radius1, layers1, radius2, layers2):
    frosting = (math.pi*radius1**2)*layers1 + (math.pi*radius2**2)*layers2
    return frosting

amount_frosting = round(getFrosting(radius1, layers1, radius2, layers2), 2)

print("your cake will be", round(volume, 3), "Cubic cm and the amount of frosting needed is", amount_frosting, "square cm")


volume_slice = float(input("How much in volume do you want each slice to be "))

def getNumberSlices(volume, volume_slice):
    slices = volume/volume_slice
    return slices

print("You will get", round(getNumberSlices(volume, volume_slice), 0),"slices." )