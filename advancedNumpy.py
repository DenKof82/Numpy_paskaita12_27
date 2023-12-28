import numpy as np

Task 3: Complex/Mixed data types
You are provided example data for stations. Your task is to:

1.Filter for stations ST01 and ST02
2.Calculate mean (average) temeprature across all stations
3.Sort based on the temperatures
4.Convert the temperature from Celsius to Farenheit"""

"""#1. Filter for stations ST01 and ST02

stations = [(f"ST{i+1:02d}", np.random.uniform(-10, 30)) for i in range(100)]
print(stations[:10])


filtered_stations = [station for station in stations if station[0] in ["ST01", "ST02"]]
print(filtered_stations)

 #2.Calculating the mean temperature across all stations

# Extracting the temperature values from the stations list
temperatures = [temp for _, temp in stations]

# Calculating the mean temperature
mean_temperature = np.mean(temperatures)
print(mean_temperature)

# 3.Sorting the stations based on the temperatures

sorted_stations = sorted(stations, key=lambda x: x[1])
print(sorted_stations[:5])

# 4.Converting the temperatures from Celsius to Fahrenheit

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

stations_fahrenheit = [(station[0], celsius_to_fahrenheit(station[1])) for station in stations]
print(stations_fahrenheit[:10])

"""Task 4: more fields
Now let's imagine a world is a sphere, and add the coordinates of each of the stations. With the new data

1.Find the distance from one station to all other stations. 
If you want you can calculate the actual distance using a formula to find the distance between two 
points on a sphere or for the sake of simplicity use the euclidian distance
2.Find the station with the shortest mean path to all the other stations
3.Find the shortest path connecting three stations
4.Find the distance between 5 coldest stations.
5.Split the world into sections of 10 degrees horizontally and reduce the temperatures of the 
stations moving up by 4 degrees for each 10 degrees (the further north or south 
we go from the equator (the middle) the colder it gets)
6.Split the world into sections of 10 degrees vertically and 10 degrees horizontally. 
Find the average temperature and number of stations in each section. If there are no 
stations, the temperature should be np.nan"""

"""from scipy.spatial import distance_matrix


# Creating stations with coordinates on a sphere
np.random.seed(0)  # For reproducibility
stations = [
    (
        f"ST{i+1:02d}",  # Name
        temp:=np.random.uniform(-10, 30),  # Temperature (°C)
        x:=np.random.normal(),  # X coordinate on a point sphere
        y:=np.random.normal(),  # Y coordinate on a point sphere
        z:=np.random.normal(),  # Z coordinate on a point sphere
        np.linalg.norm([x, y, z])  # Norm for normalizing each point on the surface of a sphere
    )
    for i in range(100)
]

# Normalizing the points to the surface of the sphere
stations = [(name, temp, x/norm, y/norm, z/norm) for name, temp, x, y, z, norm in stations]

# Sorting the stations based on their temperature
sorted_stations_by_temp = sorted(stations, key=lambda x: x[1])

# Selecting the 5 coldest stations
coldest_stations = sorted_stations_by_temp[:5]

# Extracting the coordinates of the 5 coldest stations
coldest_stations_coordinates = np.array([station[2:5] for station in coldest_stations])

# Calculating the distance matrix for the 5 coldest stations
distance_matrix_coldest = distance_matrix(coldest_stations_coordinates, coldest_stations_coordinates)

distance_matrix_coldest"""
