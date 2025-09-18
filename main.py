import networkx as nx
import matplotlib.pyplot as plt

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
]

# Add edges to the graph
metro_graph.add_edges_from(edges)


# Function to calculate the shortest path based on 'time'
def shortest_time_path(graph, start_station, end_station):
    try:
        return nx.dijkstra_path(graph, source=start_station, target=end_station, weight='time')
    except nx.NetworkXNoPath:
        print(f"No path found between {start_station} and {end_station}.")
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

# Real-time updates using a loop
while True:
    
    # Step 4: Get user input for start and end stations
    start_station = input("Enter the pickup station (or 'exit' to quit): ")
    if start_station.lower() == 'exit':
        break
    end_station = input("Enter the drop station: ")

    # Input validation: check if stations exist in the graph
    if start_station not in metro_graph or end_station not in metro_graph:
        print("Error: One or both of the stations are not in the network. Please try again.")
        continue
        
    # Calculate the shortest path
    shortest_path = shortest_time_path(metro_graph, start_station, end_station)
    if shortest_path:
        print(f"The shortest path from {start_station} to {end_station} is: {shortest_path}")  
        
        # Get total time and distance for the calculated shortest path
        total_time = total_travel_time(metro_graph, shortest_path)
        total_distance_value = total_distance(metro_graph, shortest_path)
        print(f"Total travel time from {start_station} to {end_station} is: {total_time} minutes")
        print(f"Total distance from {start_station} to {end_station} is: {total_distance_value} km")
        
        # Step 5: Visualize only the shortest path on the graph
        subgraph = metro_graph.subgraph(shortest_path)  # Extract subgraph for the shortest path
        pos = nx.spring_layout(metro_graph, seed=42)  # Positions for all nodes (fixed seed for consistent layout)
        
        # Clear previous plot
        plt.clf()       
        
        # Draw all nodes but highlight only those in the shortest path
        nx.draw(metro_graph, pos, with_labels=True, node_color='lightgrey', node_size=2000, font_size=10)
        nx.draw(subgraph, pos, with_labels=True, node_color='lightblue', node_size=2500, font_size=10, font_weight='bold')

        # Highlight edges in the shortest path
        edge_labels_time = nx.get_edge_attributes(subgraph, 'time')
        nx.draw_networkx_edge_labels(subgraph, pos, edge_labels=edge_labels_time)
        
        # Display both time and distance on edges in the subgraph
        edge_labels = {(u, v): f"{d['time']} min, {d['distance']} km" for u, v, d in subgraph.edges(data=True)}
        nx.draw_networkx_edge_labels(subgraph, pos, edge_labels=edge_labels)

        plt.title(f"Shortest Path from {start_station} to {end_station} (Time in Minutes)")
        plt.pause(1)  # Pause for 1 second to update the plot

# Close the plot when exiting the loop
plt.close()

#user can get your destination place 
