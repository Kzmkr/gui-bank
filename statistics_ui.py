from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QGroupBox
from statistics import total_expense, total_by_category, monthly_expenses, average_expense, std_expense
from db_manager import TransactionManager
from datetime import datetime


class StatisticsWidget(QtWidgets.QWidget):
    """Statistics page widget for displaying financial statistics"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.db_manager = TransactionManager()
        self.setup_ui()
    
    def setup_ui(self):
        """Setup the statistics UI"""
        main_layout = QVBoxLayout()
        
        # Title
        title = QLabel("Statisztikák")
        title.setStyleSheet("font-size: 18px; font-weight: bold;")
        main_layout.addWidget(title)
        
        # Refresh button
        refresh_btn = QPushButton("Frissítés")
        refresh_btn.clicked.connect(self.update_statistics)
        main_layout.addWidget(refresh_btn)
        
        # Overall statistics group
        overall_group = QGroupBox("Általános Statisztikák")
        overall_layout = QVBoxLayout()
        
        self.total_expense_label = QLabel("Összes kiadás: 0 Ft")
        self.avg_weekly_label = QLabel("Heti átlag: 0 Ft")
        self.avg_monthly_label = QLabel("Havi átlag: 0 Ft")
        self.std_label = QLabel("Szórás: 0 Ft")
        
        overall_layout.addWidget(self.total_expense_label)
        overall_layout.addWidget(self.avg_weekly_label)
        overall_layout.addWidget(self.avg_monthly_label)
        overall_layout.addWidget(self.std_label)
        
        overall_group.setLayout(overall_layout)
        main_layout.addWidget(overall_group)
        
        # Category statistics group
        category_group = QGroupBox("Kategóriánkénti Kiadások")
        category_layout = QVBoxLayout()
        
        self.category_labels = QLabel("Nincs adat")
        category_layout.addWidget(self.category_labels)
        
        category_group.setLayout(category_layout)
        main_layout.addWidget(category_group)
        
        # Monthly statistics group
        monthly_group = QGroupBox("Aktuális Havi Kiadások")
        monthly_layout = QVBoxLayout()
        
        self.monthly_label = QLabel("Nincs adat")
        monthly_layout.addWidget(self.monthly_label)
        
        monthly_group.setLayout(monthly_layout)
        main_layout.addWidget(monthly_group)
        
        main_layout.addStretch()
        
        self.setLayout(main_layout)
        
        # Initial update
        self.update_statistics()
    
    def update_statistics(self):
        """Update all statistics displays"""
        transactions = self.db_manager.get_all_trans()
        
        if not transactions:
            self.total_expense_label.setText("Összes kiadás: 0 Ft")
            self.avg_weekly_label.setText("Heti átlag: 0 Ft")
            self.avg_monthly_label.setText("Havi átlag: 0 Ft")
            self.std_label.setText("Szórás: 0 Ft")
            self.category_labels.setText("Nincs adat")
            self.monthly_label.setText("Nincs adat")
            return
        
        # Calculate overall statistics
        total = total_expense(transactions)
        self.total_expense_label.setText(f"Összes kiadás: {total:,.2f} Ft")
        
        weekly_avg, monthly_avg = average_expense(transactions)
        self.avg_weekly_label.setText(f"Heti átlag: {weekly_avg:,.2f} Ft")
        self.avg_monthly_label.setText(f"Havi átlag: {monthly_avg:,.2f} Ft")
        
        std = std_expense(transactions)
        self.std_label.setText(f"Szórás: {std:,.2f} Ft")
        
        # Category statistics
        category_data = total_by_category(self.db_manager.session)
        if category_data:
            category_text = ""
            for cat_name, total in category_data:
                category_text += f"{cat_name}: {-total:,.2f} Ft\n"
            self.category_labels.setText(category_text.strip())
        else:
            self.category_labels.setText("Nincs kategorizált kiadás")
        
        # Monthly statistics for current month
        now = datetime.now()
        monthly_data = monthly_expenses(self.db_manager.session, now.year, now.month)
        
        if monthly_data:
            monthly_text = f"Aktuális hónap ({now.year}-{now.month:02d}):\n"
            total_month = sum([total for _, total in monthly_data])
            monthly_text += f"Összesen: {-total_month:,.2f} Ft\n"
            monthly_text += f"Napok száma: {len(monthly_data)}"
            self.monthly_label.setText(monthly_text)
        else:
            self.monthly_label.setText("Nincs adat az aktuális hónapra")


def setup_statistics_page(parent_widget):
    """Setup the statistics page within a parent widget"""
    # Clear existing layout if any
    if parent_widget.layout():
        QtWidgets.QWidget().setLayout(parent_widget.layout())
    
    layout = QVBoxLayout()
    layout.setContentsMargins(0, 0, 0, 0)
    
    stats_widget = StatisticsWidget(parent_widget)
    layout.addWidget(stats_widget)
    parent_widget.setLayout(layout)
    
    return stats_widget
