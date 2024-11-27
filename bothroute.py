import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk, messagebox

# Step 1: Create a graph object
metro_graph = nx.Graph()

# Define metro stations for both routes
red_line_stations = [
    "Thaltej Gam", "Thaltej", "Doordarshan Kendra", "Gurukul Road", "Gujarat University",
    "Commerce Six Road", "SP Stadium", "Old High Court (interchange station)", "Shahpur",
    "Gheekanta", "Kalupur Railway Station", "Kankaria East", "Apparel Park", "Amraiwadi",
    "Rabari Colony", "Vastral", "Nirant Cross Road", "Vastral Gam"
]
blue_line_stations = [
    "APMC", "Jivraj Park", "Rajiv Nagar", "Shreyas", "Paldi",
    "Gandhi Gram", "Old High Court (interchange station)", "Usmanpura",
    "Vadaj", "Sabarmati Railway Station", "Sabarmati", "Motera"
]


# Add both routes to the graph
metro_graph.add_nodes_from(red_line_stations + blue_line_stations)
# Step 3: Define edges (station-to-station connections with distance and time)
edges = [
    # Red Line edges
    ("Thaltej Gam", "Thaltej", {'distance': 1.2, 'time': 2}),
    ("Thaltej", "Doordarshan Kendra", {'distance': 1.2, 'time': 3}),
    ("Doordarshan Kendra", "Gurukul Road", {'distance': 1.2, 'time': 2}),
    ("Gurukul Road", "Gujarat University", {'distance': 1.8, 'time': 3}),
    ("Gujarat University", "Commerce Six Road", {'distance': 1.1, 'time': 4}),
    ("Commerce Six Road", "SP Stadium", {'distance': 1.3, 'time': 5}),
    ("SP Stadium", "Old High Court (interchange station)", {'distance': 1.1, 'time': 3}),
    ("Old High Court (interchange station)", "Shahpur", {'distance': 1.1, 'time': 3}),
    ("Shahpur", "Gheekanta", {'distance': 2, 'time': 4}),
    ("Gheekanta", "Kalupur Railway Station", {'distance': 2.2, 'time': 3}),
    ("Kalupur Railway Station", "Kankaria East", {'distance': 3.5, 'time': 4}),
    ("Kankaria East", "Apparel Park", {'distance': 2.2, 'time': 5}),
    ("Apparel Park", "Amraiwadi", {'distance': 0.8, 'time': 3}),
    ("Amraiwadi", "Rabari Colony", {'distance': 1.5, 'time': 4}),
    ("Rabari Colony", "Vastral", {'distance': 2.5, 'time': 3}),
    ("Vastral", "Nirant Cross Road", {'distance': 7.5, 'time': 2}),
    ("Nirant Cross Road", "Vastral Gam", {'distance': 1.2, 'time': 2}),
    
    # Blue Line edges
    ("APMC", "Jivraj Park", {'distance': 1.5, 'time': 3}),
    ("Jivraj Park", "Rajiv Nagar", {'distance': 1.2, 'time': 2}),
    ("Rajiv Nagar", "Shreyas", {'distance': 1.3, 'time': 2}),
    ("Shreyas", "Paldi", {'distance': 1.5, 'time': 3}),
    ("Paldi", "Gandhi Gram", {'distance': 1.4, 'time': 2}),
    ("Gandhi Gram", "Old High Court (interchange station)", {'distance': 1.1, 'time': 3}),
    ("Old High Court (interchange station)", "Usmanpura", {'distance': 1.0, 'time': 2}),
    ("Usmanpura", "Vadaj", {'distance': 1.7, 'time': 3}),
    ("Vadaj", "Sabarmati Railway Station", {'distance': 2.1, 'time': 4}),
    ("Sabarmati Railway Station", "Sabarmati", {'distance': 1.8, 'time': 3}),
    ("Sabarmati", "Motera", {'distance': 1.6, 'time': 3}),
]


# Add edges to the graph
metro_graph.add_edges_from(edges)


