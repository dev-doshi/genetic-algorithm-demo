import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
from tkinter import Tk, Label, PhotoImage

class Analysis:
    def __init__(self):
        self.STEPS = []
        # Create an empty plot
        plt.ion()  # Turn on interactive mode
        self.fig, self.ax = plt.subplots()
        self.line, = self.ax.plot(0, 0)

    def add_steps(self, step):
        self.STEPS.append(step)

    def update(self):
        if len(self.STEPS) == 0:
            return
        self.line.set_data(len(self.STEPS), self.STEPS[len(self.STEPS)-1])
        self.ax.relim()  # Recalculate the data limits
        self.ax.autoscale_view()  # Autoscale the plot
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()


class DataPlotter:
    def __init__(self):
        self.x_data = []
        self.y_data = []

        # Initialize the plot
        self.figure, self.ax = plt.subplots()
        self.line, = self.ax.plot([], [], 'b-')

        # Set plot properties
        self.ax.set_xlim(0, 10)  # Adjust the limits according to your data
        self.ax.set_ylim(0, 100)  # Adjust the limits according to your data
        self.ax.set_xlabel('X-axis')
        self.ax.set_ylabel('Y-axis')
        self.ax.set_title('Data Plot')

    def update(self, x, y):
        # Add new data points
        self.x_data.append(x)
        self.y_data.append(y)

        # Update the line with new data
        self.line.set_data(self.x_data, self.y_data)

        # Adjust plot limits (optional)
        self.ax.relim()
        self.ax.autoscale_view()

        # Redraw the plot
        self.figure.canvas.draw()
        plt.pause(0.001)  # Add a small delay to allow the plot to refresh