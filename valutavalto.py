import requests
import tkinter as tk
from tkinter import messagebox, ttk

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

def open_exchange_window(root):
    exchange_window = tk.Toplevel(root)
    exchange_window.title("Valutaváltó")
    exchange_window.geometry("350x300")

    tk.Label(exchange_window, text="Összeg:").pack(pady=5)
    entry_amount = tk.Entry(exchange_window)
    entry_amount.pack(pady=5)

    tk.Label(exchange_window, text="Erről:").pack(pady=5)
    combo_from = ttk.Combobox(exchange_window, values=["HUF", "USD", "EUR", "GBP", "CHF"])
    combo_from.set("HUF")
    combo_from.pack(pady=5)

    tk.Label(exchange_window, text="Erre:").pack(pady=5)
    combo_to = ttk.Combobox(exchange_window, values=["USD", "EUR", "GBP", "CHF", "HUF"])
    combo_to.set("EUR")
    combo_to.pack(pady=5)

    result_label = tk.Label(exchange_window, text="", font=("Arial", 10, "bold"))
    result_label.pack(pady=10)

    def perform_exchange():
        try:
            amount = float(entry_amount.get())
            from_c = combo_from.get()
            to_c = combo_to.get()

            result, rate = get_exchange_rate(from_c, to_c, amount)

            if result is not None:
                result_label.config(text=f"{result:.2f} {to_c}\n(1 {from_c} = {rate} {to_c})", fg="green")
            else:
                messagebox.showerror("Hiba", "Sikertelen API hívás.")

        except ValueError:
            messagebox.showwarning("Hiba", "Kérlek, számot adj meg!")

    tk.Button(exchange_window, text="Átváltás", command=perform_exchange, bg="#4CAF50", fg="white").pack(pady=10, fill='x', padx=20)
