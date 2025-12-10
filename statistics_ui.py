from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QGroupBox, QTabWidget, QWidget
from statistics import total_expense, total_by_category, monthly_expenses, average_expense, std_expense
from db_manager import TransactionManager
from datetime import datetime
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

# Use dark background style for plots
try:
    plt.style.use('dark_background')
    # Customize to match our UI
    plt.rcParams['figure.facecolor'] = '#1e1e1e'
    plt.rcParams['axes.facecolor'] = '#1e1e1e'
    plt.rcParams['savefig.facecolor'] = '#1e1e1e'
    plt.rcParams['text.color'] = '#ffffff'
    plt.rcParams['axes.labelcolor'] = '#ffffff'
    plt.rcParams['xtick.color'] = '#ffffff'
    plt.rcParams['ytick.color'] = '#ffffff'
    plt.rcParams['axes.edgecolor'] = '#333333'
except:
    pass

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
        
        # Create tab widget
        tabs = QTabWidget()
        
        # Tab 1: Overview
        overview_widget = QWidget()
        overview_layout = QVBoxLayout()
        
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
        overview_layout.addWidget(overall_group)
        
        # Monthly statistics group
        monthly_group = QGroupBox("Aktuális Havi Kiadások")
        monthly_layout = QVBoxLayout()
        
        self.monthly_label = QLabel("Nincs adat")
        monthly_layout.addWidget(self.monthly_label)
        
        monthly_group.setLayout(monthly_layout)
        overview_layout.addWidget(monthly_group)
        
        overview_layout.addStretch()
        overview_widget.setLayout(overview_layout)
        tabs.addTab(overview_widget, "Összegzés")
        
        # Tab 2: Category Chart
        chart_widget = QWidget()
        chart_layout = QVBoxLayout()
        
        # Category statistics group
        category_group = QGroupBox("Kategóriánkénti Kiadások")
        category_layout = QHBoxLayout()
        
        # Left side: Category list
        self.category_labels = QLabel("Nincs adat")
        category_layout.addWidget(self.category_labels)
        
        # Right side: Pie chart
        self.figure = Figure(figsize=(6, 5), dpi=100, facecolor='#1e1e1e')
        self.canvas = FigureCanvas(self.figure)
        category_layout.addWidget(self.canvas)
        
        category_group.setLayout(category_layout)
        chart_layout.addWidget(category_group)
        chart_layout.addStretch()
        
        chart_widget.setLayout(chart_layout)
        tabs.addTab(chart_widget, "Kördiagram")
        
        # Tab 3: Monthly Histogram
        histogram_widget = QWidget()
        histogram_layout = QVBoxLayout()
        
        # Date selector group
        date_group = QGroupBox("Hónap Választása")
        date_layout = QHBoxLayout()
        
        # Year selector
        year_label = QLabel("Év:")
        self.year_spin = QtWidgets.QSpinBox()
        self.year_spin.setMinimum(2000)
        self.year_spin.setMaximum(2100)
        self.year_spin.setValue(datetime.now().year)
        self.year_spin.valueChanged.connect(self.on_date_changed)
        
        # Month selector
        month_label = QLabel("Hónap:")
        self.month_combo = QtWidgets.QComboBox()
        months = ["Január", "Február", "Március", "Április", "Május", "Június",
                  "Július", "Augusztus", "Szeptember", "Október", "November", "December"]
        self.month_combo.addItems(months)
        self.month_combo.setCurrentIndex(datetime.now().month - 1)
        self.month_combo.currentIndexChanged.connect(self.on_date_changed)
        
        date_layout.addWidget(year_label)
        date_layout.addWidget(self.year_spin)
        date_layout.addWidget(month_label)
        date_layout.addWidget(self.month_combo)
        date_layout.addStretch()
        
        date_group.setLayout(date_layout)
        histogram_layout.addWidget(date_group)
        
        # Monthly histogram group
        histogram_group = QGroupBox("Havi Kiadások Bontása")
        histogram_inner_layout = QVBoxLayout()
        
        self.histogram_figure = Figure(figsize=(6, 4), dpi=100, facecolor='#1e1e1e')
        self.histogram_canvas = FigureCanvas(self.histogram_figure)
        histogram_inner_layout.addWidget(self.histogram_canvas)
        
        histogram_group.setLayout(histogram_inner_layout)
        histogram_layout.addWidget(histogram_group)
        
        # Daily list group
        list_group = QGroupBox("Napi Kiadások Listája")
        list_layout = QVBoxLayout()
        
        self.daily_list = QtWidgets.QListWidget()
        list_layout.addWidget(self.daily_list)
        
        list_group.setLayout(list_layout)
        histogram_layout.addWidget(list_group, 1)
        
        histogram_widget.setLayout(histogram_layout)
        tabs.addTab(histogram_widget, "Havi Bontás")
        
        main_layout.addWidget(tabs)
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
            
            # Draw pie chart
            self._draw_pie_chart(category_data)
        else:
            self.category_labels.setText("Nincs kategorizált kiadás")
            self.figure.clear()
            self.canvas.draw()
        
        # Monthly statistics for current month
        now = datetime.now()
        
        # Use selected year and month from spinbox/combo if they exist
        if hasattr(self, 'year_spin') and hasattr(self, 'month_combo'):
            selected_year = self.year_spin.value()
            selected_month = self.month_combo.currentIndex() + 1
        else:
            selected_year = now.year
            selected_month = now.month
        
        monthly_data = monthly_expenses(self.db_manager.session, selected_year, selected_month)
        
        if monthly_data:
            monthly_text = f"Kiválasztott hónap ({selected_year}-{selected_month:02d}):\n"
            total_month = sum([total for _, total in monthly_data])
            monthly_text += f"Összesen: {-total_month:,.2f} Ft\n"
            monthly_text += f"Napok száma: {len(monthly_data)}"
            self.monthly_label.setText(monthly_text)
            
            # Draw histogram
            self._draw_monthly_histogram(monthly_data)
            
            # Update daily list
            self._update_daily_list(monthly_data)
        else:
            self.monthly_label.setText("Nincs adat a kiválasztott hónapra")
            self.histogram_figure.clear()
            self.histogram_canvas.draw()
            self.daily_list.clear()
    
    def _draw_pie_chart(self, category_data):
        """Draw a pie chart for category expenses"""
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        
        # Prepare data
        labels = [cat_name for cat_name, _ in category_data]
        sizes = [-total for _, total in category_data]  # Convert to positive for display
        
        # Draw pie chart without percentages
        ax.pie(sizes, startangle=90)

        # Add legend to the side to make category names readable
        ax.legend(labels, loc='center left', bbox_to_anchor=(1, 0, 0.5, 1), fontsize=9)
        ax.set_title('Kiadások kategóriánként')

        self.figure.tight_layout()
        self.canvas.draw()
    
    def _draw_monthly_histogram(self, monthly_data):
        """Draw a histogram for monthly expenses by day"""
        self.histogram_figure.clear()
        ax = self.histogram_figure.add_subplot(111)
        
        # Create a dictionary for all days in the month (1-31)
        all_days = {i: 0 for i in range(1, 32)}
        
        # Fill in the data from monthly_data
        for day_str, total in monthly_data:
            day = int(day_str)
            all_days[day] = -total  # Convert to positive for display
        
        # Prepare data for all days
        days = list(all_days.keys())
        amounts = list(all_days.values())
        
        # Draw histogram with all days (0 for days with no expenses)
        ax.bar(days, amounts, color='steelblue', edgecolor='black', width=0.8)
        ax.set_xlabel('Nap')
        ax.set_ylabel('Kiadás (Ft)')
        ax.set_title('Napi Kiadások a Hónapban')
        ax.grid(axis='y', alpha=0.3)
        
        # Format x-axis to show all days
        ax.set_xticks(range(1, 32, 1))
        ax.set_xlim(0.5, 31.5)
        
        self.histogram_canvas.draw()
    
    def on_date_changed(self):
        """Handle date change in month/year selectors"""
        year = self.year_spin.value()
        month = self.month_combo.currentIndex() + 1
        
        # Get monthly data for selected month
        monthly_data = monthly_expenses(self.db_manager.session, year, month)
        
        if monthly_data:
            # Draw histogram
            self._draw_monthly_histogram(monthly_data)
            
            # Update daily list
            self._update_daily_list(monthly_data)
        else:
            self.histogram_figure.clear()
            self.histogram_canvas.draw()
            self.daily_list.clear()
    
    def _update_daily_list(self, monthly_data):
        """Update the daily list with monthly expenses"""
        self.daily_list.clear()
        
        total_month = 0
        for day, total in monthly_data:
            total_month += total
            item_text = f"{day}. nap: {-total:,.2f} Ft"
            self.daily_list.addItem(item_text)
        
        # Add total at the end
        separator = QtWidgets.QListWidgetItem("─" * 40)
        self.daily_list.addItem(separator)
        total_item = QtWidgets.QListWidgetItem(f"Havi összesen: {-total_month:,.2f} Ft")
        self.daily_list.addItem(total_item)


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
