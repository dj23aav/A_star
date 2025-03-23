
# A* Pathfinding Visualization

This project implements the A* pathfinding algorithm to find the shortest path on a grid. The map is represented by a binary image, where obstacles are marked, and the agent needs to navigate from a start position to a goal position. The algorithm's process is visualized in real-time using Pygame.

## Features
- **A* Pathfinding Algorithm**: Implements the A* algorithm to calculate the shortest path while avoiding obstacles.
- **Grid-based Visualization**: Visualizes the grid, agent's movement, goal position, obstacles, and visited nodes.
- **Image-based Obstacle Map**: Converts a binary image into a grid to represent obstacles for the pathfinding agent.
- **Real-time Pygame Visualization**: Displays the A* algorithm's execution in real-time.

## Prerequisites

Ensure that Python 3.x is installed. You can download it from [Python.org](https://www.python.org/downloads/).

### Required Libraries:
To run this project, the following Python libraries are required:
- **Pygame**
- **OpenCV**
- **NumPy**

You can install them using pip:

```bash
pip install pygame opencv-python numpy
```

## How to Use

### 1. Clone the Repository

Clone the repository to your local machine using the following command:

```bash
git clone https://github.com/dj23aav/A_star.git
```

### 2. Place Your Map Image

Ensure that you have a binary image (e.g., `map2.png`) representing the obstacles. The agent will start at the top-left corner, and the goal is located at the bottom-right corner. Each pixel in the image will represent a grid cell.

### 3. Modify Image Path (Optional)

If your map image is located elsewhere, change the `image_path` variable in the code to point to your image file:

```python
image_path = "map2.png"  # Replace with your image path
```

### 4. Run the Script

After setting up the necessary image and libraries, run the script `A_star.py`:

```bash
python A_star.py
```

### 5. Visualization

The visualization will show the A* algorithm in action. The following color scheme is used:

- **Red**: Start Position (Agent)
- **Green**: Goal Position
- **Black**: Obstacles
- **Teal**: Visited Cells
- **Red Path**: The path found by the A* algorithm

### Example Output

![Example Output](screenshot.png)  <!-- Add a screenshot of the output here -->

## Code Description

- **A_star.py**: Contains the implementation of the A* algorithm, grid generation, image-to-binary conversion, and real-time visualization using Pygame.
  - The script starts by converting the input image into a binary grid, where obstacles are represented by 0 (black pixels).
  - The A* algorithm is applied to find the shortest path from the start (top-left) to the goal (bottom-right) while avoiding obstacles.
  - The grid and pathfinding process are visualized using Pygame, with real-time updates showing visited nodes and the final path.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

