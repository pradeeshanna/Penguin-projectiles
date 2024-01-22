import pygame as pg
import sys

# Initialize Pygame
pg.init()

# Set up the Pygame window
width, height = 400, 300
screen = pg.display.set_mode((width, height))
clock = pg.time.Clock()

# Penguin colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 165, 0)

# Function to draw a small white penguin with hands
def draw_penguin(x, y):
    # Body
    pg.draw.ellipse(screen, WHITE, [x, y, 30, 60])

    # Head
    pg.draw.circle(screen, WHITE, (x + 15, y - 15), 15)

    # Eyes
    pg.draw.circle(screen, BLACK, (x + 12, y - 18), 3)
    pg.draw.circle(screen, BLACK, (x + 18, y - 18), 3)

    # Beak
    pg.draw.polygon(screen, ORANGE, [(x + 15, y - 12), (x + 14, y - 10), (x + 16, y - 10)])

    # Wings
    pg.draw.ellipse(screen, WHITE, [x - 5, y + 20, 10, 20])
    pg.draw.ellipse(screen, WHITE, [x + 25, y + 20, 10, 20])

    # Hands
    pg.draw.line(screen, WHITE, (x + 5, y + 10), (x - 5, y + 15), 3)
    pg.draw.line(screen, WHITE, (x + 25, y + 10), (x + 35, y + 15), 3)

# Main loop
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Fill the screen with a black color
    screen.fill(BLACK)

    # Draw a small white penguin at the center of the screen
    draw_penguin(width // 2 - 15, height // 2 - 30)

    # Update the display
    pg.display.flip()

    # Control the frame rate
    clock.tick(60)

# Quit Pygame
pg.quit()
sys.exit()
