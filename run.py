import sys
import typing
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QStackedWidget
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, uic

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main_window.ui', self)
        self.take_sample_btn.clicked.connect(self.show_take_sample_screen)
        self.train_model_btn.clicked.connect(self.show_train_model_screen)
        self.calibrate_btn.clicked.connect(self.show_calibrate_screen)
        self.get_prediction_btn.clicked.connect(self.show_get_prediction_screen)
        self.pick_a_model_btn.clicked.connect(self.show_pick_a_model_screen)
        self.quit_btn.clicked.connect(self.show_close_screen)

    def show_take_sample_screen(self):
        self.take_sample_screen = TakeSampleScreen()
        self.take_sample_screen.show()
        self.close()

    def show_train_model_screen(self):
        self.train_model_screen = TrainModelScreen()
        self.train_model_screen.show()
        self.close()


    def show_calibrate_screen(self):
        self.calibrate_screen = CalibrateScreen()
        self.calibrate_screen.show()
        self.close()

    def show_get_prediction_screen(self):
        self.get_prediction_screen = GetPredictionScreen()
        self.get_prediction_screen.show()
        self.close()

    def show_pick_a_model_screen(self):
        self.pick_a_model_screen = PickAModel()
        self.pick_a_model_screen.show()
        self.close()


    def show_close_screen(self):
        app.quit()

class TakeSampleScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("take_sample_screen.ui", self)
        self.backButton.clicked.connect(self.show_main_window)

    def show_main_window(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()

class TrainModelScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("model_training_screen.ui", self)
        self.backButton.clicked.connect(self.show_main_window)

    def show_main_window(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()


class CalibrateScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("calibrate_screen.ui", self)
        self.backButton.clicked.connect(self.show_main_window)
        self.backButton_2.clicked.connect(self.show_main_window)

    def show_main_window(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()

class GetPredictionScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("prediction_screen.ui", self)
        self.backButton.clicked.connect(self.show_main_window)

    def show_main_window(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()

class PickAModel(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("pick_model.ui", self)
        self.backButton.clicked.connect(self.show_main_window)

    def show_main_window(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
