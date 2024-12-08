# Ahmedabad Metro Route Finder

This project is a real-time Ahmedabad Metro route finder using **NetworkX** and **Matplotlib** in Python. It calculates the shortest path between metro stations based on travel time and visualizes the route on a graph.

## Features

- **Shortest Path Calculation:** Finds the shortest path between any two metro stations based on travel time.
- **Total Time and Distance:** Calculates both the total travel time and distance for the selected route.
- **Real-time Interaction:** Prompts the user to input pickup and drop stations in real-time.
- **Visualization:** The metro network and the calculated shortest path are visualized using Matplotlib.

## How It Works

### Graph Structure

- **Nodes:** Represent metro stations.
- **Edges:** Represent direct connections between metro stations, with associated travel time (in minutes) and distance (in kilometers).

### Shortest Path Algorithm

The project uses Dijkstra's algorithm to calculate the shortest path between two stations, optimizing for minimum travel time.

### Example Metro Stations

- **Thaltej Gam**
- **Gujarat University**
- **Kalupur Railway Station**
- **Vastral Gam**

... and others.

## Requirements

Ensure you have the following Python libraries installed:

- `networkx`
- `matplotlib`

You can install these dependencies using:

```bash
pip install networkx matplotlib
