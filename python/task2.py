import random 

distance = [ 

    [0, 8, 6, 7, 5],   
    [8, 0, 4, 3, 6],   
    [6, 4, 0, 5, 7],   
    [7, 3, 5, 0, 4],    
    [5, 6, 7, 4, 0]     
] 
locations = [ 
    "Chennai", 
    "Madurai", 
    "Bengaluru", 
    "Coimbatore", 
    "Tiruchirappalli" 
] 
def calculate_distance(route): 
    total = 0 
    for i in range(len(route)-1): 
        total += distance[route[i]][route[i+1]] 
    return total 
def generate_neighbors(route): 
    neighbors = [] 
    for i in range(1, len(route)-2): 
        for j in range(i+1, len(route)-1): 
            new_route = route.copy() 
            new_route[i], new_route[j] = new_route[j], new_route[i] 
            neighbors.append(new_route)
    return neighbors 
def hill_climbing(route): 
    current_route = route 
    current_distance = calculate_distance(current_route) 
    while True: 
        best_route = current_route 
        best_distance = current_distance 
        for neighbor in generate_neighbors(current_route): 
            neighbor_distance = calculate_distance(neighbor) 
            if neighbor_distance < best_distance: 
                best_route = neighbor 
                best_distance = neighbor_distance 
        if best_distance == current_distance: 
            break
        current_route = best_route 
        current_distance = best_distance
    return current_route, current_distance
initial_route = [0, 1, 2, 3, 4, 0] 
print("Initial Route:") 
print(" -> ".join(locations[i] for i in initial_route)) 
print("Initial Distance:", calculate_distance(initial_route)) 
optimized_route, optimized_distance = hill_climbing(initial_route) 
print("\nOptimized Route:") 
print(" -> ".join(locations[i] for i in optimized_route)) 
print("Optimized Distance:", optimized_distance)
