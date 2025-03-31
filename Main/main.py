# Import commonly used libraries

import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from Main.UI.main_window import Ui_mw_Main
from Persons.add_person import AddPerson
from Application_Login.login import LoginForm


class MainWindow(qtw.QMainWindow, Ui_mw_Main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.action_Quit.triggered.connect(self.close)
        self.action_AddPerson.triggered.connect(self.open_add_person)

        self.form = LoginForm()
        self.form.login_success.connect(self.show)
        self.form.show()

    @qtc.Slot()
    def open_add_person(self):
        self.form = AddPerson()
        self.form.exec()


if __name__ == "__main__":
    # Create application object
    app = qtw.QApplication(sys.argv)

    # Instantiate the window and show it. It is not shown by default
    window = MainWindow()

    # Exit
    sys.exit(app.exec())
