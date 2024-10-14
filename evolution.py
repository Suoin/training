
import pygame
import sys

# Настройки
CELL_SIZE = 50
MAP_WIDTH = 10
MAP_HEIGHT = 10
FPS = 30

class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.position = [0, 0]  # Начальная позиция (x, y)

    def move_to(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.position = [x, y]

    def get_position(self):
        return tuple(self.position)

    def draw(self, screen):
        # Рисуем клетку
        rect = pygame.Rect(self.position[0] * CELL_SIZE, self.position[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, (0, 255, 0), rect)

def main():
    pygame.init()
    screen = pygame.display.set_mode((CELL_SIZE * MAP_WIDTH, CELL_SIZE * MAP_HEIGHT))
    clock = pygame.time.Clock()
    map_instance = Map(MAP_WIDTH, MAP_HEIGHT)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                cell_x = mouse_x // CELL_SIZE
                cell_y = mouse_y // CELL_SIZE
                map_instance.move_to(cell_x, cell_y)

        screen.fill((255, 255, 255))  # Заливаем экран белым
        map_instance.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()