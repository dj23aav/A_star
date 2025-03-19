import pygame

GRID_SIZE = 10  # Set to match GridWorld default
CELL_SIZE = 50
WIDTH, HEIGHT = GRID_SIZE * CELL_SIZE, GRID_SIZE * CELL_SIZE
WHITE, BLACK, RED, GREY, LIGHT_GREY, GREEN, TEAL = (
    (255, 255, 255), (0, 0, 0), (255, 0, 0),
    (128, 128, 128), (200, 200, 200), (0, 255, 0), (0, 128, 128)
)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("A* Pathfinding")

class GridWorld:
    def __init__(self, size=10):
        self.size = size
        self.agent_pos = (0, 0)
        self.goal_pos = (size - 1, size - 1)
        self.obstacles = []
        self.visited_cells = set()
        self.path = []
        self.visited_cells.add(self.agent_pos)

        self.font = pygame.font.Font(None, 24)  # Font for text rendering

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

                # Draw cell coordinates for reference
                text_surface = self.font.render(f"({x},{y})", True, LIGHT_GREY)
                screen.blit(text_surface, (y * CELL_SIZE + 5, x * CELL_SIZE + 5))

        pygame.display.flip()

gw = GridWorld()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    gw.draw()

pygame.quit()


