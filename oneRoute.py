import networkx as nx
import matplotlib.pyplot as plt
import random
import time
import datetime

# Step 1: Create a graph object
metro_graph = nx.Graph() 

# Step 2: Add metro stations as nodes
stations = [
    "Thaltej Gam", "Thaltej", "Doordarshan Kendra", "Gurukul Road", "Gujarat University", 
    "Commerce Six Road", "SP Stadium", "Old High Court (interchange station)", "Shahpur", 
    "Gheekanta", "Kalupur Railway Station", "Kankaria East", "Apparel Park", "Amraiwadi",  
    "Rabari Colony", "Vastral", "Nirant Cross Road", "Vastral Gam"
]
metro_graph.add_nodes_from(stations)

# Step 3: Define edges (station-to-station connections with distance and time)
edges = [
    ("Thaltej Gam", "Thaltej", {'distance': 1.2, 'time': 2}),
    ("Thaltej", "Doordarshan Kendra", {'distance': 2, 'time': 3}),
    ("Doordarshan Kendra", "Gurukul Road", {'distance': 1.5, 'time': 2}),
    ("Gurukul Road", "Gujarat University", {'distance': 1.8, 'time': 3}),
    ("Gujarat University", "Commerce Six Road", {'distance': 2, 'time': 4}),
    ("Commerce Six Road", "SP Stadium", {'distance': 2.5, 'time': 5}),
    ("SP Stadium", "Old High Court (interchange station)", {'distance': 1.8, 'time': 3}),
    ("Old High Court (interchange station)", "Shahpur", {'distance': 1.6, 'time': 3}),
    ("Shahpur", "Gheekanta", {'distance': 2, 'time': 4}),
    ("Gheekanta", "Kalupur Railway Station", {'distance': 1.8, 'time': 3}),
    ("Kalupur Railway Station", "Kankaria East", {'distance': 2.2, 'time': 4}),
    ("Kankaria East", "Apparel Park", {'distance': 2.5, 'time': 5}),
    ("Apparel Park", "Amraiwadi", {'distance': 1.8, 'time': 3}),
    ("Amraiwadi", "Rabari Colony", {'distance': 2.1, 'time': 4}),
    ("Rabari Colony", "Vastral", {'distance': 1.6, 'time': 3}),
    ("Vastral", "Nirant Cross Road", {'distance': 1.5, 'time': 2}),
    ("Nirant Cross Road", "Vastral Gam", {'distance': 1.2, 'time': 2}),
]

# Add edges to the graph
metro_graph.add_edges_from(edges)

# Function to simulate real-time updates
def update_travel_times(graph):
    for u, v, data in graph.edges(data=True):
        # Randomly adjust travel time to simulate real-time updates
        adjustment = random.randint(-1, 2)  # Simulate minor changes in time
        data['time'] = max(1, data['time'] + adjustment)  # Ensure time doesn't go below 1

# Step 4: Get user input for start and end stations
start_station = input("Enter the pickup station: ")
end_station = input("Enter the drop station: ")

# Step 5: Function to calculate shortest path based on 'time'
def shortest_time_path(graph, start_station, end_station):
    try:
        return nx.dijkstra_path(graph, source=start_station, target=end_station, weight='time')
    except nx.NetworkXNoPath:
        print(f"No path found between {start_station} and {end_station}.")
        return []

# Calculate the shortest path
shortest_path = shortest_time_path(metro_graph, start_station, end_station)

# If a valid path is found, proceed
if shortest_path:
    print(f"The shortest path from {start_station} to {end_station} is: {shortest_path}")

    # Step 6: Function to get total travel time of the shortest path
    def total_travel_time(graph, path):
        total_time = 0
        for i in range(len(path) - 1):
            total_time += graph[path[i]][path[i + 1]]['time']
        return total_time

    # New function to calculate total distance of the shortest path
    def total_distance(graph, path):
        total_distance = 0
        for i in range(len(path) - 1):
            total_distance += graph[path[i]][path[i + 1]]['distance']
        return total_distance

    # Get total time and distance for the calculated shortest path
    total_time = total_travel_time(metro_graph, shortest_path)
    total_distance_value = total_distance(metro_graph, shortest_path)
    
    print(f"Total travel time from {start_station} to {end_station} is: {total_time} minutes")
    print(f"Total distance from {start_station} to {end_station} is: {total_distance_value} km")

    # Simulate real-time updates for a few iterations with India timing
    for _ in range(3):  # Simulate three updates
        current_time_ist = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Get current time in IST
        print(f"\nUpdating travel times... (Current IST Time: {current_time_ist})")
        update_travel_times(metro_graph)
        
        # Recalculate the shortest path with updated times
        shortest_path = shortest_time_path(metro_graph, start_station, end_station)
        
        if shortest_path:
            total_time = total_travel_time(metro_graph, shortest_path)
            total_distance_value = total_distance(metro_graph, shortest_path)
            print(f"Updated total travel time from {start_station} to {end_station} is: {total_time} minutes")
            print(f"Updated total distance from {start_station} to {end_station} is: {total_distance_value} km")
        
        time.sleep(1)  # Simulate a delay between updates

    # Step 7: Visualize only the shortest path on the graph
    subgraph = metro_graph.subgraph(shortest_path)  # Extract subgraph for the shortest path

    pos = nx.spring_layout(metro_graph)  # Positions for all

#enter your pickup and drop station end show output
