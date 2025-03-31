# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QGridLayout, QGroupBox,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)
import Icons_rc

class Ui_w_LoginForm(object):
    def setupUi(self, w_LoginForm):
        if not w_LoginForm.objectName():
            w_LoginForm.setObjectName(u"w_LoginForm")
        w_LoginForm.resize(499, 245)
        font = QFont()
        font.setPointSize(12)
        w_LoginForm.setFont(font)
        icon = QIcon()
        icon.addFile(u":/Main/smile.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        w_LoginForm.setWindowIcon(icon)
        self.gridLayout = QGridLayout(w_LoginForm)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pb_Cancel = QPushButton(w_LoginForm)
        self.pb_Cancel.setObjectName(u"pb_Cancel")
        icon1 = QIcon()
        icon1.addFile(u":/Buttons/close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_Cancel.setIcon(icon1)

        self.gridLayout.addWidget(self.pb_Cancel, 2, 1, 1, 1)

        self.pb_OK = QPushButton(w_LoginForm)
        self.pb_OK.setObjectName(u"pb_OK")
        icon2 = QIcon()
        icon2.addFile(u":/Buttons/check.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_OK.setIcon(icon2)

        self.gridLayout.addWidget(self.pb_OK, 2, 0, 1, 1)

        self.groupBox = QGroupBox(w_LoginForm)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.le_UserID = QLineEdit(self.groupBox)
        self.le_UserID.setObjectName(u"le_UserID")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.le_UserID)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.le_Pass = QLineEdit(self.groupBox)
        self.le_Pass.setObjectName(u"le_Pass")
        self.le_Pass.setEchoMode(QLineEdit.EchoMode.Password)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.le_Pass)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 2)

        self.lb_Message = QLabel(w_LoginForm)
        self.lb_Message.setObjectName(u"lb_Message")

        self.gridLayout.addWidget(self.lb_Message, 3, 0, 1, 2)

        QWidget.setTabOrder(self.le_UserID, self.le_Pass)
        QWidget.setTabOrder(self.le_Pass, self.pb_OK)
        QWidget.setTabOrder(self.pb_OK, self.pb_Cancel)

        self.retranslateUi(w_LoginForm)

        QMetaObject.connectSlotsByName(w_LoginForm)
    # setupUi

    def retranslateUi(self, w_LoginForm):
        w_LoginForm.setWindowTitle(QCoreApplication.translate("w_LoginForm", u"Sample Application", None))
        self.pb_Cancel.setText(QCoreApplication.translate("w_LoginForm", u"Cancel", None))
        self.pb_OK.setText(QCoreApplication.translate("w_LoginForm", u"OK", None))
        self.groupBox.setTitle(QCoreApplication.translate("w_LoginForm", u"Welcome! Please Login", None))
        self.label.setText(QCoreApplication.translate("w_LoginForm", u"User ID", None))
        self.label_2.setText(QCoreApplication.translate("w_LoginForm", u"Password", None))
        self.lb_Message.setText("")
    # retranslateUi

