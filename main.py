from n_queens import solve_n_queens
from graph_coloring import graph_coloring
from utils import display_results

num_rooms = int(input("Enter the room number: "))
rooms = [f"Room{i+1}" for i in range(num_rooms)]

graph = [[1 if i != j else 0 for j in range(num_rooms)] for i in range(num_rooms)]

time_slots = graph_coloring(graph)

switch_positions = solve_n_queens(num_rooms)

display_results(rooms, time_slots, switch_positions)