
# PWM Tutorial
# Create pulse width modulation signal, graph it,
# and see the effect of modifying parameters

from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QVBoxLayout
import numpy as np
import matplotlib.pyplot as plt


class PWMSignal:
    def __init__(self):
        self.duty_percent = 30 # in percent
        self.cycle_period_sec = 1.0 # seconds
        self.cycles = 10
        self.dt = 0.01
        
        self.t = 0
        self.y = 0
        
    def generate_timeseries(self):
        # adapted from https://stackoverflow.com/questions/36726384/how-to-generate-pwm-using-python
        self.t = np.arange(0,self.cycle_period_sec * self.cycles, self.dt)
        self.y = self.t % self.cycle_period_sec < self.cycle_period_sec * self.duty_percent/100
        return self.t, self.y
    
    def plot_graph(self):
        plt.plot(self.t, self.y)
        plt.show()
        
def setup():
    print("PWM Tutorial")
    pwm = PWMSignal()
    pwm.generate_timeseries()
    pwm.plot_graph()
    

if __name__ == '__main__':
    app = QApplication([])
    window = QWidget()
    layout = QVBoxLayout()
    layout.addWidget(QPushButton('25%'))
    layout.addWidget(QPushButton('50%'))
    layout.addWidget(QPushButton('75%'))
    layout.addWidget(QPushButton('90%'))
    window.setLayout(layout)
    window.show()
    
    setup()
    app.exec_()
