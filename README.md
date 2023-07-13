# A* algorithm


Problem description: Given a landscape of size n x m with some random obstacles on the
way, find the shortest path of the robot from a starting point (S) to a final destination (F) using A*
algorithm.

To execute the code just type on the terminal: python Astar.py

This code implements the A* algorithm to find the shortest path between a start and a goal point on a 2D landscape grid. It uses a priority queue to store nodes, where the priority is determined by the cost of the path plus a heuristic function. The algorithm expands nodes until the goal is reached or the queue becomes empty. The `get_neighbors` function retrieves the valid neighboring nodes for a given node. The example usage demonstrates finding the shortest path on a sample landscape grid.