# Function to calculate the shortest path based on 'time'
def shortest_time_path(graph, start_station, end_station):

    try:
        return nx.dijkstra_path(graph, source=start_station, target=end_station, weight='time')
    except nx.NetworkXNoPath:
        messagebox.showinfo("No Path", f"No path found between {start_station} and {end_station}.")
        return []
# Function to get total travel time of the shortest path
def total_travel_time(graph, path):
    total_time = 0
    for i in range(len(path) - 1):
        total_time += graph[path[i]][path[i + 1]]['time']
    return total_time
# Function to calculate total distance of the shortest path
def total_distance(graph, path):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += graph[path[i]][path[i + 1]]['distance']
    return total_distance

# Function to calculate and visualize the route
def calculate_route():
    start_station = start_station_var.get()
    end_station = end_station_var.get()

    if start_station == end_station:
        messagebox.showinfo("Error", "Start and End stations cannot be the same!")
        return

    shortest_path = shortest_time_path(metro_graph, start_station, end_station)

    if shortest_path:
        total_time = total_travel_time(metro_graph, shortest_path)
        total_distance_value = total_distance(metro_graph, shortest_path)

        result = f"Shortest path: {' -> '.join(shortest_path)}\n"
        result += f"Total travel time: {total_time} minutes\n"
        result += f"Total distance: {total_distance_value} km\n"
        result_label.config(text=result)
        visualize_path(shortest_path, total_time, total_distance_value)
    else:
        messagebox.showinfo("No Path", "No path found between the selected stations.")


# Function to visualize the path using matplotlib
def visualize_path(path, total_time, total_distance):
    plt.clf()  # Clear previous plot
    pos = nx.spring_layout(metro_graph, seed=42)  # Fixed positions for consistency

    
    # Draw all nodes
    nx.draw(metro_graph, pos, with_labels=True, node_color='lightgrey', node_size=2000, font_size=10)

    
    
    # Highlight the shortest path
    subgraph = metro_graph.subgraph(path)
    nx.draw(subgraph, pos, with_labels=True, node_color='lightblue', node_size=2500, font_weight='bold')

    
    # Display edge labels
    edge_labels = {(u, v): f"{d['time']} min, {d['distance']} km" for u, v, d in subgraph.edges(data=True)}
    nx.draw_networkx_edge_labels(subgraph, pos, edge_labels=edge_labels)

    
    plt.title(f"Shortest Path from {path[0]} to {path[-1]} (Time: {total_time} min, Distance: {total_distance} km)")
    plt.tight_layout()  # Adjust layout
    canvas.draw()  # Render the plot in the Tkinter window

# Tkinter window setup
root = tk.Tk()
root.title("Ahmedabad Metro Route Finder")
root.geometry("800x600")

# Frame for input selection
input_frame = ttk.Frame(root)
input_frame.pack(pady=20)

# Variables for stations
start_station_var = tk.StringVar()
end_station_var = tk.StringVar()

# Start station dropdown
ttk.Label(input_frame, text="Select Start Station:").grid(row=0, column=0, padx=10, pady=10)
start_station_menu = ttk.Combobox(input_frame, textvariable=start_station_var, values=red_line_stations + blue_line_stations)
start_station_menu.grid(row=0, column=1, padx=10, pady=10)

# End station dropdown
ttk.Label(input_frame, text="Select End Station:").grid(row=1, column=0, padx=10, pady=10)
end_station_menu = ttk.Combobox(input_frame, textvariable=end_station_var, values=red_line_stations + blue_line_stations)
end_station_menu.grid(row=1, column=1, padx=10, pady=10)

# Button to calculate the route
calculate_button = ttk.Button(input_frame, text="Calculate Route", command=calculate_route)
calculate_button.grid(row=2, columnspan=2, pady=20)

# Label for displaying results
result_label = ttk.Label(root, text="", wraplength=400, justify="left")
result_label.pack(pady=20)

# Matplotlib figure and canvas
fig, ax = plt.subplots(figsize=(8, 4))
canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Start the Tkinter event loop
root.mainloop()
