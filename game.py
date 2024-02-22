import pygame as pg
import sys
from math import pi, cos, sin, sqrt

# Initialize Pygame
pg.init()

# Function to display text on the screen
def display_text(text, color, position, size):
    font = pg.font.Font(None, size)  # Use the default font
    rendered_text = font.render(text, True, color)
    screen.blit(rendered_text, position)

# Class to create a colored rectangle
class ColoredRect():
    def __init__(self, size, color):
        self.surface = pg.Surface(size)
        self.surface.fill(color)
    def show(self, position):
        rect = self.surface.get_rect(topleft=position)
        screen.blit(self.surface, rect)
def main():
    # Set up the Pygame window
    global screen
    screen = pg.display.set_mode((1000, 600))
    clock = pg.time.Clock()

    # Create the ground object
    ground = ColoredRect((1000, 100), (139, 69, 19))  # Brown color for the ground

    # Initialize ball properties
    ball_position = (10, 510)
    gravity = 98
    launch_angle = 22.5
    initial_velocity = 300
    vx = initial_velocity * cos(launch_angle * pi / 180)
    vy = initial_velocity * sin(launch_angle * pi / 180)
    bounce_coefficient = 0.6
    friction = 1000
    time_counter = 120
    trajectory_points = [(10, 510)]
    trajectory_points_1 = []
    trajectory_points_2 = []

    # Initialize variables for state transitions
    state = 1
    time_interval = 0.1

    # Main loop
    running = True
    while running:
        # Get the current frames per second (FPS)
        fps = clock.get_fps()
        if fps >= 60:
            fps = 60
        if fps == 0:
            fps = 10**100

        # Get and handle events
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

        # Fill the screen with a black color
        screen.fill((0, 0, 0))

        # Display the ground rectangle
        ground.show((0, 520))

        # Draw a white circle representing the ball
        pg.draw.circle(screen, (255, 255, 255), ball_position, 10)

        # Attempt to draw lines with specific colors for different states
        try:
            pg.draw.lines(screen, (0, 0, 255), False, trajectory_points, 5)
        except:
            pass
        else:
            pg.draw.lines(screen, (0, 0, 255), False, trajectory_points, 5)
        try:
            pg.draw.lines(screen, (0, 255, 0), False, trajectory_points_1, 5)
        except:
            pass
        else:
            pg.draw.lines(screen, (0, 255, 0), False, trajectory_points_1, 5)
        try:
            pg.draw.lines(screen, (255, 0, 0), False, trajectory_points_2, 5)
        except:
            pass
        else:
            pg.draw.lines(screen, (255, 0, 0), False, trajectory_points_2, 5)

        # Calculate angular velocity
        angular_velocity = sqrt(vx**2 + vy**2)

        # Check the current state (state) for state-specific actions
        if state == 1:
            # Check if it's time to add a point
            if time_counter >= fps:
                time_counter = 0
                trajectory_points.append(ball_position)
            else:
                time_counter += fps / (60 * time_interval)

            # Check if angular velocity is below a threshold
            if angular_velocity < 1:
                trajectory_points.append(ball_position)
                ball_position = (10, 510)
                launch_angle += 22.5
                vx = initial_velocity * cos(launch_angle * pi / 180)
                vy = initial_velocity * sin(launch_angle * pi / 180)
                time_counter = 120
                state += 1
                angular_velocity = sqrt(vx**2 + vy**2)

            # Update ball position and velocity
            ball_position = (ball_position[0] + vx / fps, ball_position[1] - vy / fps)
            vy = vy - gravity / fps

            # Check for collision with walls and add point if needed
            if (
                ball_position[0] < 10
                or ball_position[0] > 990
                or ball_position[1] < 10
                or ball_position[1] > 510
            ):
                trajectory_points.append(ball_position)

        # State 2
        elif state == 2:
            if time_counter >= fps:
                time_counter = 0
                trajectory_points_1.append(ball_position)
            else:
                time_counter += fps / (60 * time_interval)

            if angular_velocity < 1:
                trajectory_points_1.append(ball_position)
                ball_position = (10, 510)
                launch_angle += 22.5
                vx = initial_velocity * cos(launch_angle * pi / 180)
                vy = initial_velocity * sin(launch_angle * pi / 180)
                time_counter = 120
                state += 1
                angular_velocity = sqrt(vx**2 + vy**2)

            ball_position = (ball_position[0] + vx / fps, ball_position[1] - vy / fps)
            vy = vy - gravity / fps

            if (
                ball_position[0] < 10
                or ball_position[0] > 990
                or ball_position[1] < 10
                or ball_position[1] > 510
            ):
                trajectory_points_1.append(ball_position)

        # State 3
        elif state == 3:
            if time_counter >= fps:
                time_counter = 0
                trajectory_points_2.append(ball_position)
            else:
                time_counter += fps / (60 * time_interval)

            if angular_velocity < 1:
                trajectory_points_2.append(ball_position)
                ball_position = (10, 510)
                launch_angle += 22.5
                vx = initial_velocity * cos(launch_angle * pi / 180)
                vy = initial_velocity * sin(launch_angle * pi / 180)
                time_counter = 120
                state = 1  # Transition to the first state
                angular_velocity = sqrt(vx**2 + vy**2)

            ball_position = (ball_position[0] + vx / fps, ball_position[1] - vy / fps)
            vy = vy - gravity / fps

            if (
                ball_position[0] < 10
                or ball_position[0] > 990
                or ball_position[1] < 10
                or ball_position[1] > 510
            ):
                trajectory_points_2.append(ball_position)

        # Check for collision with walls and update ball position and velocity accordingly
        if ball_position[0] > 990:
            ball_position = (990, ball_position[1])
            vx = -vx * bounce_coefficient
        if ball_position[0] < 10:
            ball_position = (10, ball_position[1])
            vx = -vx * bounce_coefficient
        if ball_position[1] > 510:
            if abs(vx) < friction / fps:
                vx = 0
            else:
                vx += friction / fps if vx < 0 else -friction / fps
            ball_position = (ball_position[0], 510)
            vy = -vy * bounce_coefficient
        if ball_position[1] < 10:
            if abs(vx) < friction / fps:
                vx = 0
            else:
                vx += friction / fps if vx < 0 else -friction / fps
            ball_position = (ball_position[0], 10)
            vy = -vy * bounce_coefficient

        # Display information on the screen (velocity, angle, and FPS)
        display_text(f'Velocity={round(angular_velocity, ndigits=2)} pixels/sec', (255, 255, 255), (400, 10), 50)
        display_text(f'Angle={launch_angle}° ', (255, 255, 255), (100, 10), 50)
        display_text(str(round(fps)), (0, 255, 0), (10, 10), 30)

        # Update the display and control the frame rate
        pg.display.update()
        clock.tick(60)

