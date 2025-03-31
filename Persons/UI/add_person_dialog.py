# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_person_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.8.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QFont, QIcon)
from PySide6.QtWidgets import (QFormLayout, QGridLayout,
                               QGroupBox, QLabel, QLineEdit, QPushButton,
                               QSizePolicy, QSpacerItem, QWidget)


class Ui_d_Person(object):
    def setupUi(self, d_Person):
        if not d_Person.objectName():
            d_Person.setObjectName(u"d_Person")
        d_Person.setWindowModality(Qt.WindowModality.ApplicationModal)
        d_Person.resize(460, 246)
        font = QFont()
        font.setPointSize(12)
        d_Person.setFont(font)
        icon = QIcon()
        icon.addFile(u":/Main/smile.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        d_Person.setWindowIcon(icon)
        self.gridLayout = QGridLayout(d_Person)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pb_Close = QPushButton(d_Person)
        self.pb_Close.setObjectName(u"pb_Close")
        icon1 = QIcon()
        icon1.addFile(u":/Buttons/close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_Close.setIcon(icon1)
        self.pb_Close.setAutoDefault(False)

        self.gridLayout.addWidget(self.pb_Close, 2, 2, 1, 1)

        self.pb_Submit = QPushButton(d_Person)
        self.pb_Submit.setObjectName(u"pb_Submit")
        icon2 = QIcon()
        icon2.addFile(u":/Buttons/check.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_Submit.setIcon(icon2)

        self.gridLayout.addWidget(self.pb_Submit, 2, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 0, 1, 1)

        self.gb_Person = QGroupBox(d_Person)
        self.gb_Person.setObjectName(u"gb_Person")
        self.gb_Person.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.formLayout = QFormLayout(self.gb_Person)
        self.formLayout.setObjectName(u"formLayout")
        self.l_FirstName = QLabel(self.gb_Person)
        self.l_FirstName.setObjectName(u"l_FirstName")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.l_FirstName)

        self.le_FirstName = QLineEdit(self.gb_Person)
        self.le_FirstName.setObjectName(u"le_FirstName")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.le_FirstName)

        self.l_LastName = QLabel(self.gb_Person)
        self.l_LastName.setObjectName(u"l_LastName")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.l_LastName)

        self.le_LastName = QLineEdit(self.gb_Person)
        self.le_LastName.setObjectName(u"le_LastName")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.le_LastName)


        self.gridLayout.addWidget(self.gb_Person, 0, 0, 1, 3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 3)

        self.lb_Status = QLabel(d_Person)
        self.lb_Status.setObjectName(u"lb_Status")

        self.gridLayout.addWidget(self.lb_Status, 3, 0, 1, 3)

        QWidget.setTabOrder(self.le_FirstName, self.le_LastName)
        QWidget.setTabOrder(self.le_LastName, self.pb_Submit)
        QWidget.setTabOrder(self.pb_Submit, self.pb_Close)

        self.retranslateUi(d_Person)

        QMetaObject.connectSlotsByName(d_Person)
    # setupUi

    def retranslateUi(self, d_Person):
        d_Person.setWindowTitle(QCoreApplication.translate("d_Person", u"Sample Application", None))
        self.pb_Close.setText(QCoreApplication.translate("d_Person", u"Close", None))
        self.pb_Submit.setText(QCoreApplication.translate("d_Person", u"Submit", None))
        self.gb_Person.setTitle(QCoreApplication.translate("d_Person", u"Add Person", None))
        self.l_FirstName.setText(QCoreApplication.translate("d_Person", u"First Name", None))
        self.l_LastName.setText(QCoreApplication.translate("d_Person", u"Last Name", None))
        self.lb_Status.setText("")
    # retranslateUi

