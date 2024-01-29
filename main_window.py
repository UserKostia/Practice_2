# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
# from registration import RegistrationDialog
import PersonalAccount
import InvestInShares
import requests
import shares
import graphics
import ipo
# from db import User
# from registration import RegistrationDialog

# db = User('database.db')


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        # self.register_button = QtWidgets.QPushButton(self.centralwidget)
        # self.register_button.setGeometry(QtCore.QRect(20, 400, 150, 30))
        # self.register_button.setObjectName("register_button")
        # self.register_button.setText("Зареєструватися")
        # self.register_button.clicked.connect(self.show_registration_screen)

        # -*- coding: utf-8 -*-
        class Ui_MainWindow(object):
            def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(1920, 1080)
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setEnabled(True)
                self.centralwidget.setObjectName("centralwidget")

                self.view_all_actives_btn = QtWidgets.QPushButton(self.centralwidget)
                self.view_all_actives_btn.setGeometry(QtCore.QRect(30, 10, 360, 100))
                font = QtGui.QFont()
                font.setPointSize(13)
                self.view_all_actives_btn.setFont(font)
                self.view_all_actives_btn.setStyleSheet("background-color: rgb(102, 153, 204);")
                self.view_all_actives_btn.setObjectName("view_all_actives_btn")

                self.investment_in_shares_btn = QtWidgets.QPushButton(self.centralwidget)
                self.investment_in_shares_btn.setGeometry(QtCore.QRect(780, 10, 360, 100))
                font = QtGui.QFont()
                font.setPointSize(16)
                self.investment_in_shares_btn.setFont(font)
                self.investment_in_shares_btn.setStyleSheet("background-color: rgb(102, 153, 204);")
                self.investment_in_shares_btn.setObjectName("investment_in_shares_btn")

                self.personal_portfoli_btn = QtWidgets.QPushButton(self.centralwidget)
                self.personal_portfoli_btn.setGeometry(QtCore.QRect(1530, 10, 360, 100))
                font = QtGui.QFont()
                font.setPointSize(16)
                self.personal_portfoli_btn.setFont(font)
                self.personal_portfoli_btn.setStyleSheet("background-color: rgb(102, 153, 204);")
                self.personal_portfoli_btn.setObjectName("personal_portfoli_btn")

                self.shares_btn = QtWidgets.QPushButton(self.centralwidget)
                self.shares_btn.setGeometry(QtCore.QRect(30, 130, 901, 81))
                font = QtGui.QFont()
                font.setPointSize(20)
                self.shares_btn.setFont(font)
                self.shares_btn.setStyleSheet("background-color: rgb(153, 204, 255);")
                self.shares_btn.setObjectName("shares_btn")

                self.IPO_btn_2 = QtWidgets.QPushButton(self.centralwidget)
                self.IPO_btn_2.setGeometry(QtCore.QRect(990, 130, 901, 81))
                font = QtGui.QFont()
                font.setPointSize(20)
                self.IPO_btn_2.setFont(font)
                self.IPO_btn_2.setStyleSheet("background-color: rgb(153, 204, 255);")
                self.IPO_btn_2.setObjectName("shares_btn_2")

                self.main_background_img = QtWidgets.QLabel(self.centralwidget)
                self.main_background_img.setGeometry(QtCore.QRect(-4, -7, 1921, 1091))
                self.main_background_img.setText("")
                self.main_background_img.setPixmap(QtGui.QPixmap(
                    "img_for_project/Слісаренко/photo_2024-01-26_21-09-45.jpg"))
                self.main_background_img.setScaledContents(True)
                self.main_background_img.setObjectName("main_background_img")

                self.news_textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
                self.news_textBrowser.setGeometry(QtCore.QRect(30, 230, 901, 821))
                self.news_textBrowser.setObjectName("news_textBrowser")

                self.news_textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
                self.news_textBrowser_2.setGeometry(QtCore.QRect(990, 230, 901, 821))
                self.news_textBrowser_2.setObjectName("news_textBrowser_2")

                self.main_background_img.raise_()
                self.view_all_actives_btn.raise_()
                self.investment_in_shares_btn.raise_()
                self.personal_portfoli_btn.raise_()
                self.shares_btn.raise_()
                self.IPO_btn_2.raise_()
                self.news_textBrowser.raise_()
                self.news_textBrowser_2.raise_()
                MainWindow.setCentralWidget(self.centralwidget)
                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

                self.news_timer = QTimer(MainWindow)
                self.news_timer.timeout.connect(self.update_news)
                url = "https://api.polygon.io/v2/reference/news?apiKey=RiLOAG5fD1G5rXExyqKUiUdO9pbKWswy"

                response = requests.get(url)
                print(response)
                res = response.json()
                i = 0
                self.news_textBrowser.append(str(res.get('results')[0].get('title') + '\n'))
                self.news_textBrowser.append(str(res.get('results')[1].get('title') + '\n'))
                self.news_textBrowser.append(str(res.get('results')[2].get('title') + '\n'))
                self.news_textBrowser.append(str(res.get('results')[3].get('title') + '\n'))
                self.news_textBrowser.append(str(res.get('results')[4].get('title') + '\n'))
                self.news_textBrowser.append(str(res.get('results')[5].get('title') + '\n'))
                self.news_textBrowser.append(str(res.get('results')[6].get('title') + '\n'))
                self.news_textBrowser.append(str(res.get('results')[7].get('title') + '\n'))
                self.news_textBrowser.append(str(res.get('results')[8].get('title') + '\n'))
                self.news_textBrowser.append(str(res.get('results')[9].get('title') + '\n'))

                self.news_textBrowser_2.append(str(res.get('results')[6].get('title') + '\n'))
                self.news_textBrowser_2.append(str(res.get('results')[9].get('title') + '\n'))
                self.news_textBrowser_2.append(str(res.get('results')[8].get('title') + '\n'))
                self.news_textBrowser_2.append(str(res.get('results')[4].get('title') + '\n'))
                self.news_textBrowser_2.append(str(res.get('results')[7].get('title') + '\n'))
                self.news_textBrowser_2.append(str(res.get('results')[0].get('title') + '\n'))
                self.news_textBrowser_2.append(str(res.get('results')[1].get('title') + '\n'))
                self.news_textBrowser_2.append(str(res.get('results')[3].get('title') + '\n'))
                self.news_textBrowser_2.append(str(res.get('results')[5].get('title') + '\n'))
                self.news_textBrowser_2.append(str(res.get('results')[2].get('title') + '\n'))

                self.news_timer.start(600000)

                self.view_all_actives_btn.clicked.connect(self.show_assets_window)
                self.shares_btn.clicked.connect(self.show_shares_window)
                self.IPO_btn_2.clicked.connect(self.show_IPO_window)
                self.personal_portfoli_btn.clicked.connect(self.show_personal_account_window)
                self.investment_in_shares_btn.clicked.connect(self.investment_in_shares_window)

            def update_news(self):
                try:
                    url = "https://api.polygon.io/v2/reference/news?apiKey=RiLOAG5fD1G5rXExyqKUiUdO9pbKWswy"

                    # querystring = {"uuid": "9803606d-a324-3864-83a8-2bd621e6ccbd", "region": "US"}
                    #
                    # headers = {
                    #     "X-RapidAPI-Key": "ba6b78cb49mshc8ec9669246f923p1b37e5jsn1ad13622518c",
                    #     "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
                    # }
                    # print(url)

                    response = requests.get(url)
                    print(response)
                    res = response.json()

                    self.news_textBrowser.append(str(res.get('results')[0].get('title')))
                except requests.exceptions.RequestException as e:
                    print(f"Error fetching news: {e}")
                    self.news_textBrowser.clear()
                    self.news_textBrowser.append("Error fetching news. Please try again later.")

            # def show_registration_screen(self):
            #     registration_dialog = RegistrationDialog(db)
            #     if registration_dialog.exec_() == QtWidgets.QDialog.Accepted:
            #         # Реєстрація пройшла успішно, виконайте додаткові дії, якщо потрібно
            #         print("Реєстрація пройшла успішно")
            #
            #         # Приховати форму реєстрації
            #         registration_dialog.hide()
            #
            #         # Показати основне вікно
            #         MainWindow.show()

            def show_assets_window(self):
                self.assets_window = QtWidgets.QMainWindow()
                self.ui_shares = shares.Ui_MainWindow()
                self.ui_shares.setupUi(self.assets_window)
                self.assets_window.show()

            def show_shares_window(self):
                self.graphics_window = QtWidgets.QMainWindow()
                self.ui_graphics = graphics.Ui_MainWindow()
                self.ui_graphics.setupUi(self.graphics_window)
                self.graphics_window.show()

            def show_IPO_window(self):
                self.IPO_window = QtWidgets.QMainWindow()
                self.ui_ipo = ipo.Ui_MainWindow()
                self.ui_ipo.setupUi(self.IPO_window)
                self.IPO_window.show()

            def show_personal_account_window(self):
                self.account_window = QtWidgets.QMainWindow()
                self.ui_account = PersonalAccount.Ui_MainWindow()
                self.ui_account.setupUi(self.account_window)
                self.account_window.show()

            def investment_in_shares_window(self):
                self.investment = QtWidgets.QMainWindow()
                self.ui_investment = InvestInShares.Ui_MainWindow()
                self.ui_investment.setupUi(self.investment)
                self.investment.show()

            def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
                self.view_all_actives_btn.setText(_translate("MainWindow", "Перегляд всіх активів"))
                self.investment_in_shares_btn.setText(_translate("MainWindow", "Інвестиції в акції"))
                self.personal_portfoli_btn.setText(_translate("MainWindow", "Кабінет"))
                self.shares_btn.setText(_translate("MainWindow", "Що таке акції"))
                self.IPO_btn_2.setText(_translate("MainWindow", "Що таке IPO"))

        if __name__ == "__main__":
            import sys
            app = QtWidgets.QApplication(sys.argv)
            Window = QtWidgets.QMainWindow()
            ui = Ui_MainWindow()
            ui.setupUi(Window)
            Window.show()
            sys.exit(app.exec_())

    # def show_registration_screen(self):
    #     registration_dialog = RegistrationDialog(db)
    #     if registration_dialog.exec_() == QtWidgets.QDialog.Accepted:
    #         # Реєстрація пройшла успішно, виконайте додаткові дії, якщо потрібно
    #         print("Реєстрація пройшла успішно")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    sys.exit(app.exec_())
