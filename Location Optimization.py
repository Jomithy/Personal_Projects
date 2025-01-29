# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 10:44:12 2024

@author: jomil
"""

import numpy as np
from scipy.optimize import minimize
from geopy.distance import great_circle
from geopy.geocoders import Nominatim

# Function to calculate the sum of great-circle distances from a candidate point to all given points
def total_distance(opt_point, ref_points):
    lat1, lon1 = opt_point
    distances = [ great_circle((lat1, lon1), (lat2, lon2)).kilometers for lat2, lon2 in ref_points]
    return np.sum(distances)

# Function to find the optimal meeting point
def optimal_meeting_point(latitudes, longitudes):
    ref_points = list(zip(latitudes, longitudes))

    # Initial guess is the centroid of the given points 
    initial_guess = [np.mean(latitudes), np.mean(longitudes)]

    # Minimize the total distance
    result = minimize(total_distance, initial_guess, args=(ref_points,), method='L-BFGS-B',
                      bounds=[(-90, 90), (-180, 180)])
    
    return result.x


loc = Nominatim(user_agent="GetLoc")


locations = ["1311 S 5th St, Waco, TX 76706",
             "2515 Speedway, Austin, TX 78712",
             "400 Bizzell St, College Station, TX 77840"]
latitudes = [loc.geocode(i).latitude for i in locations]
longitudes = [loc.geocode(i).longitude for i in locations]

#print([(i,j) for i,j in list(zip(latitudes,longitudes))]) # debug

optimal_point = optimal_meeting_point(latitudes, longitudes)
locname = loc.reverse(", ".join([str(i) for i in optimal_point]))
address = locname.address.split(", ")

print("Optimal location: \n{} {}".format(" ".join(address[:-1]),tuple(optimal_point)))
