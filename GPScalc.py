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

def input_array(array_name, format_choice):
    
    array = []
    num_points = int(input(f"How many points will you enter for {array_name}? "))

    for i in range(num_points):
        if format_choice == "1":
            # Decimal format: "lat, lon"
            point_str = input(
                f"Enter GPS point {i+1} in decimal format (lat, lon) for Location {chr(65 + i)}: "
            )
            lat_str, lon_str = point_str.split(',')
            lat = float(lat_str.strip())
            lon = float(lon_str.strip())
            array.append((lat, lon))

        else:
            dms_str = input(
                f"Enter GPS point {i+1} in DMS format (deg min sec deg min sec)\n"
                f"for Location {chr(65 + i)} (example: 40 44 54.36 73 59 8.36): "
            )
            deg_lat, min_lat, sec_lat, deg_lon, min_lon, sec_lon = map(float, dms_str.split())

            # Convert lat
            decimal_lat = deg_lat + (min_lat / 60.0) + (sec_lat / 3600.0)
            # Convert lon
            decimal_lon = deg_lon + (min_lon / 60.0) + (sec_lon / 3600.0)

            array.append((decimal_lat, decimal_lon))
    
    return array

if __name__ == "__main__":
    print("Welcome to the Geo Location Matching Tool!")
    print("Please select the coordinate format you will be using:")
    print("  1) Decimal (e.g., 42.3601, -71.0589)")
    print("  2) DMS (e.g., 40 44 54.36 73 59 8.36)")

    format_choice = input("Enter 1 or 2: ").strip()
    while format_choice not in ["1", "2"]:
        format_choice = input("Invalid choice. Please enter '1' or '2': ").strip()

    # Get the user arrays
    array1 = input_array("the first array (points to match)", format_choice)
    array2 = input_array("the second array (reference points)", format_choice)
    
    # If either array is empty, exit
    if not array1 or not array2:
        print("Both arrays must have at least one point. Exiting.")
    else:
        # Find the closest points
        results = find_closest_points(array1, array2)

        print("\nMatching Results:")
        for label, (lat1, lon1), (closest_lat, closest_lon), distance in results:
            print(
                f"{label} ({lat1:.6f}, {lon1:.6f}) is closest to "
                f"({closest_lat:.6f}, {closest_lon:.6f}) with a distance of {distance:.2f} km."
            )