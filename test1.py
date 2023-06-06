from vpython import *

# Create scene
scene = canvas(width=800, height=600, center=vector(0, -8, 0), background=vector(1, 1, 1))

# Constants
gravity = -9.8  # Acceleration due to gravity

# Create objects
table = box(pos=vector(0, -9, 0), size=vector(10, 0.2, 10), color=vector(0.5, 0.5, 0.5))
copper_tube = cylinder(pos=vector(-2, 4, 0), axis=vector(0, -10, 0), radius=1, opacity=0.5, color=vector(1, 0.5, 0))
wooden_tube = cylinder(pos=vector(2, 4, 0), axis=vector(0, -10, 0), radius=1, opacity=0.5, color=vector(0.6, 0.4, 0.2))
copper_magnet = cylinder(pos=vector(-2, 11, 0), axis=vector(0, -0.5, 0), radius=0.2, color=vector(1, 0, 0))
wooden_magnet = cylinder(pos=vector(2, 11, 0), axis=vector(0, -0.5, 0), radius=0.2, color=vector(0, 0, 1))

# Set initial conditions
copper_magnet_velocity = 0
wooden_magnet_velocity = 0

# Time step
dt = 0.01

# Create graphs
pos_graph = graph(width=800, height=400, xtitle='Time', ytitle='Position', xmax=10, ymax=15)
pos_copper_curve = gcurve(graph=pos_graph, color=color.red, label='Copper Magnet')
pos_wooden_curve = gcurve(graph=pos_graph, color=color.blue, label='Wooden Magnet')

vel_graph = graph(width=800, height=400, xtitle='Time', ytitle='Velocity', xmax=10, ymax=10)
vel_copper_curve = gcurve(graph=vel_graph, color=color.red, label='Copper Magnet')
vel_wooden_curve = gcurve(graph=vel_graph, color=color.blue, label='Wooden Magnet')

while copper_magnet.pos.y >= -9 or wooden_magnet.pos.y >= -9:
    rate(100)

    # Update copper magnet position and velocity
    copper_magnet.pos.y += copper_magnet_velocity * dt
    copper_magnet_velocity += gravity * dt

    # Check if copper magnet hits the table
    if copper_magnet.pos.y - copper_magnet.axis.y / 2 <= table.pos.y + table.size.y / 2:
        # Stop moving
        copper_magnet_velocity = 0

    # Check if copper magnet is inside copper tube
    if copper_magnet.pos.y <= copper_tube.pos.y and abs(copper_magnet.pos.x - copper_tube.pos.x) <= copper_tube.radius:
        # Apply magnetic field effect in opposite direction
        copper_magnet_velocity -= copper_magnet_velocity * 3 * dt

    # Update wooden magnet position and velocity
    wooden_magnet.pos.y += wooden_magnet_velocity * dt
    wooden_magnet_velocity += gravity * dt

    # Check if wooden magnet hits the table
    if wooden_magnet.pos.y - wooden_magnet.axis.y / 2 <= table.pos.y + table.size.y / 2:
        # Stop moving
        wooden_magnet_velocity = 0

    # Append data to graph curves
    pos_copper_curve.plot(scene.time, copper_magnet.pos.y)
    pos_wooden_curve.plot(scene.time, wooden_magnet.pos.y)
    vel_copper_curve.plot(scene.time, copper_magnet_velocity)
    vel_wooden_curve.plot(scene.time, wooden_magnet_velocity)
