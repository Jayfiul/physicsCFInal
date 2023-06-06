
# Create scene
scene = canvas(width=800, height=600, center=vector(0, -8, 0), background=vector(1, 1, 1))

# Constants
gravity = vector(0, -9.8, 0)  # Acceleration due to gravity

# Create objects
table = box(pos=vector(0, -9, 0), size=vector(10, 0.2, 10), color=vector(0.5, 0.5, 0.5))
copper_tube = cylinder(pos=vector(-2, 4, 0), axis=vector(0, -10, 0), radius=1, opacity=0.5, color=vector(1, 0.5, 0))
wooden_tube = cylinder(pos=vector(2, 4, 0), axis=vector(0, -10, 0), radius=1, opacity=0.5, color=vector(0.6, 0.4, 0.2))
copper_magnet = cylinder(pos=vector(-2, 11, 0), axis=vector(0, -0.5, 0), radius=0.5, color=vector(1, 0, 0))
wooden_magnet = cylinder(pos=vector(2, 11, 0), axis=vector(0, -0.5, 0), radius=0.5, color=vector(0, 0, 1))

# Set initial conditions
copper_magnet.velocity = vector(0, 0, 0)
wooden_magnet.velocity = vector(0, 0, 0)

# Time step
dt = 0.01

while copper_magnet.pos.y >= -9 or wooden_magnet.pos.y >= -9:
    rate(100)

    # Update copper magnet position and velocity
    copper_magnet.pos += copper_magnet.velocity * dt
    copper_magnet.velocity += gravity * dt

    # Check if copper magnet hits the table
    if copper_magnet.pos.y - copper_magnet.axis.y/2 <= table.pos.y + table.size.y / 2:
        # Stop moving
        copper_magnet.velocity = vector(0, 0, 0)

    # Check if copper magnet is inside copper tube
    if copper_magnet.pos.y <= copper_tube.pos.y and abs(copper_magnet.pos.x - copper_tube.pos.x) <= copper_tube.radius:
        # Apply magnetic field effect in opposite direction
        copper_magnet.velocity -= copper_magnet.velocity * 3 * dt
    else:
         copper_magnet.velocity -= vector(0,0,0)

    # Update wooden magnet position and velocity
    wooden_magnet.pos += wooden_magnet.velocity * dt
    wooden_magnet.velocity += gravity * dt

    # Check if wooden magnet hits the table
    if wooden_magnet.pos.y - wooden_magnet.axis.y/2 <= table.pos.y + table.size.y / 2:
        # Stop moving
        wooden_magnet.velocity = vector(0, 0, 0)

    # Check if wooden magnet is inside wooden tube
    if wooden_magnet.pos.y <= wooden_tube.pos.y and abs(wooden_magnet.pos.x - wooden_tube.pos.x) <= wooden_tube.radius:
        # Apply gravity only
        wooden_magnet.velocity += gravity * dt
