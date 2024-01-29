import sys
import warnings
from PyQt5 import QtWidgets, QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT
import matplotlib.pyplot as plt
import yfinance as yf


class StockWidget(QtWidgets.QWidget):
    def __init__(self, symbol, price, parent=None):
        super(StockWidget, self).__init__(parent)
        self.symbol = symbol
        self.price = price

        self.init_ui()

    def init_ui(self):
        layout = QtWidgets.QHBoxLayout()

        symbol_label = QtWidgets.QLabel(self.symbol)
        price_label = QtWidgets.QLabel(f"Price: {self.price}")

        layout.addWidget(symbol_label)
        layout.addWidget(price_label)

        self.setLayout(layout)


class StockChartWidget(QtWidgets.QWidget):
    def __init__(self):
        super(StockChartWidget, self).__init__()

        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar2QT(self.canvas, self)

        self.init_ui()

    def init_ui(self):
        layout = QtWidgets.QVBoxLayout(self)

        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)

    def show_stock_chart(self, symbol, prices):
        try:
            self.ax.clear()
            dates = prices.index.to_pydatetime()
            self.ax.plot(dates, prices.values, label=symbol, color='red', marker='o')
            self.ax.legend()
            self.ax.set_xlabel('Date')
            self.ax.set_ylabel('Price')

            # Annotate the last data point with the exact price
            last_date = dates[-1]
            last_price = prices.values[-1]
            self.ax.annotate(f'{symbol}: {last_price:.2f}', xy=(last_date, last_price),
                             xytext=(last_date, last_price * 0.95), ha='left', va='top',
                             arrowprops=dict(facecolor='black', arrowstyle='->'))

            self.canvas.draw()
        except Exception as e:
            print(f"Error in show_stock_chart: {e}")
            import traceback
            traceback.print_exc()


class StockApp(QtWidgets.QWidget):
    def __init__(self):
        super(StockApp, self).__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Stock Viewer')
        self.setGeometry(100, 100, 1980, 1080)  # Set the screen resolution to 1980x1080

        self.stock_list_widget = QtWidgets.QListWidget(self)
        self.stock_list_widget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.stock_list_widget.itemClicked.connect(self.show_stock_chart)

        self.stock_chart_widget = StockChartWidget()

        self.layout = QtWidgets.QHBoxLayout()
        self.layout.addWidget(self.stock_list_widget)
        self.layout.addWidget(self.stock_chart_widget)
        self.setLayout(self.layout)

        self.populate_stock_list()

    def populate_stock_list(self):
        stock_symbols = ['AAPL', 'GOOGL', 'AMZN', 'MSFT', 'TSLA', 'FB', 'NFLX', 'NVDA', 'BA', 'INTC',
                         'CSCO', 'WMT', 'CVX', 'XOM', 'GS', 'PG', 'KO', 'PEP', 'DIS', 'VZ',
                         'T', 'UNH', 'MCD', 'JNJ', 'WFC', 'BAC', 'V', 'GS', 'CAT', 'GE', 'GM',
                         'F', 'MMM', 'HD', 'AAP', 'GOOG', 'AMT', 'IBM', 'AABA', 'GS', 'JPM',
                         'HD', 'BA', 'UTX', 'CSCO', 'WMT', 'CVX', 'XOM']

        # Add more unique stock symbols to make a total of 50
        additional_symbols = ['AMAT', 'ABBV', 'ABB', 'ABT', 'ACN', 'ADBE', 'ADI', 'ADM', 'ADP', 'ADS']

        stock_symbols.extend(additional_symbols[:50 - len(stock_symbols)])

        for symbol in stock_symbols:
            item = QtWidgets.QListWidgetItem(f" {symbol}")
            self.stock_list_widget.addItem(item)

    def show_stock_chart(self, item):
        symbol = item.text().strip()

        stock_data = get_stock_data(symbol)

        if stock_data is not None:
            self.stock_chart_widget.show_stock_chart(symbol, stock_data['Close'])
        else:
            print("Failed to retrieve stock data.")


def get_stock_data(symbol):
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            stock = yf.Ticker(symbol)
            data = stock.history(period='1d')
        return data

    except Exception as e:
        print(f"Error: {e}")
        return None


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 100, 200, 50))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Show StockApp")
        self.pushButton.clicked.connect(self.show_stock_app)

        MainWindow.setCentralWidget(self.centralwidget)

    def show_stock_app(self):
        self.stock_app_window = QtWidgets.QWidget()
        self.ui_stock_app = StockApp()
        self.ui_stock_app.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui_main_window = Ui_MainWindow()
    MainWindow = QtWidgets.QMainWindow()
    ui_main_window.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
