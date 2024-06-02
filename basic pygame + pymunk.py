import pygame  # importing modules
import pymunk
import sys

# Physical Bodies in pymunk:
# - Static Body: A body that doesn't move, but other bodies can collide with it
# - Dynamic Body: A body that can be moved by physics
# - Kinematic Body: A body that can be moved by the player (or other non-physical code)

# For a Dynamic Body, we will need 3 different arguments:
# - Mass (weight)
# - Inertia (resistance to movement)
# - body_type (what body type we want)

# Note that all numbers selected are for ease of visualization and not for mathematical rigor


# Function for creating an object in simulation
def create_apple(space, pos):
    body = pymunk.Body(1, 100, body_type=pymunk.Body.DYNAMIC)  # initializes the body object
    body.position = pos  # sets the position of the body to whatever coordinates were passed in
    shape = pymunk.Circle(body, 100)  # sets the shape of the body's collider
    space.add(body, shape)  # adds the body and shape to our space
    return shape  # returns the shape at the calculated position of the body


# Function for representing object in simulation
def draw_apples(apples):
    for apple in apples:  # Can represent a list of objects
        pos_x = int(apple.body.position.x)  # pygame requires positional arguments to be integer values
        pos_y = int(apple.body.position.y)  # so we must convert the body's position from floats
        apple_rect = apple_surface.get_rect(center=(pos_x, pos_y))  # Draws a rectangle
        # This rectangle is centered at the position of the body, and has dimensions of the surface
        screen.blit(apple_surface, apple_rect)  # Puts it on the screen
        # Will need to check the documentation for this


def static_ball(space):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)  # static bodies do not need mass or inertia
    body.position = (500, 500)  # sets the position of the body
    shape = pymunk.Circle(body, 50)  # sets the shape of the body's collider
    space.add(body, shape)  # adds the body and shape to our space
    return shape  # returns the shape at the calculated position of the body

# By just using this same basic formula for creating and initializing objects in a space, you can create anything


def draw_static_balls(balls):
    for ball in balls:
        pos_x = int(ball.body.position.x)  # pygame requires positional arguments to be integer values
        pos_y = int(ball.body.position.y)  # so we must convert the body's position from floats
        pygame.draw.circle(screen, (0, 0, 0), (pos_x, pos_y), 80)
        # Screen object to draw on, color of drawing, center of drawing, size of drawing
        # Only somewhat blatantly copy and pasted from above
        # We could probably generalize this function...


pygame.init()  # initiating pygame
screen = pygame.display.set_mode((800, 800))  # creating the display surface
clock = pygame.time.Clock()  # creating the game clock
space = pymunk.Space()  # initializing our physics space
space.gravity = (0, 100)  # first input corresponds to the horizontal gravity, second to the vertical gravity

apple_surface = pygame.image.load("pixel_apple.png")  # importing a picture of an apple
apples = []  # creates a list to hold our simulation objects

balls = []  # pycharm wants me to turn this sequence into a one-liner...
balls.append(static_ball(space))


while True:  # Game Loop
    for event in pygame.event.get():  # checking for user input
        if event.type == pygame.QUIT:  # input to close the game
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:  # Handles mouseclick events
            apples.append((create_apple(space, event.pos)))  # Creates an apple at the event click position

    screen.fill((217, 217, 217))  # background color
    draw_apples(apples)  # draws every apple in the simulation
    draw_static_balls(balls)  # interestingly, we don't have to draw this, and objects will still interact with it
    space.step(1/50)  # updates our physics simulation.the loop first updates the physics
    pygame.display.update()  # and then updates the screen
    # Note: We do not have to have these two loops concurrently, they could be looped independently
    clock.tick(120)  # limiting the frames per second to 120

