import pygame

import Grid

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Width and height of each cell, as well as spacing
WIDTH = 20
HEIGHT = 20
MARGIN = 5

# Initialize pygame
pygame.init()

# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [255, 255]
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set title of screen
pygame.display.set_caption("A* Demo")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Administrative
ticktock = 0


# -------- Main Program Loop -----------

# -------- EXAMPLE 1

while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    # Set the screen background
    screen.fill(BLACK)

    # Display legend
    displaytext = "Red = Barrier, Green = Path"
    myfont = pygame.font.SysFont('arial', 20)
    textsurface = myfont.render(displaytext, False, WHITE)
    screen.blit(textsurface, (0, 230))

    # Display iteration
    iteration = "#1"
    textdisplay = myfont.render(iteration, False, WHITE)
    screen.blit(textdisplay, (230, 5))

    # -------- Game Board -----------

    # Declare and create 2 dimensional grid
    grid = []
    for row in range(9):
        # Add an empty array that will hold each cell in this row
        grid.append([])
        for column in range(9):
            grid[row].append(0)  # Append a cell in this position in the row

    # Draw the grid
    for row in range(9):
        for column in range(9):
            color = WHITE
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])

    # Limit to 60 frames per second
    clock.tick(5)
    ticktock += 1
    if ticktock == 10:
        break

    # Draw to screen
    pygame.display.flip()

while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    # Set the screen background
    screen.fill(BLACK)

    # Display legend
    displaytext = "Red = Barrier, Green = Path"
    myfont = pygame.font.SysFont('arial', 20)
    textsurface = myfont.render(displaytext, False, WHITE)
    screen.blit(textsurface, (0, 230))

    # Display iteration
    iteration = "#1"
    textdisplay = myfont.render(iteration, False, WHITE)
    screen.blit(textdisplay, (230, 5))

    # -------- Game Board -----------

    # Declare and create 2 dimensional grid
    grid = []
    for row in range(9):
        # Add an empty array that will hold each cell in this row
        grid.append([])
        for column in range(9):
            grid[row].append(0)  # Append a cell in this position in the row

    # Draw the grid
    for row in range(9):
        for column in range(9):
            color = WHITE
            pygame.draw.rect(screen,
                         color,
                         [(MARGIN + WIDTH) * column + MARGIN,
                          (MARGIN + HEIGHT) * row + MARGIN,
                          WIDTH,
                          HEIGHT])

    # Set barrier cells
    impassea = [(2, 2), (3, 3), (4, 4), (5, 3), (6, 2), (3, 2), (4, 2), (5, 2), (2, 2)]
    for point in impassea:
        grid[point[0]][point[1]] = 1

    # Draw the grid
    for row in range(9):
        for column in range(9):
            color = WHITE
            if grid[row][column] == 1:
                color = RED
            elif grid[row][column] == 2:
                color = GREEN
            pygame.draw.rect(screen,
                         color,
                         [(MARGIN + WIDTH) * column + MARGIN,
                          (MARGIN + HEIGHT) * row + MARGIN,
                          WIDTH,
                          HEIGHT])

    # Limit to 60 frames per second
    clock.tick(5)
    ticktock += 1
    if ticktock == 20:
        break

    # Draw to screen
    pygame.display.flip()

while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    # Set the screen background
    screen.fill(BLACK)

    # Display legend
    displaytext = "Red = Barrier, Green = Path"
    myfont = pygame.font.SysFont('arial', 20)
    textsurface = myfont.render(displaytext, False, WHITE)
    screen.blit(textsurface, (0, 230))

    # Display iteration
    iteration = "#1"
    textdisplay = myfont.render(iteration, False, WHITE)
    screen.blit(textdisplay, (230, 5))

    # -------- Game Board -----------

    # Declare and create 2 dimensional grid
    grid = []
    for row in range(9):
        # Add an empty array that will hold each cell in this row
        grid.append([])
        for column in range(9):
            grid[row].append(0)  # Append a cell in this position in the row

    # Draw the grid
    for row in range(9):
        for column in range(9):
            color = WHITE
            pygame.draw.rect(screen,
                         color,
                         [(MARGIN + WIDTH) * column + MARGIN,
                          (MARGIN + HEIGHT) * row + MARGIN,
                          WIDTH,
                          HEIGHT])

    # Set barrier cells
    impassea = [(2, 2), (3, 3), (4, 4), (5, 3), (6, 2), (3, 2), (4, 2), (5, 2), (2, 2)]
    for point in impassea:
        grid[point[0]][point[1]] = 1

    # Get path based on barriers and A*
    agrid = Grid.AStarGraph(impassea)
    result = Grid.AStarSearch((0, 0), (7, 3), agrid)
    # Set the path we found
    for point in result:
        grid[point[0]][point[1]] = 2

    # Draw the grid
    for row in range(9):
        for column in range(9):
            color = WHITE
            if grid[row][column] == 1:
                color = RED
            elif grid[row][column] == 2:
                color = GREEN
            pygame.draw.rect(screen,
                         color,
                         [(MARGIN + WIDTH) * column + MARGIN,
                          (MARGIN + HEIGHT) * row + MARGIN,
                          WIDTH,
                          HEIGHT])

    # Limit to 60 frames per second
    clock.tick(5)
    ticktock += 1
    if ticktock == 30:
        break

    # Draw to screen
    pygame.display.flip()

