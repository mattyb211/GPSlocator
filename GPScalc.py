import math

def haversine_distance(lat1, lon1, lat2, lon2):
    R = 6371  # Earth's radius in km

    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    dlat = lat2 - lat1
    dlon = lon2 - lon1
    
    # Haversine formula
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    return distance

def find_closest_points(array1, array2):
    closest_points = []
    for index1, (lat1, lon1) in enumerate(array1):
        min_distance = float('inf')
        closest_point = None
        for lat2, lon2 in array2:
            distance = haversine_distance(lat1, lon1, lat2, lon2)
            if distance < min_distance:
                min_distance = distance
                closest_point = (lat2, lon2)
        closest_points.append((f"Location {chr(65 + index1)}", (lat1, lon1), closest_point, min_distance))
    return closest_points

def input_array(array_name):
    
    array = []
    num_points = int(input(f"How many points will you enter for {array_name}? "))
    for index in range(num_points):
        while True:
            point = input(f"Enter GPS point {index + 1} as 'latitude,longitude' for Location {chr(65 + index)}: ")
            try:
                lat, lon = map(float, point.split(","))
                array.append((lat, lon))
                break
            except ValueError:
                print("Invalid input. Please enter in the format 'latitude,longitude'.")
    return array

if __name__ == "__main__":
    print("Welcome to the Geo Location Matching Tool!")

    array1 = input_array("the first array (points to match)")
    array2 = input_array("the second array (reference points)")
    
    if not array1 or not array2:
        print("Both arrays must have at least one point. Exiting.")
    else:
        # Perform the matching
        results = find_closest_points(array1, array2)
        
        print("\nMatching Results:")
        for result in results:
            label, (lat1, lon1), (closest_lat, closest_lon), distance = result
            print(f"{label} ({lat1}, {lon1}) is closest to ({closest_lat}, {closest_lon}) with a distance of {distance:.2f} km.")