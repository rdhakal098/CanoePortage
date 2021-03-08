print("What is your distance in rods")
rdsDistance = float(input())


def Conversions():
    print("Distance in Rods: ", rdsDistance)
    print("Distance in Meters: ",  rdsDistance * 5.0292)
    print("Distance in Feet: ", ((rdsDistance * 5.0292) / 0.3048))
    print("Distance in Miles: ", ((rdsDistance * 5.0292) / 1609.34))
    print("Distance in Furlongs: ",  rdsDistance / 40)
    print('Time to walk', rdsDistance, "rods:",
          (rdsDistance * 0.06048402129))

Conversions()

# 1 rod = 5.0292 meters
# 1 furlong = 40 rods
# 1 mile = 1609.34 meters
# 1 foot = 0.3048 meters
# average walking speed is 3.1 miles per hour
