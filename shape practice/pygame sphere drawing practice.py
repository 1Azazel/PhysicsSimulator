import numpy as np
import pygame
import pygame.gfxdraw

WIDTH = 1280
HEIGHT = 720

RADIUS = 40

root_2 = np.sqrt(2)
root_3 = np.sqrt(3)
neg_root_2 = np.negative(np.sqrt(2))
neg_root_3 = np.negative(np.sqrt(3))

TRANSFORMATION_MATRIX = np.array([[root_3, 0, neg_root_3], [1, 2, 1], [root_2, neg_root_2, root_2]])
ORTHOGRAPHIC_PROJECTION_MATRIX = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 0]])

XY_RECT_COORD = [(RADIUS, RADIUS, 0), (RADIUS, -RADIUS, 0), (-RADIUS, RADIUS, 0), (-RADIUS, -RADIUS, 0)]
XZ_RECT_COORD = [(RADIUS, 0, RADIUS), (RADIUS, 0, -RADIUS), (-RADIUS, 0, RADIUS), (-RADIUS, 0, -RADIUS)]
YZ_RECT_COORD = [(0, RADIUS, RADIUS), (0, RADIUS, -RADIUS), (0, -RADIUS, RADIUS), (0, -RADIUS, -RADIUS)]

# Use these as what you project vectors of other magnitudes onto
x_direction_vector = pygame.Vector2(np.tan(np.pi / 3) * (HEIGHT / 2) + (WIDTH / 2), HEIGHT)
y_direction_vector = pygame.Vector2((WIDTH / 2), 0)
z_direction_vector = pygame.Vector2(np.tan(np.pi / 3) * (HEIGHT / 2) - (WIDTH / 2), HEIGHT)

i = x_direction_vector.normalize()
j = y_direction_vector.normalize()
k = z_direction_vector.normalize()

# For the circle that represents the xy cross-section of a sphere at the origin:
# The circle would have a horizontal radius of r, and a vertical radius of r
rx_of_xy_ellipse = RADIUS
ry_of_xy_ellipse = RADIUS


# Let's try and implement some matrix math to make the isometric transformations easier on ourselves
def convert_point_in_3d_to_2d(point):
    x = point[0]
    y = point[1]
    z = point[2]
    three_d_vector = np.array([[x], [y], [z]])
    composite_matrix = np.matmul(TRANSFORMATION_MATRIX, three_d_vector)
    rotated_vector = (1 / np.sqrt(6)) * composite_matrix
    return rotated_vector


def orthographic_projection(rotated_vector):
    two_d_vector = np.matmul(ORTHOGRAPHIC_PROJECTION_MATRIX, rotated_vector)
    return two_d_vector


def xyz_coord_to_pygame_vector(coordinate_tuple):
    two_d_vector = orthographic_projection(convert_point_in_3d_to_2d(coordinate_tuple))
    x_value = two_d_vector[0, 0] + (WIDTH / 2)  # Grabs the value in the first row, first column
    # still have to reference column # even for an array with just 1 column
    y_value = two_d_vector[1, 0] + (HEIGHT / 2)  # We add 1/2 the width and height because our 3d space is centered at
    # the origin, but the pygame screen is centered at the midpoint of the height and width
    return pygame.Vector2(x_value, y_value)


def list_of_xyz_to_list_of_pygame_vectors(coordinate_list):
    vector_list = []
    for coordinate in coordinate_list:
        vector_list.append(xyz_coord_to_pygame_vector(coordinate))
    return vector_list


def get_xy_magnitude_of_xyz_vector(point_at_end_of_vector):
    xy_vector = xyz_coord_to_pygame_vector(point_at_end_of_vector)
    return xy_vector.magnitude()


# The rectangle that encloses a circle in the xy plane will have the following 4 points as coordinates:
# (r, r, 0), (r, -r, 0), (-r, r, 0), (-r, -r, 0)
# Since the pygame.Rect object requires the top left point, and the width and height;
# Let the point with -x, +y be the top left, and the point with +x, -y be the bottom right
# top_left = (-r, r, 0)
# bot_right = (r, -r, 0)
# These points are in the xyz plane, first we must convert them to xy
# Then we find the height via |y2 - y1|, and the width via |x2 - x1|

# We are interested in the ellipses that are given by intersection of some 2D plane with some sphere
# In 3 dimensions, we could represent the equation for each in the following ways:


def draw_three_ellipses(center):
    r = RADIUS
    x1 = (r, 0, 0)
    y1 = (0, r, 0)
    z1 = (0, 0, r)

    x1v = pygame.Vector3(x1)
    print("pre-transform x radii len: " + str(x1v.length()))

    x_radius = int(xyz_coord_to_pygame_vector(x1).length())
    y_radius = int(xyz_coord_to_pygame_vector(y1).length())
    z_radius = int(xyz_coord_to_pygame_vector(z1).length())

    x = int(center.x)
    y = int(center.y)
    print("post-transform x radii length: " + str(x_radius))
    pygame.gfxdraw.ellipse(screen, x, y, z_radius, y_radius, (100, 100, 100, 255))
    # pygame.gfxdraw.ellipse(screen, x, y, x_radius, y_radius, color="black")
    # pygame.gfxdraw.ellipse(screen, x, y, x_radius, z_radius, color="black")


# pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0

height = screen.get_height()
width = screen.get_width()
half_height = screen.get_height() / 2
half_width = screen.get_width() / 2
x_width_magnitude = np.tan(np.pi / 3) * half_height
negative_half_height = np.negative(half_height)
negative_x_width_magnitude = np.negative(x_width_magnitude)

origin = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
y_end = pygame.Vector2(screen.get_width() / 2, 0)
# For x_end and z_end, the line that represents the axis runs from the origin to the end of the screen
# It should have a total length equal to the hypotenuse of the triangle formed by weight /2 and height /2 of the window
x_end = pygame.Vector2(x_width_magnitude + half_width, height)
z_end = pygame.Vector2(x_width_magnitude - half_width, height)


player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    # Let's draw the circle that is formed when a sphere intersects the xy, xz, and yz in an isometric configuration
    # The code below gives us the circle that is formed when a sphere intersects with the xy plane in a 2-D space
    # pygame.draw.circle(screen, "black", player_pos, 40)
    # pygame.draw.circle(screen, "white", player_pos, 38)

    # Let's draw the x, y, and z axes using transformation matrices, and then apply them to our spherical cross-sections
    pygame.draw.line(screen, "green", origin, y_end)
    pygame.draw.line(screen, "red", origin, x_end)
    pygame.draw.line(screen, "blue", origin, z_end)
    # It works! We have to make sure to save this code

    draw_three_ellipses(player_pos)

    # Let's try and restrict the movement of the player to only the xz plane
    # Then the xz plane is the floor, the xy and yz planes are walls, and the y dimension is Up
    # Then, we need to translate key presses into movement in our isometric space
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()


