import folium

# Create a map centered at a location (latitude, longitude)
m = folium.Map(location=[12.9716, 77.5946], zoom_start=12)  # Bangalore 💖

# Add a marker
folium.Marker(
    location=[12.9716, 77.5946],
    popup="Hello, This is Bangalore!",
    tooltip="Click me",
    icon=folium.Icon(color="pink", icon="heart")
).add_to(m)

# Add another marker for fun
folium.Marker(
    location=[12.2958, 76.6394],  # Mysore
    popup="Royal Mysore Palace ✨",
    tooltip="Click me too",
    icon=folium.Icon(color="purple", icon="star")
).add_to(m)

# Save map as HTML
m.save("mia_map.html")
print("Map saved as mia_map.html — open it in your browser 🌍")
