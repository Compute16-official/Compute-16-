import pygame
import subprocess
## This is to make the screen size
screen_size = (800, 600)
## This is to make the backround screen color yellow
pygame.init()
screen = pygame.display.set_mode(screen_size)
screen.fill((48, 25, 52))
pygame.display.flip()
import pygame.font
pygame.font.init()

# Screen setup.
screen_size = (800, 600)
pygame.init()
screen = pygame.display.set_mode(screen_size)
screen.fill((48, 25, 52))
pygame.display.flip()

import pygame.font
pygame.font.init()

# Modified selection placeholder code.
pygame.key.set_repeat(400, 30)

font = pygame.font.Font("assets/8bit.ttf", 30)

def process_command(command):
    command = command.strip()
    if command.startswith("cart.make ="):
        cart_name = command.split("=", 1)[1].strip()
        if cart_name:
            subprocess.Popen(["python", "cart-make.py", cart_name])

# Set window title.
pygame.display.set_caption("Compute 16 Pro")
line_height = font.get_linesize()

# Define colors.
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
GREEN = (0, 255, 0)
PURPLE = (128, 0, 128)
GREY = (128, 128, 128)
SKYBLUE = (135, 206, 235)
WHITE = (255, 255, 255)

# Banner segments with per-letter colors.
banner_segments = [
    ("C", YELLOW),
    ("o", ORANGE),
    ("m", GREEN),
    ("p", PURPLE),
    ("u", YELLOW),
    ("t", ORANGE),
    ("e", GREEN),
    (" ", WHITE),
    ("16", GREY),
    (" ", WHITE),
    ("Pro", SKYBLUE)
]

def draw_banner():
    segment_surfaces = []
    total_width = 0
    for text, color in banner_segments:
        surf = font.render(text, True, color)
        segment_surfaces.append(surf)
        total_width += surf.get_width()
    banner_x = (screen_size[0] - total_width) // 2
    banner_y = 10  # top margin

    # Draw a decoration pattern above the banner.
    deco_color = WHITE
    pygame.draw.line(screen, deco_color, (banner_x - 20, banner_y + font.get_height()//2),
                     (banner_x - 5, banner_y + font.get_height()//2), 2)
    pygame.draw.line(screen, deco_color, (banner_x - 5, banner_y + font.get_height()//2),
                     (banner_x - 12, banner_y - 5), 2)
    pygame.draw.line(screen, deco_color, (banner_x - 5, banner_y + font.get_height()//2),
                     (banner_x - 12, banner_y + font.get_height() + 5), 2)

    current_x = banner_x
    for surf in segment_surfaces:
        screen.blit(surf, (current_x, banner_y))
        current_x += surf.get_width()
    return banner_y + font.get_height() + 10

text_lines = [""]
editor_start_y = None

def redraw():
    screen.fill((48, 25, 52))
    banner_bottom = draw_banner()
    global editor_start_y
    editor_start_y = banner_bottom + 10
    y = editor_start_y
    for line in text_lines:
        rendered = font.render(line, True, WHITE)
        screen.blit(rendered, (10, y))
        y += line_height
    pygame.display.flip()

redraw()

# Editing mode.
editing = True
while editing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            editing = False
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                editing = False
            elif event.key == pygame.K_RETURN:
                text_lines.append("")
            elif event.key == pygame.K_BACKSPACE:
                if text_lines[-1]:
                    text_lines[-1] = text_lines[-1][:-1]
                elif len(text_lines) > 1:
                    text_lines.pop()
            else:
                text_lines[-1] += event.unicode
    redraw()

# Main loop just to keep window open.
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
font = pygame.font.Font("assets/8bit.ttf", 30)
def process_command(command):
    command = command.strip()
    if command.startswith("cart.make ="):
        cart_name = command.split("=", 1)[1].strip()
        if cart_name:
            # Run the cart-make.py passing the cart name as an argument.
            subprocess.Popen(["python", "cart-make.py", cart_name])
pygame.display.set_caption("Python Retro Game Maker")
line_height = font.get_linesize()

# Define colors
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
GREEN = (0, 255, 0)
PURPLE = (128, 0, 128)
GREY = (128, 128, 128)
SKYBLUE = (135, 206, 235)
WHITE = (255, 255, 255)

# The banner segments for "Compute 16 Pro" with per-letter colors.
# "Compute" letters: C, o, m, p, u, T, E 
# "16" in grey, and "Pro" in sky blue.
banner_segments = [
    ("C", YELLOW), 
    ("o", ORANGE), 
    ("m", GREEN),
    ("p", PURPLE),
    ("u", YELLOW),
    ("t", ORANGE),
    ("e", GREEN),
    (" ", WHITE),
    ("16", GREY),
    (" ", WHITE),
    ("Pro", SKYBLUE)
]

def draw_banner():
    # Render each segment and compute total width.
    segment_surfaces = []
    total_width = 0
    for text, color in banner_segments:
        surf = font.render(text, True, color)
        segment_surfaces.append(surf)
        total_width += surf.get_width()
    # Position banner at the middle top in a "| \ /" style arrangement:
    # We place the text centered horizontally, with a slight left offset to mimic the pattern.
    banner_x = (screen_size[0] - total_width) // 2
    banner_y = 10  # top margin
    # Optionally draw a simple decoration pattern resembling "| \ /" above the banner.
    # We'll draw three lines: a vertical line, a backslash and a forward slash.
    deco_color = WHITE
    pygame.draw.line(screen, deco_color, (banner_x - 20, banner_y + font.get_height()//2), (banner_x - 5, banner_y + font.get_height()//2), 2)
    pygame.draw.line(screen, deco_color, (banner_x - 5, banner_y + font.get_height()//2), (banner_x - 12, banner_y - 5), 2)
    pygame.draw.line(screen, deco_color, (banner_x - 5, banner_y + font.get_height()//2), (banner_x - 12, banner_y + font.get_height() + 5), 2)
    # Blit banner segments.
    current_x = banner_x
    for surf in segment_surfaces:
        screen.blit(surf, (current_x, banner_y))
        current_x += surf.get_width()
    # Return the bottom y coordinate of the banner for layout purposes.
    return banner_y + font.get_height() + 10

text_lines = [""]
# Let the starting y for the text editor be below the banner.
editor_start_y = None

def redraw():
    screen.fill((48, 25, 52))
    # Draw the banner and get its bottom position.
    banner_bottom = draw_banner()
    global editor_start_y
    editor_start_y = banner_bottom + 10
    # Draw the text editor lines starting below the banner.
    y = editor_start_y
    for line in text_lines:
        rendered = font.render(line, True, (255, 255, 255))
        screen.blit(rendered, (10, y))
        y += line_height
    pygame.display.flip()

redraw()

editing = True
while editing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            editing = False
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                editing = False
            elif event.key == pygame.K_RETURN:
                text_lines.append("")
            elif event.key == pygame.K_BACKSPACE:
                if text_lines[-1]:
                    text_lines[-1] = text_lines[-1][:-1]
                elif len(text_lines) > 1:
                    text_lines.pop()
            else:
                text_lines[-1] += event.unicode
    redraw()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()