import streamlit as st
import pandas as pd

# Page settings
st.set_page_config(
    page_title="ChristEats",
    page_icon="🍽️",
    layout="wide"
)

# Header
st.title("🍽️ CHRIST (Deemed to be University) Delhi NCR")
st.subheader("Campus Food Outlet Proximity Finder")

st.markdown("---")

# Sidebar
st.sidebar.title("📍 Navigation")
st.sidebar.info(
"""
This app helps students quickly find the **nearest food outlets** on campus.

Select your location and discover where to eat!
"""
)

st.sidebar.markdown("---")
st.sidebar.write("Developed for Graph Theory CIA 3")

# Campus distance data
campus_map = {
    "Main Gate": {"Nescafe": 50, "Taste of Dilli": 120, "Punjabi Bites": 140, "Rolls Lane": 160},
    "Block A": {"Nescafe": 40, "Taste of Dilli": 100, "Punjabi Bites": 120, "Rolls Lane": 140},
    "Block B": {"Nescafe": 25, "Taste of Dilli": 85, "Punjabi Bites": 85, "Rolls Lane": 85},
    "Rooftop": {"Nescafe": 70, "Taste of Dilli": 30, "Punjabi Bites": 50, "Rolls Lane": 60},
    "Freshiteria": {"Nescafe": 20, "Taste of Dilli": 60, "Punjabi Bites": 80, "Rolls Lane": 95}
}

# Layout columns
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📍 Select Your Current Location")
    location = st.selectbox(
        "Choose location",
        list(campus_map.keys())
    )

with col2:
    st.markdown("### ⚙️ Filter Options")
    max_distance = st.slider(
        "Maximum distance (meters)",
        0, 200, 150
    )

st.markdown("---")

# Button to calculate
if st.button("🔎 Find Nearest Food Outlets"):

    outlets = campus_map[location]

    # Filter by distance
    filtered = {k: v for k, v in outlets.items() if v <= max_distance}

    if filtered:

        sorted_outlets = sorted(filtered.items(), key=lambda x: x[1])

        data = []
        for rank, (name, distance) in enumerate(sorted_outlets, start=1):
            data.append([rank, name, distance])

        df = pd.DataFrame(data, columns=["Rank", "Outlet", "Distance (m)"])

        st.success(f"Showing results near **{location}**")

        st.markdown("### 🏆 Closest Food Outlet")
        st.info(f"**{sorted_outlets[0][0]}** is the nearest outlet ({sorted_outlets[0][1]} meters away)")

        st.markdown("### 📊 Ranked Food Outlets")
        st.dataframe(df, use_container_width=True)

    else:
        st.warning("No outlets found within this distance.")

st.markdown("---")

# Campus information section
st.markdown("### 🏫 About Campus Food")

st.write(
"""
Christ University Delhi NCR campus offers several food outlets for students including:

• **Nescafe** – Coffee, snacks, sandwiches  
• **Taste of Dilli** – North Indian meals  
• **Punjabi Bites** – Fast food and rolls  
• **Rolls Lane** – Wraps and quick bites  

This app demonstrates how **graph theory shortest path concepts** can be applied
to find the nearest food outlet based on distance.
"""
)

st.markdown("---")

# Footer
st.caption("ChristEats Campus Finder • Graph Theory CIA 3 Project")
