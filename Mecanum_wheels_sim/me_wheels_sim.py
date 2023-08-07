import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants for screen dimensions
WIDTH, HEIGHT = 1200, 900  # Increase the screen size

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mechanum Wheel Simulation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

Power = 255
max_speed = 20

def update_vector(theta, turn):
    sin = math.sin(theta - math.pi / 4)
    cos = math.cos(theta - math.pi / 4)
    max_value = max(math.fabs(sin), math.fabs(cos))

    TopLeft = Power * cos / max_value + turn
    TopRight = Power * sin / max_value - turn
    BotLeft = Power * sin / max_value + turn
    BotRight = Power * cos / max_value - turn

    if (Power + math.fabs(turn)) > 1:
        TopLeft /= Power + turn
        TopRight /= Power + turn
        BotLeft /= Power + turn
        BotRight /= Power + turn

    return TopLeft, TopRight, BotLeft, BotRight
  
def draw_box(TopLeft, TopRight, BotLeft, BotRight):
    # Constants for the box dimensions
    BOX_WIDTH, BOX_HEIGHT = 240, 400

    # Calculate the position to place the box in the middle of the screen
    box_x = (WIDTH - BOX_WIDTH) // 2
    box_y = (HEIGHT - BOX_HEIGHT) // 2

    # Draw the outline of the box on the screen
    pygame.draw.rect(screen, BLACK, (box_x, box_y, BOX_WIDTH, BOX_HEIGHT), width=2)

    # Draw wheels at each corner of the box
    wheel_width, wheel_height = 60, 120  # Adjust the values for vertical elongation
    wheel_color = BLACK

    top_left_wheel = (box_x - wheel_width, box_y + wheel_height / 2)
    top_right_wheel = (box_x + BOX_WIDTH + wheel_width, box_y + wheel_height / 2)
    bot_left_wheel = (box_x - wheel_width, box_y + BOX_HEIGHT - wheel_height / 2)
    bot_right_wheel = (box_x + BOX_WIDTH + wheel_width, box_y + BOX_HEIGHT - wheel_height / 2)
    
    top_left_wheel_center = (box_x - wheel_width / 2, box_y + wheel_height / 2)
    top_right_wheel_center = (box_x + BOX_WIDTH + wheel_width / 2, box_y + wheel_height / 2)
    bot_left_wheel_center = (box_x - wheel_width / 2, box_y + BOX_HEIGHT - wheel_height / 2)
    bot_right_wheel_center = (box_x + BOX_WIDTH + wheel_width / 2, box_y + BOX_HEIGHT - wheel_height / 2)

    pygame.draw.ellipse(screen, wheel_color, (top_left_wheel[0], top_left_wheel[1] - wheel_height / 2, wheel_width, wheel_height), width=2)
    pygame.draw.ellipse(screen, wheel_color, (top_right_wheel[0] - wheel_width, top_right_wheel[1] - wheel_height / 2, wheel_width, wheel_height), width=2)
    pygame.draw.ellipse(screen, wheel_color, (bot_left_wheel[0], bot_left_wheel[1] - wheel_height / 2, wheel_width, wheel_height), width=2)
    pygame.draw.ellipse(screen, wheel_color, (bot_right_wheel[0] - wheel_width, bot_right_wheel[1] - wheel_height / 2, wheel_width, wheel_height), width=2)

    # Draw vectors from the center of the screen to the wheels
    center_x, center_y = WIDTH // 2, HEIGHT // 2
    pygame.draw.line(screen, GREEN, top_left_wheel_center, (top_left_wheel_center[0], top_left_wheel_center[1] + TopLeft * max_speed), width=3)
    pygame.draw.line(screen, GREEN, top_right_wheel_center, (top_right_wheel_center[0], top_right_wheel_center[1] + TopRight * max_speed), width=3)
    pygame.draw.line(screen, GREEN, bot_left_wheel_center, (bot_left_wheel_center[0], bot_left_wheel_center[1] + BotLeft * max_speed), width=3)
    pygame.draw.line(screen, GREEN, bot_right_wheel_center, (bot_right_wheel_center[0], bot_right_wheel_center[1] + BotRight * max_speed), width=3)

    draw_small_arrow(top_left_wheel_center, (top_left_wheel_center[0], top_left_wheel_center[1] + TopLeft * max_speed))
    draw_small_arrow(top_right_wheel_center, (top_right_wheel_center[0], top_right_wheel_center[1] + TopRight * max_speed))
    draw_small_arrow(bot_left_wheel_center, (bot_left_wheel_center[0], bot_left_wheel_center[1] + BotLeft * max_speed))
    draw_small_arrow(bot_right_wheel_center, (bot_right_wheel_center[0], bot_right_wheel_center[1] + BotRight * max_speed))