# -------- EXAMPLE 2
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    # Set the screen background
    screen.fill(BLACK)

    # Display legend
    displaytext = "Red = Barrier, Green = Path"
    myfont = pygame.font.SysFont('arial', 20)
    textsurface = myfont.render(displaytext, False, WHITE)
    screen.blit(textsurface, (0, 230))

    # Display iteration
    iteration = "#2"
    textdisplay = myfont.render(iteration, False, WHITE)
    screen.blit(textdisplay, (230, 5))

    # -------- Game Board -----------

    # Declare and create 2 dimensional grid
    grid = []
    for row in range(9):
        # Add an empty array that will hold each cell in this row
        grid.append([])
        for column in range(9):
            grid[row].append(0)  # Append a cell in this position in the row

    # Draw the grid
    for row in range(9):
        for column in range(9):
            color = WHITE
            if grid[row][column] == 1:
                color = RED
            elif grid[row][column] == 2:
                color = GREEN
            pygame.draw.rect(screen,
                         color,
                         [(MARGIN + WIDTH) * column + MARGIN,
                          (MARGIN + HEIGHT) * row + MARGIN,
                          WIDTH,
                          HEIGHT])

    # Limit to 60 frames per second
    clock.tick(5)
    ticktock += 1
    if ticktock == 40:
        break

    # Draw to screen
    pygame.display.flip()

while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    # Set the screen background
    screen.fill(BLACK)

    # Display legend
    displaytext = "Red = Barrier, Green = Path"
    myfont = pygame.font.SysFont('arial', 20)
    textsurface = myfont.render(displaytext, False, WHITE)
    screen.blit(textsurface, (0, 230))

    # Display iteration
    iteration = "#2"
    textdisplay = myfont.render(iteration, False, WHITE)
    screen.blit(textdisplay, (230, 5))

    # -------- Game Board -----------

    # Declare and create 2 dimensional grid
    gridb = []
    for row in range(9):
        # Add an empty array that will hold each cell in this row
        gridb.append([])
        for column in range(9):
            gridb[row].append(0)  # Append a cell in this position in the row

    # Set barrier cells
    impasseb = [(2, 2), (3, 2), (4, 2), (5, 2), (3, 5), (3, 3), (3, 4), (4, 3), (4, 4)]
    for point in impasseb:
        gridb[point[0]][point[1]] = 1

    # Draw the grid
    for row in range(9):
        for column in range(9):
            color = WHITE
            if gridb[row][column] == 1:
                color = RED
            elif gridb[row][column] == 2:
                color = GREEN
            pygame.draw.rect(screen,
                         color,
                         [(MARGIN + WIDTH) * column + MARGIN,
                          (MARGIN + HEIGHT) * row + MARGIN,
                          WIDTH,
                          HEIGHT])

    # Limit to 60 frames per second
    clock.tick(5)
    ticktock += 1
    if ticktock == 50:
        break

    # Draw to screen
    pygame.display.flip()

while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    # Set the screen background
    screen.fill(BLACK)

    # Display legend
    displaytext = "Red = Barrier, Green = Path"
    myfont = pygame.font.SysFont('arial', 20)
    textsurface = myfont.render(displaytext, False, WHITE)
    screen.blit(textsurface, (0, 230))

    # Display iteration
    iteration = "#2"
    textdisplay = myfont.render(iteration, False, WHITE)
    screen.blit(textdisplay, (230, 5))

    # -------- Game Board -----------

    # Declare and create 2 dimensional grid
    gridb = []
    for row in range(9):
        # Add an empty array that will hold each cell in this row
        gridb.append([])
        for column in range(9):
            gridb[row].append(0)  # Append a cell in this position in the row

    # Set barrier cells
    impasseb = [(2, 2), (3, 2), (4, 2), (5, 2), (3, 5), (3, 3), (3, 4), (4, 3), (4, 4)]
    for point in impasseb:
        gridb[point[0]][point[1]] = 1

    # Get path based on barriers and A*
    bgrid = Grid.AStarGraph(impasseb)
    result = Grid.AStarSearch((0, 0), (5, 6), bgrid)
    # Set the path we found
    for point in result:
        gridb[point[0]][point[1]] = 2

    # Draw the grid
    for row in range(9):
        for column in range(9):
            color = WHITE
            if gridb[row][column] == 1:
                color = RED
            elif gridb[row][column] == 2:
                color = GREEN
            pygame.draw.rect(screen,
                         color,
                         [(MARGIN + WIDTH) * column + MARGIN,
                          (MARGIN + HEIGHT) * row + MARGIN,
                          WIDTH,
                          HEIGHT])

    # Limit to 60 frames per second
    clock.tick(5)
    ticktock += 1
    if ticktock == 60:
        break

    # Draw to screen
    pygame.display.flip()

pygame.quit()