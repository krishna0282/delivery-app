import streamlit as st
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import random

geolocator = Nominatim(user_agent="delivery_app")

st.title("🚚 Smart Delivery Optimization App")

# INPUT
source = st.text_input("Enter Source (city,state,country)")
destination = st.text_input("Enter Destination (city,state,country)")
vehicle = st.selectbox("Select Vehicle", ["Bike", "Car", "Truck"])

def get_coord(place):
    loc = geolocator.geocode(place)
    return (loc.latitude, loc.longitude) if loc else None

if st.button("Optimize Route"):

    source_coord = get_coord(source)
    dest_coord = get_coord(destination)

    if not source_coord or not dest_coord:
        st.error("Invalid location")
    else:
        # Distance calculation
        straight = geodesic(source_coord, dest_coord).km
        distance = straight * random.uniform(1.1, 1.2)

        # Non-optimized
        normal = distance * random.uniform(1.2, 1.4)

        # Fuel
        if vehicle == "Bike":
            fuel = distance * 0.03
        elif vehicle == "Car":
            fuel = distance * 0.08
        else:
            fuel = distance * 0.2

        carbon = fuel * 2.3

        # Traffic
        traffic = random.choice(["Low", "Moderate", "High"])

        st.subheader("📊 Results")
        st.write(f"Distance: {distance:.2f} km")
        st.write(f"Fuel Used: {fuel:.2f} liters")
        st.write(f"Carbon Emission: {carbon:.2f} kg CO2")
        st.write(f"Traffic: {traffic}")

        st.subheader("🧭 Route Explanation")

        st.write(f"Start from {source}")

        if traffic == "High":
            st.write("Traffic is high → take alternate roads")
        elif traffic == "Moderate":
            st.write("Traffic is moderate → slight delay")
        else:
            st.write("Traffic is low → smooth travel")

        st.write(f"Reach {destination}")

        st.subheader("❌ Without Optimization")
        st.write(f"Distance: {normal:.2f} km")
        st.write(f"Fuel: {normal*0.08:.2f} liters")
        st.write(f"CO2: {(normal*0.08*2.3):.2f} kg")