def draw_arrow(start, end):
    # Calculate the angle of the arrowhead (rotate it by 30 degrees in both directions)
    arrow_angle = math.atan2(start[1] - end[1], start[0] - end[0]) - math.pi + math.radians(180)
    arrow_length = 30  # Increase the arrow length

    # Calculate the three points for the arrowhead triangle
    arrow_point1 = (end[0] + arrow_length * math.cos(arrow_angle + math.radians(30)),
                    end[1] + arrow_length * math.sin(arrow_angle + math.radians(30)))
    arrow_point2 = (end[0] + arrow_length * math.cos(arrow_angle - math.radians(30)),
                    end[1] + arrow_length * math.sin(arrow_angle - math.radians(30)))

    # Draw the arrowhead
    pygame.draw.polygon(screen, GREEN, [end, arrow_point1, arrow_point2])

def draw_small_arrow(start, end):
    # Calculate the angle of the arrowhead (rotate it by 30 degrees in both directions)
    arrow_angle = math.atan2(start[1] - end[1], start[0] - end[0]) - math.pi + math.radians(180)
    arrow_length = 14  # Increase the arrow length

    # Calculate the three points for the arrowhead triangle
    arrow_point1 = (end[0] + arrow_length * math.cos(arrow_angle + math.radians(30)),
                    end[1] + arrow_length * math.sin(arrow_angle + math.radians(30)))
    arrow_point2 = (end[0] + arrow_length * math.cos(arrow_angle - math.radians(30)),
                    end[1] + arrow_length * math.sin(arrow_angle - math.radians(30)))

    # Draw the arrowhead (as a filled polygon)
    pygame.draw.line(screen, GREEN, (end[0] + 1, end[1]), arrow_point1, width=3)
    pygame.draw.line(screen, GREEN, (end[0] + 1, end[1]), arrow_point2, width=3)

def line_length(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get the mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Clear the screen
    screen.fill(WHITE)

    # Draw the box and wheels, and vectors from the center to the wheels

    # Draw a vector from the center of the screen to the mouse position
    center_x, center_y = WIDTH // 2, HEIGHT // 2
    dx, dy = mouse_x - center_x, mouse_y - center_y

    # Limit the length of the vector to a maximum value
    max_length = 150
    length = math.sqrt(dx**2 + dy**2)
    if length > max_length:
        scale = max_length / length
        dx *= scale
        dy *= scale

    # Calculate the endpoint of the limited vector
    end_x, end_y = center_x + dx, center_y + dy

    # Calculate the angle of the line in radians
    line_angle = math.atan2(dy, dx)

    # Calculate the angle in degrees (optional, for display purposes)
    line_angle_degrees = math.degrees(line_angle)

    TopLeft, TopRight, BotLeft, BotRight = update_vector(line_angle, 0)

    draw_box(TopLeft, TopRight, BotLeft, BotRight)
    # Draw the limited vector from the center to the mouse position

    max_speed = (line_length(center_x, center_y, end_x, end_y) / 100) * 40

    pygame.draw.line(screen, GREEN, (center_x, center_y), (end_x, end_y), width=4)
    draw_arrow((center_x, center_y), (end_x, end_y))

    font = pygame.font.Font(None, 30)
    angle_text = font.render(f"Angle: {line_angle_degrees:.2f} degrees", True, BLACK)
    screen.blit(angle_text, (10, 10))

    # Update the display
    pygame.display.update()
