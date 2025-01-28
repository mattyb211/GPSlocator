# **GeoLocation Matcher**

## **Overview**
The **GeoLocation Matcher** is a Python tool that finds the closest point in one array of geolocations to each point in another array using the **Haversine formula**. It calculates distances in kilometers with spherical accuracy.

Additionally, this repository contains a **GitHub Action** to greet first-time contributors when they open an issue or pull request.

---

## **Features and Updates**

1. **Multiple Input Formats**  
   - **Decimal Degrees** (e.g., `42.3601, -71.0589`)  
   - **Degrees, Minutes, Seconds (DMS)** (e.g., `40 44 54.36 73 59 8.36`)

2. **Haversine Distance Calculation**  
   - Computes the great-circle distance between two lat/long points on Earth.

3. **GitHub Action**  
   - An automated workflow (`.github/workflows`) that **greets new contributors** on their first pull request or issue.

---

## **Installation and Usage**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/YourUsername/GeoLocation-Matcher.git
   cd GeoLocation-Matcher
