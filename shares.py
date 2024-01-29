# -*- coding: utf-8 -*-

# shares
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ContactDetails(object):
    def setupUi(self, ContactDetails):
        ContactDetails.setObjectName("Контакти InvestUp")
        ContactDetails.resize(600, 500)
        ContactDetails.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.Window)
        ContactDetails.setStyleSheet("QMainWindow {background-color: white; border: 2px solid black; border-radius: 10px;}")

        self.centralwidget = QtWidgets.QWidget(ContactDetails)
        self.centralwidget.setObjectName("centralwidget")

        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(20, 20, 561, 31))
        self.label_title.setStyleSheet("font: 16pt \"Arial Black\";")
        self.label_title.setText("Контакти")

        self.label_company_info = QtWidgets.QLabel(self.centralwidget)
        self.label_company_info.setGeometry(QtCore.QRect(40, 70, 600, 400))
        self.label_company_info.setStyleSheet("font: 12pt \"Arial\";")
        self.label_company_info.setText("InvestUp - твій біржовий брокер\n\n"
                                         "Адреса: м. Деражня-Подільська\n\n"
                                         "e-mail: inup_derpod@gmail.com\n\n"
                                         "Графік:\n"
                                         "Пн-Пт: 09:00 - 15:00\n"
                                         "Сб: 08:00 - 13:00\n"
                                         "Нд: вихідний\n\n"
                                         "Тел: +38(093)-132-15-74")

        self.close_button = QtWidgets.QPushButton(self.centralwidget)
        self.close_button.setGeometry(QtCore.QRect(540, 20, 41, 31))
        self.close_button.setStyleSheet("background-color: red; color: white; border: none; border-radius: 5px;")
        self.close_button.setText("X")
        self.close_button.clicked.connect(ContactDetails.close)

        ContactDetails.setCentralWidget(self.centralwidget)

        self.retranslateUi(ContactDetails)
        QtCore.QMetaObject.connectSlotsByName(ContactDetails)

        self.set_shadow_effect(ContactDetails)

    def retranslateUi(self, ContactDetails):
        _translate = QtCore.QCoreApplication.translate
        ContactDetails.setWindowTitle(_translate("ContactDetails", "Контакти InvestUp"))

    def set_shadow_effect(self, ContactDetails):
        shadow = QtWidgets.QGraphicsDropShadowEffect(self.centralwidget)
        shadow.setBlurRadius(20)
        shadow.setColor(QtGui.QColor(0, 0, 0, 150))
        shadow.setOffset(0, 0)
        self.centralwidget.setGraphicsEffect(shadow)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(2082, 1080)
        MainWindow.setStyleSheet("background-color: rgb(252, 252, 252);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 50, 1491, 381))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("img_for_project/Савчук/photo_2024-01-27_22-10-30.jpg"))
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(840, 400, 1221, 491))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("img_for_project/Савчук/photo_2024-01-27_22-09-38.jpg")) #
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 390, 821, 311))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("img_for_project/Савчук/photo_2024-01-27_22-10-42.jpg"))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 680, 281, 71))
        self.pushButton.setStyleSheet("background-color: rgb(46, 46, 46);\n"
                                      "color: rgb(245, 234, 230);\n"
                                      "font: 87 8 \"Arial Black\";")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 890, 1481, 171))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img_for_project/Савчук/photo_2024-01-27_22-10-37.jpg"))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.show_contact_details)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Отримати консультацію"))

    def show_contact_details(self):
        self.contact_details_window = QtWidgets.QMainWindow()
        self.ui_contact_details = Ui_ContactDetails()
        self.ui_contact_details.setupUi(self.contact_details_window)
        self.contact_details_window.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())
