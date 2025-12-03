import requests
from PyQt6 import QtWidgets, QtCore

API_KEY = "1999ae51283cbf54ff2765da"
BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair"

def get_exchange_rate(from_currency, to_currency, amount):
    try:
        url = f"{BASE_URL}/{from_currency}/{to_currency}/{amount}"
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200 and data["result"] == "success":
            return data["conversion_result"], data["conversion_rate"]
        else:
            return None, None
    except Exception:
        return None, None


class CurrencyExchangeDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Valutaváltó")
        self.setFixedSize(350, 300)
        self.setup_ui()
    
    def setup_ui(self):
        layout = QtWidgets.QVBoxLayout()
        
        # Összeg
        layout.addWidget(QtWidgets.QLabel("Összeg:"))
        self.entry_amount = QtWidgets.QLineEdit()
        layout.addWidget(self.entry_amount)
        
        # Erről
        layout.addWidget(QtWidgets.QLabel("Erről:"))
        self.combo_from = QtWidgets.QComboBox()
        self.combo_from.addItems(["HUF", "USD", "EUR", "GBP", "CHF"])
        self.combo_from.setCurrentText("HUF")
        layout.addWidget(self.combo_from)
        
        # Erre
        layout.addWidget(QtWidgets.QLabel("Erre:"))
        self.combo_to = QtWidgets.QComboBox()
        self.combo_to.addItems(["USD", "EUR", "GBP", "CHF", "HUF"])
        self.combo_to.setCurrentText("EUR")
        layout.addWidget(self.combo_to)
        
        # Eredmény
        self.result_label = QtWidgets.QLabel("")
        self.result_label.setStyleSheet("font-weight: bold; color: green;")
        layout.addWidget(self.result_label)
        
        # Átváltás gomb
        btn_convert = QtWidgets.QPushButton("Átváltás")
        btn_convert.setStyleSheet("background-color: #4CAF50; color: white; padding: 8px;")
        btn_convert.clicked.connect(self.perform_exchange)
        layout.addWidget(btn_convert)
        
        self.setLayout(layout)
    
    def perform_exchange(self):
        try:
            amount = float(self.entry_amount.text())
            from_c = self.combo_from.currentText()
            to_c = self.combo_to.currentText()

            result, rate = get_exchange_rate(from_c, to_c, amount)

            if result is not None:
                self.result_label.setText(f"{result:.2f} {to_c}\n(1 {from_c} = {rate} {to_c})")
                self.result_label.setStyleSheet("font-weight: bold; color: green;")
            else:
                QtWidgets.QMessageBox.critical(self, "Hiba", "Sikertelen API hívás.")
                
        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Hiba", "Kérlek, számot adj meg!")


def open_exchange_window(parent=None):
    """Convenience function to open the currency exchange dialog"""
    dialog = CurrencyExchangeDialog(parent)
    dialog.exec()
