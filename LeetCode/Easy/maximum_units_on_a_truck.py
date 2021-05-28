
def maximumUnits(boxTypes, truckSize):
    boxTypes.sort(key=lambda col: col[1], reverse=True)
    units = 0

    for type in boxTypes:
        if type[0] < truckSize:
            # there are less boxes than space left
            truckSize -= type[0] # these boxes have been added to the truck
            units += type[0] * type[1]
        else: 
            # type[0] >= truckSize:
            # these are the last boxes that'll be added to the truck
            units += truckSize * type[1]
            return units

    return units

boxTypes = [[5,10],[2,5],[4,7],[3,9]]
truckSize = 100

print(maximumUnits(boxTypes, truckSize))