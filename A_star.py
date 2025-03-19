import pygame
import cv2
import numpy as np
import heapq
import time


GRID_SIZE = 20  # Set to match GridWorld default
CELL_SIZE = 50
WIDTH, HEIGHT = GRID_SIZE * CELL_SIZE, GRID_SIZE * CELL_SIZE
WHITE, BLACK, RED, GREY, LIGHT_GREY, GREEN, TEAL = (
    (255, 255, 255), (0, 0, 0), (255, 0, 0),
    (128, 128, 128), (200, 200, 200), (0, 255, 0), (0, 128, 128)
)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("A* Pathfinding")

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0  # Cost from start to current node
        self.h = 0  # Heuristic (Manhattan distance to goal)
        self.f = 0  # Total cost (g + h)

    def __lt__(self, other):
        return self.f < other.f  # Compare nodes based on f-value



class GridWorld:
    def __init__(self, size=20):
        self.size = size
        self.agent_pos = (0, 0)
        self.goal_pos = (size - 1, size - 1)
        self.obstacles = []
        self.visited_cells = set()
        self.path = []
        self.visited_cells.add(self.agent_pos)

        self.font = pygame.font.Font(None, 24)  # Font for text rendering

    def a_star(self):
        start_node = Node(self.agent_pos)
        goal_node = Node(self.goal_pos)

        open_list = []
        closed_set = set()
        heapq.heappush(open_list, start_node)

        while open_list:


            current = heapq.heappop(open_list)

            if current.position == self.goal_pos:

                self.path = self.reconstruct_path(current)
                return True  # Path found


            closed_set.add(current.position)
            self.visited_cells.add(current.position)
            self.draw()
            time.sleep(0.002)

            for new_pos in self.get_neighbors(current.position):
                if new_pos in self.obstacles or new_pos in closed_set:
                    continue

                new_node = Node(new_pos, current)
                new_node.g = current.g + 1
                new_node.h = self.heuristic(new_pos, self.goal_pos)
                new_node.f = new_node.g + new_node.h

                heapq.heappush(open_list, new_node)


        return False  # No path found




    def get_neighbors(self, position):
        x, y = position
        neighbors = [
            (x - 1, y), (x + 1, y),
            (x, y - 1), (x, y + 1)
        ]
        return [(nx, ny) for nx, ny in neighbors if 0 <= nx < self.size and 0 <= ny < self.size]

    def heuristic(self, pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])  # Manhattan Distance

    def reconstruct_path(self, current):

        path = []
        while current is not None:
            path.append(current.position)

            current = current.parent

        path.reverse()
        return path
    def draw(self):

        screen.fill(WHITE)
        for x in range(self.size):
            for y in range(self.size):

                rect = pygame.Rect(y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE)

                if (x, y) in self.visited_cells:
                    pygame.draw.rect(screen, TEAL, rect)
                pygame.draw.rect(screen, BLACK, rect, 1)

                if (x, y) == self.agent_pos:
                    pygame.draw.rect(screen, RED, rect)
                elif (x, y) == self.goal_pos:
                    pygame.draw.rect(screen, GREEN, rect)
                elif (x,y) in self.obstacles:
                    pygame.draw.rect(screen, BLACK, rect)

                elif (x,y) in self.path:
                    rect = pygame.Rect(y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                    pygame.draw.rect(screen, RED, rect)



                # Draw cell coordinates for reference
                text_surface = self.font.render(f"({x},{y})", True, LIGHT_GREY)
                screen.blit(text_surface, (y * CELL_SIZE + 5, x * CELL_SIZE + 5))

        pygame.display.flip()





def image_to_binary_array(image_path, new_width, new_height, threshold=128):
    # Load the image in grayscale
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Resize the image to the desired resolution
    img_resized = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_NEAREST)

    # Apply thresholding to convert to binary (1s and 0s)
    _, binary_img = cv2.threshold(img_resized, threshold, 1, cv2.THRESH_BINARY)

    return binary_img


image_path = "map.png"  # Replace with your image path
output_width = 20  # Desired output width
output_height = 20  # Desired output height

binary_array = image_to_binary_array(image_path, output_width, output_height)
obstacle=[]
for i in range(output_height):
    for j in range(output_width):
        if binary_array[i][j] == 0:
            obstacle.append((i,j))




# Print the 2D binary array
print(binary_array)





gw = GridWorld()
for i in obstacle:
    gw.obstacles.append(i)
print(gw.obstacles)

if gw.a_star():
    print("Path Found:", gw.path)
else:
    print("No Path Found!")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

   # time.sleep(.25)
    gw.draw()




pygame.quit()

