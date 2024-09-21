from PySide6.QtWidgets import QMainWindow, QWidget, QMessageBox

from py_man_dont_be_upset.gui.ui.ui_main_window import Ui_MainWindow
from py_man_dont_be_upset.utils import get_app_data


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent)
        self.setupUi(self)

        app_data = get_app_data()
        app_title = f"pyManDontBeUpset v{app_data['version']}"
        self.setWindowTitle(app_title)

        # connections
        self.action_About_Qt.triggered.connect(
            lambda: QMessageBox.aboutQt(self, "About Qt")
        )
        self.actionAbout_the_Game.triggered.connect(
            lambda: QMessageBox.about(self, app_title, "...")
        )