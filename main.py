# PWM Tutorial
# Create pulse width modulation signal, graph it,
# and see the effect of modifying parameters

# plotting based on tutorial https://www.pythonguis.com/tutorials/plotting-matplotlib/
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QMainWindow
from PWMSignal import PWMSignal
import pyqtgraph as pg

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.pwm = PWMSignal()
        self.graph_title = "PWM signal at "+str(self.pwm.cycles)+" Hz"
        self.setWindowTitle("PWM Tutorial")

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
        pen = pg.mkPen(color=(0, 0, 200), width=3)
        self.graphWidget.setBackground('w')
        self.generate_graph_title(duty_percents[0])
        style = {'color':'blue', 'font-size': '15px'}
        self.graphWidget.setLabel('left', 'Voltage', **style)
        self.graphWidget.setLabel('bottom', 'time', **style)
        self.graphWidget.showGrid(x=True, y=True)

        data = self.pwm.generate_timeseries()
        self.line_reference = self.graphWidget.plot(data[0], data[1], pen=pen)

        main_layout.addWidget(self.graphWidget)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)
        self.show()

    def generate_graph_title(self, duty):
        new_title = "PWM signal at "+str(self.pwm.cycles)+" Hz and " + str(duty) + "% duty"
        self.graphWidget.setTitle(new_title, size="15pt")

    def button_handler(self):
        # noinspection PyTypeChecker
        source: QPushButton = self.sender()
        duty = int(source.text()[:-1])
        data = self.pwm.generate_timeseries(duty)
        self.generate_graph_title(duty)
        self.line_reference.setData(data[0], data[1])


def main():
     app = QApplication(sys.argv)
     window = MainWindow()

     sys.exit(app.exec())

if __name__ == '__main__':
    main()