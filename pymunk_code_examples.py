import pymunk

space = pymunk.Space()  # creates the space which contains the simulation
space.gravity = 0, -981  # sets its gravity

body = pymunk.Body()  # create a body
body.position = 50, 100  # set the position of the body

poly = pymunk.Poly.create_box(body)  # Create a box shape and attach to body
poly.mass = 10  # Set the mass on the shape
space.add(body, poly)  # Add both body and shape to the simulation

print_options = pymunk.SpaceDebugDrawOptions()  # For easy printing

for _ in range(100):  # Run simulation 100 steps total
    space.step(0.02)  # Step the simulation one step forward
    space.debug_draw(print_options)  # Print the state of the simulation
