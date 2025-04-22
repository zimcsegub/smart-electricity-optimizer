
from tabulate import tabulate

def display_results(rooms, time_slots, switch_positions):
    data = []
    for i in range(len(rooms)):
        data.append([rooms[i], time_slots[i] + 1, f"Slot {switch_positions[i]}"])
    print(tabulate(data, headers=["Room", "Time Slot", "Switch Position"], tablefmt="grid"))