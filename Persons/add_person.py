# Import commonly used libraries

import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from Persons.UI.add_person_dialog import Ui_d_Person


class AddPerson(qtw.QDialog, Ui_d_Person):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pb_Close.clicked.connect(self.reject)
        self.pb_Submit.clicked.connect(self.process_entry)
        self.le_FirstName.setFocus()


    @qtc.Slot()
    def process_entry(self):
        self.lb_Status.setText("New person added!")
        self.le_FirstName.clear()
        self.le_LastName.clear()

        self.le_FirstName.setFocus()


if __name__ == "__main__":
    # Create application object
    app = qtw.QApplication(sys.argv)

    # Instantiate the window and show it. It is not shown by default
    form = AddPerson()
    form.open()

    # Exit
    sys.exit(app.exec())
