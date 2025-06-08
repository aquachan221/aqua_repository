import pygame

# Initialize pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 600, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paper.io Simple Clone - Single Player")

# Colors
WHITE = (255, 255, 255)
PLAYER_COLOR = (0, 245, 90)

# Game settings
BLOCK = 10
FPS = 30

class Player:
    def __init__(self, x, y, color, controls):
        self.x = x
        self.y = y
        self.color = color
        self.dir = (1, 0)
        self.trail = []
        self.territory = set()
        self.controls = controls
        # Only add the starting square to territory, not a line
        self.territory.add((self.x, self.y))

    def move(self):
        self.x += self.dir[0] * BLOCK
        self.y += self.dir[1] * BLOCK
        self.x %= WIDTH
        self.y %= HEIGHT

    def update_dir(self, key):
        if key == self.controls['up'] and self.dir != (0, 1):
            self.dir = (0, -1)
        elif key == self.controls['down'] and self.dir != (0, -1):
            self.dir = (0, 1)
        elif key == self.controls['left'] and self.dir != (1, 0):
            self.dir = (-1, 0)
        elif key == self.controls['right'] and self.dir != (-1, 0):
            self.dir = (1, 0)

    def draw(self, win):
        for tx, ty in self.territory:
            pygame.draw.rect(win, self.color, (tx, ty, BLOCK, BLOCK))
        for tx, ty in self.trail:
            pygame.draw.rect(win, self.color, (tx, ty, BLOCK, BLOCK))
        pygame.draw.rect(win, self.color, (self.x, self.y, BLOCK, BLOCK))

    def in_territory(self, pos):
        return pos in self.territory

    def add_trail(self):
        pos = (self.x, self.y)
        if pos not in self.territory and pos not in self.trail:
            self.trail.append(pos)

    def close_trail(self):
        for pos in self.trail:
            self.territory.add(pos)
        if self.trail:
            self.flood_fill_inside()
        self.trail = []

    def flood_fill_inside(self):
        if len(self.trail) < 3:
            return
        min_x = min(x for x, y in self.trail)
        max_x = max(x for x, y in self.trail)
        min_y = min(y for x, y in self.trail)
        max_y = max(y for x, y in self.trail)
        for y in range(min_y + 1, max_y, BLOCK):
            for x in range(min_x + 1, max_x, BLOCK):
                pos = (x, y)
                if pos not in self.territory and pos not in self.trail:
                    if self.point_in_polygon(x, y, self.trail):
                        self.flood_fill(x, y)
                        return

    def flood_fill(self, x, y):
        stack = [(x, y)]
        while stack:
            cx, cy = stack.pop()
            pos = (cx, cy)
            if pos in self.territory or pos in self.trail:
                continue
            self.territory.add(pos)
            for dx, dy in [(-BLOCK,0),(BLOCK,0),(0,-BLOCK),(0,BLOCK)]:
                nx, ny = cx+dx, cy+dy
                if 0 <= nx < WIDTH and 0 <= ny < HEIGHT:
                    npos = (nx, ny)
                    if npos not in self.territory and npos not in self.trail:
                        stack.append((nx, ny))

    def point_in_polygon(self, x, y, poly):
        num = len(poly)
        if num < 3:
            return False
        j = num - 1
        inside = False
        for i in range(num):
            xi, yi = poly[i]
            xj, yj = poly[j]
            if ((yi > y) != (yj > y)) and (x < (xj - xi) * (y - yi) / ((yj - yi) if (yj - yi) != 0 else 1e-9) + xi):
                inside = not inside
            j = i
        return inside

def main():
    clock = pygame.time.Clock()
    run = True
    player = Player(100, 100, PLAYER_COLOR, {
        'up': pygame.K_w, 'down': pygame.K_s, 'left': pygame.K_a, 'right': pygame.K_d
    })
    font = pygame.font.SysFont("bahnschrift", 25)

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                player.update_dir(event.key)

        player.move()
        if not player.in_territory((player.x, player.y)):
            player.add_trail()
        if (player.x, player.y) in player.territory and player.trail:
            player.close_trail()

        win.fill(WHITE)
        player.draw(win)
        score = font.render(f"Territory: {len(player.territory)}", True, (0,0,0))
        win.blit(score, (10, 10))
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
