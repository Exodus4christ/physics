import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# User inputs for initial height & velocity
h0 = float(input("Enter the initial height (m): "))
v0 = float(input("Enter the initial velocity (m/s): "))

# Constants
g = 9.81 # gravitational acceleration (m/s^2)
t_end = 2*v0/g # final time of free fall (s)
dt = 0.01 # time step (s)

# Arrays to store the data points for plotting
t_data = np.arange(0, t_end+dt, dt)
x_data = np.zeros(len(t_data))
v_data = np.zeros(len(t_data))

# Equations of motion
for i in range(len(t_data)-1):
    x_data[i+1] = x_data[i] + v_data[i]*dt
    v_data[i+1] = v_data[i] - g*dt

# Plot the v(t) & x(t) graphs
plt.plot(t_data, x_data, label='Position (m)')
plt.plot(t_data, v_data, label='Velocity (m/s)')
plt.xlabel('Time (s)')
plt.ylabel('v(t) & x(t)')
plt.legend()
plt.show()

# Create the animation
fig, ax = plt.subplots()
t_line, = ax.plot([], [], label='Time (s)')
x_line, = ax.plot([], [], label='Position (m)')
v_line, = ax.plot([], [], label='Velocity (m/s)')

ax.set_xlim(0, t_end)
ax.set_ylim(-2*h0, 2*h0)

def update(num):
    t_line.set_data(t_data[:num+1], t_data[:num+1])
    x_line.set_data(t_data[:num+1], x_data[:num+1])
    v_line.set_data(t_data[:num+1], v_data[:num+1])
    return t_line, x_line, v_line

ani = FuncAnimation(fig, update, frames=len(t_data), interval=50, blit=True)

# Save the animation as a GIF file
ani.save('free_fall_animation.gif', writer='pillow', fps=20)

plt.show()