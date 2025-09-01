import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from collections import deque

# Grid parameters updated to include destination at (5,5)
W, H = 6, 6
obstacles = {(1, 1), (2, 2), (3, 1),(5,4)}
tasks = {(0, 2), (2, 3), (3, 0),(4,2)}
destination = (5, 5)
agent = (0, 0)

def valid(x, y):
    return 0 <= x < W and 0 <= y < H and (x, y) not in obstacles

def bfs(start, goals):
    """Find shortest path from start to any of the goals (set).
    Returns path (list of tuples) or None if no path."""
    queue = deque([start])
    came_from = {start: None}

    while queue:
        current = queue.popleft()
        if current in goals:
            # Reconstruct path
            path = []
            while current:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path
        x, y = current
        neighbors = [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]
        for nx, ny in neighbors:
            if valid(nx, ny) and (nx, ny) not in came_from:
                came_from[(nx, ny)] = current
                queue.append((nx, ny))
    return None

def draw_grid(agent, tasks, obstacles, destination, ax):
    ax.clear()
    ax.set_xlim(0, W)
    ax.set_ylim(0, H)
    ax.set_xticks(np.arange(0, W+1, 1))
    ax.set_yticks(np.arange(0, H+1, 1))
    ax.grid(True)
    ax.set_aspect('equal')
    ax.invert_yaxis()

    # Draw obstacles
    for (x, y) in obstacles:
        rect = patches.Rectangle((x, y), 1, 1, facecolor='black')
        ax.add_patch(rect)

    # Draw tasks
    for (x, y) in tasks:
        circle = patches.Circle((x + 0.5, y + 0.5), 0.3, facecolor='green')
        ax.add_patch(circle)

    # Draw destination
    dx, dy = destination
    dest_rect = patches.Rectangle((dx, dy), 1, 1, facecolor='blue', alpha=0.3)
    ax.add_patch(dest_rect)
    ax.text(dx+0.5, dy+0.5, 'Dest', color='blue', ha='center', va='center', fontsize=8, weight='bold')

    # Draw agent
    ax.plot(agent[0] + 0.5, agent[1] + 0.5, marker='o', markersize=20, color='red', label='Agent')

    ax.legend(loc='upper right')
    ax.set_title('Agent Task Collection')

# Set up figure and axis
fig, ax = plt.subplots(figsize=(6, 6))

# Simulation state variables
step = 0
max_steps = 100
current_agent = agent
current_tasks = set(tasks)

def on_click(event):
    global step, current_agent, current_tasks

    if step >= max_steps:
        print("Reached max steps without completing all tasks and destination.")
        return

    print(f"Step {step}: Agent at {current_agent}, Tasks left: {current_tasks}")

    if current_agent in current_tasks:
        print(f"Picked up task at {current_agent}!")
        current_tasks.remove(current_agent)
        if not current_tasks:
            print("All tasks collected! Now moving to destination.")

    # Determine goals: tasks if any left, else destination
    goals = current_tasks if current_tasks else {destination}

    # Find shortest path to nearest goal
    path = bfs(current_agent, goals)

    if path is None or len(path) < 2:
        print("No path to goal found or agent already at goal.")
        if current_agent == destination:
            print("Agent reached the destination! Task complete.")
        fig.canvas.mpl_disconnect(cid)
        return

    # Move one step along path
    new_agent = path[1]

    if new_agent == current_agent:
        print("Agent stuck, no move possible!")
        fig.canvas.mpl_disconnect(cid)
        return

    current_agent = new_agent
    step += 1

    draw_grid(current_agent, current_tasks, obstacles, destination, ax)
    fig.canvas.draw()

# Initial draw
draw_grid(current_agent, current_tasks, obstacles, destination, ax)
fig.canvas.draw()

# Connect click event to on_click function
cid = fig.canvas.mpl_connect('button_press_event', on_click)

plt.show()
