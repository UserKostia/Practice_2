from PyQt5 import QtWidgets, uic
import csv

class RegistrationForm(QtWidgets.QMainWindow):
    def __init__(self):
        super(RegistrationForm, self).__init__()
        uic.loadUi("registration_form.ui", self)

        self.register_button.clicked.connect(self.register_user)

    def register_user(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if not username or not password:
            QtWidgets.QMessageBox.warning(self, "Помилка", "Будь ласка, введіть ім'я користувача та пароль.")
            return

        with open("users.csv", mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([username, password])

        QtWidgets.QMessageBox.information(self, "Успіх", "Реєстрація пройшла успішно.")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = RegistrationForm()
    window.show()
    app.exec_()
