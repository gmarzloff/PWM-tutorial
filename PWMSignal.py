import matplotlib.pyplot as plt
import numpy as np

class PWMSignal:
    def __init__(self):
        self.duty_percent = 30  # in percent
        self.cycle_period_sec = 1.0  # seconds
        self.cycles = 10
        self.dt = 0.01

        self.t = 0
        self.y = 0

    def generate_timeseries(self):
        # adapted from https://stackoverflow.com/questions/36726384/how-to-generate-pwm-using-python
        self.t = np.arange(0, self.cycle_period_sec * self.cycles, self.dt)
        self.y = self.t % self.cycle_period_sec < self.cycle_period_sec * self.duty_percent / 100
        return self.t, self.y

    def plot_graph(self):
        plt.plot(self.t, self.y)
        plt.show()

    def update_duty_and_plot(self, new_duty):
        self.duty_percent = new_duty
        self.generate_timeseries()
        self.plot_graph()