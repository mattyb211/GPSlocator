# **GeoLocation Matcher**

## **Overview**
The **GeoLocation Matcher** is a Python tool that finds the closest point in one array of geolocations to each point in another array using the **Haversine formula**. It calculates distances in kilometers with spherical accuracy.

---

## **How It Works**
1. Enter the number of points for each array.
2. Input geolocation points in `latitude,longitude` format.
3. The program calculates and displays:
   - Closest matches for all points in the first array to points in the second array.
   - Distances in kilometers.

---

## **Example**
**Input:**
- **First Array:**  
  - Location A: `42.3601,-71.0589` (Boston)  
  - Location B: `40.7128,-74.0060` (New York)  
- **Second Array:**  
  - Location A: `34.0522,-118.2437` (Los Angeles)  
  - Location B: `37.7749,-122.4194` (San Francisco)

**Output:**
 - Location A (42.3601, -71.0589) is closest to (34.0522, -118.2437) with a distance of 4163.00 km. 
 - Location B (40.7128, -74.0060) is closest to (34.0522, -118.2437) with a distance of 3936.00 km.
