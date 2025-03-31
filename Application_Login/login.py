# Import commonly used libraries

import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

# Import widget object from the generated (from .ui) .py file
from Application_Login.UI.login_window import Ui_w_LoginForm


# Import the widget via class. Because the widget inherits from QWidget, QWidget has to be imported
# as well as Ui_w_LoginForm
class LoginForm(qtw.QWidget, Ui_w_LoginForm):

    # Create custom signal to emit if the login is successful
    login_success = qtc.Signal()
    def __init__(self):
        # call the initialization method of the parent and run automatically
        super().__init__()
        # call the method inside Ui_w_LoginForm that runs the UI
        self.setupUi(self)

        # Adding functionality
        self.pb_Cancel.clicked.connect(self.close)
        self.pb_OK.clicked.connect(self.process_login)

    @qtc.Slot()
    def process_login(self):
        if self.le_UserID.text() == "admin" and self.le_Pass.text() == "password":
            # If the login is successful, emit the signal and close the window
            self.login_success.emit()
            self.close()
        else:
            self.lb_Message.setText("Login Incorrect!")


if __name__ == "__main__":
    # Create application object
    app = qtw.QApplication(sys.argv)

    # Instantiate the window and show it. It is not shown by default
    window = LoginForm()
    window.show()

    # Exit
    sys.exit(app.exec())
