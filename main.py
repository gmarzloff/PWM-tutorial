# PWM Tutorial
# Create pulse width modulation signal, graph it,
# and see the effect of modifying parameters
import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QVBoxLayout, QMainWindow
from PWMSignal import PWMSignal

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.pwm = PWMSignal()

        self.setWindowTitle("PWM Tutorial")
        self.duty_buttons_box = QWidget()
        self.layout = QVBoxLayout()

        duty_percents = [25, 50, 75, 90]
        for duty in duty_percents:
            button = QPushButton(str(duty) + "%", self)
            button.clicked.connect(self.button_handler)
            self.layout.addWidget(button)

        self.duty_buttons_box.setLayout(self.layout)
        self.setCentralWidget(self.duty_buttons_box)

    def button_handler(self):
        # noinspection PyTypeChecker
        source: QPushButton = self.sender()
        self.pwm.update_duty_and_plot(int(source.text()[:-1]))


def main():
     app = QApplication(sys.argv)
     window = MainWindow()
     window.show()

     sys.exit(app.exec())

if __name__ == '__main__':
    main()