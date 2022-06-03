# PWM Tutorial
# Create pulse width modulation signal, graph it,
# and see the effect of modifying parameters

# plotting based on tutorial https://www.pythonguis.com/tutorials/plotting-matplotlib/
import sys
import matplotlib
matplotlib.use('Qt5Agg')

from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QMainWindow
import pyqtgraph as pg

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure
# from layout_colorwidget import Color

from PWMSignal import PWMSignal

class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width,height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.pwm = PWMSignal()

        self.setWindowTitle("PWM Tutorial")
        # self.duty_buttons_box = QWidget()

        main_layout = QHBoxLayout()
        duty_buttons_layout = QVBoxLayout()
        main_layout.addLayout(duty_buttons_layout)

        duty_percents = [25, 50, 75, 90]
        for duty in duty_percents:
            button = QPushButton(str(duty) + "%", self)
            button.clicked.connect(self.button_handler)
            duty_buttons_layout.addWidget(button)

        # plot using PyQtGraph
        self.graphWidget = pg.PlotWidget()
        times = [0, 1, 2, 3, 4]
        temps = [10, 1, 20, 3, 40]
        pen = pg.mkPen(color=(0, 0, 200), width=3)
        self.graphWidget.setBackground('w')
        self.graphWidget.plot(times,temps,pen=pen)

        main_layout.addWidget(self.graphWidget)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

        # plot_canvas = MplCanvas(self, width=5, height=4, dpi=100)
        # plot_canvas.axes.plot(

        self.show()

    def button_handler(self):
        # noinspection PyTypeChecker
        source: QPushButton = self.sender()
        # self.pwm.update_duty_and_plot(int(source.text()[:-1]))


def main():
     app = QApplication(sys.argv)
     window = MainWindow()

     sys.exit(app.exec())

if __name__ == '__main__':
    main()