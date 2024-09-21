import asyncio

from PySide6.QtWidgets import QMainWindow, QMessageBox, QWidget

from py_man_dont_be_upset.gui.ui.ui_main_window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent)
        self.setupUi(self)

        app_title = "pyManDontBeUpset"
        self.setWindowTitle(app_title)

        self.background_tasks = set()

        # initialize starting field
        reset_task = asyncio.ensure_future(self.reset_field())
        self.background_tasks.add(reset_task)
        reset_task.add_done_callback(self.background_tasks.discard)

        # connections
        self.action_About_Qt.triggered.connect(
            lambda: QMessageBox.aboutQt(self, "About Qt")
        )
        self.actionAbout_the_Game.triggered.connect(
            lambda: QMessageBox.about(self, app_title, "...")
        )

    async def hide_dices_and_counter_label(self):
        self.pushButton_dice_yellow.setVisible(False)
        self.pushButton_dice_green.setVisible(False)
        self.pushButton_dice_red.setVisible(False)
        self.pushButton_dice_blue.setVisible(False)
        self.label_counter.setVisible(False)

    async def reset_field(self):
        await self.hide_dices_and_counter_label()
