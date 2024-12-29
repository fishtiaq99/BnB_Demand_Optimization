import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Function to calculate demand of BnB
def demand_bnb(P_B, P_A, P_C):
    # Calculate demand of BnB using the given formula
    demand = 10000 - 2.5 * P_B**2 + 3 * P_A + 1.5 * P_C
    return demand

# Generating price values
P_B_values = np.linspace(0, 200, 100)  # Generate 100 equally spaced values from 0 to 200 for the price of BnB
P_A_values = np.linspace(0, 200, 100)  # Generate 100 equally spaced values from 0 to 200 for the price of product A
P_C_values = np.linspace(0, 200, 100)  # Generate 100 equally spaced values from 0 to 200 for the price of product C

# Creating meshgrid
# Meshgrid creates a grid of points for each combination of the provided values
P_B_grid, P_A_grid, P_C_grid = np.meshgrid(P_B_values, P_A_values, P_C_values, indexing='ij')

# Calculating demand for each combination of prices
demand_grid = demand_bnb(P_B_grid, P_A_grid, P_C_grid)

# Plotting
fig = plt.figure()  # Create a new figure
ax = fig.add_subplot(111, projection='3d')  # Add a 3D subplot to the figure

# Plot surface
# Plot the surface plot using the calculated demand grid
surf = ax.plot_surface(P_B_grid[:,:,0], P_A_grid[:,:,0], demand_grid[:,:,0], cmap='viridis')
# Set labels for axes
ax.set_xlabel('Price of BnB ($)')  # Set label for x-axis
ax.set_ylabel('Price of Product A ($)')  # Set label for y-axis
ax.set_zlabel('Demand of BnB')  # Set label for z-axis
ax.set_title('Demand of BnB')  # Set title for the plot

# Add a color bar which maps values to colors
fig.colorbar(surf, shrink=0.5, aspect=5)  # Add a colorbar to the plot

plt.show()  # Display the plot
