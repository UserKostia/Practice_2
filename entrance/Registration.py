# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Registration.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Registration_Form(object):
    def setupUi(self, Registration_Form):
        Registration_Form.setObjectName("Registration_Form")
        Registration_Form.resize(334, 161)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Registration_Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.Login_line = QtWidgets.QLineEdit(Registration_Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Login_line.setFont(font)
        self.Login_line.setObjectName("Login_line")
        self.verticalLayout.addWidget(self.Login_line)
        self.Password_line = QtWidgets.QLineEdit(Registration_Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Password_line.setFont(font)
        self.Password_line.setObjectName("Password_line")
        self.verticalLayout.addWidget(self.Password_line)
        self.Sign_Up_button = QtWidgets.QPushButton(Registration_Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Sign_Up_button.setFont(font)
        self.Sign_Up_button.setObjectName("Sign_Up_button")
        self.verticalLayout.addWidget(self.Sign_Up_button)
        self.Already_registered_button = QtWidgets.QPushButton(Registration_Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Already_registered_button.setFont(font)
        self.Already_registered_button.setObjectName("Already_registered_button")
        self.verticalLayout.addWidget(self.Already_registered_button)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Registration_Form)
        QtCore.QMetaObject.connectSlotsByName(Registration_Form)

    def retranslateUi(self, Registration_Form):
        _translate = QtCore.QCoreApplication.translate
        Registration_Form.setWindowTitle(_translate("Registration_Form", "Registration"))
        self.Login_line.setPlaceholderText(_translate("Registration_Form", "Login..."))
        self.Password_line.setPlaceholderText(_translate("Registration_Form", "Password..."))
        self.Sign_Up_button.setText(_translate("Registration_Form", "Sign Up"))
        self.Already_registered_button.setText(_translate("Registration_Form", "Already registered"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Registration_Form = QtWidgets.QWidget()
    ui = Ui_Registration_Form()
    ui.setupUi(Registration_Form)
    Registration_Form.show()
    sys.exit(app.exec_())