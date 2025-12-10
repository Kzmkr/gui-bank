import sys
import json
import requests
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox
from db_manager import TransactionManager

# --- Generált UI kód kezdete ---
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setStyleSheet("#BalMenu{\n"
"    background-color:#00FF00;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.BalMenu = QtWidgets.QWidget(parent=self.centralwidget)
        self.BalMenu.setGeometry(QtCore.QRect(0, 0, 171, 611))
        self.BalMenu.setObjectName("BalMenu")
        self.frame = QtWidgets.QFrame(parent=self.BalMenu)
        self.frame.setGeometry(QtCore.QRect(0, 0, 171, 81))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setGeometry(QtCore.QRect(8, 15, 151, 51))
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(parent=self.BalMenu)
        self.frame_2.setGeometry(QtCore.QRect(0, 60, 171, 511))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pushButton = QtWidgets.QPushButton(parent=self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(0, 10, 181, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 70, 171, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.frame_2)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 120, 171, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.frame_2)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 180, 171, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.frame_2)
        self.pushButton_5.setGeometry(QtCore.QRect(0, 240, 171, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.frame_2)
        self.pushButton_6.setGeometry(QtCore.QRect(0, 300, 171, 41))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(parent=self.frame_2)
        self.pushButton_7.setGeometry(QtCore.QRect(0, 360, 171, 41))
        self.pushButton_7.setObjectName("pushButton_7")
        self.MainOldal = QtWidgets.QWidget(parent=self.centralwidget)
        self.MainOldal.setGeometry(QtCore.QRect(170, 0, 631, 581))
        self.MainOldal.setObjectName("MainOldal")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.MainOldal)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 10, 621, 561))
        self.stackedWidget.setObjectName("stackedWidget")
        self.KiadasBevetel = QtWidgets.QWidget()
        self.KiadasBevetel.setObjectName("KiadasBevetel")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.KiadasBevetel)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 621, 561))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.EgyszeriKesz = QtWidgets.QPushButton(parent=self.tab)
        self.EgyszeriKesz.setGeometry(QtCore.QRect(20, 250, 75, 24))
        self.EgyszeriKesz.setObjectName("EgyszeriKesz")
        self.EgyszeriOsszeg = QtWidgets.QLineEdit(parent=self.tab)
        self.EgyszeriOsszeg.setGeometry(QtCore.QRect(10, 40, 113, 21))
        self.EgyszeriOsszeg.setObjectName("EgyszeriOsszeg")
        self.EgyszeriPartner = QtWidgets.QLineEdit(parent=self.tab)
        self.EgyszeriPartner.setGeometry(QtCore.QRect(10, 100, 113, 21))
        self.EgyszeriPartner.setObjectName("EgyszeriPartner")
        self.EgyszeriKategoria = QtWidgets.QComboBox(parent=self.tab)
        self.EgyszeriKategoria.setGeometry(QtCore.QRect(20, 170, 68, 22))
        self.EgyszeriKategoria.setObjectName("EgyszeriKategoria")
        self.label_2 = QtWidgets.QLabel(parent=self.tab)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 131, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.tab)
        self.label_3.setGeometry(QtCore.QRect(20, 70, 111, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.tab)
        self.label_4.setGeometry(QtCore.QRect(20, 140, 101, 16))
        self.label_4.setObjectName("label_4")
        self.EgyszeriBevetel = QtWidgets.QRadioButton(parent=self.tab)
        self.EgyszeriBevetel.setGeometry(QtCore.QRect(10, 210, 89, 20))
        self.EgyszeriBevetel.setObjectName("EgyszeriBevetel")
        self.EgyszeriKiadas = QtWidgets.QRadioButton(parent=self.tab)
        self.EgyszeriKiadas.setGeometry(QtCore.QRect(110, 210, 89, 20))
        self.EgyszeriKiadas.setObjectName("EgyszeriKiadas")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_5 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(10, 20, 131, 16))
        self.label_5.setObjectName("label_5")
        self.RenszeresOsszeg = QtWidgets.QLineEdit(parent=self.tab_2)
        self.RenszeresOsszeg.setGeometry(QtCore.QRect(10, 40, 113, 21))
        self.RenszeresOsszeg.setObjectName("RenszeresOsszeg")
        self.label_7 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(10, 80, 111, 16))
        self.label_7.setObjectName("label_7")
        self.RendszeresPartner = QtWidgets.QLineEdit(parent=self.tab_2)
        self.RendszeresPartner.setGeometry(QtCore.QRect(10, 120, 113, 21))
        self.RendszeresPartner.setObjectName("RendszeresPartner")
        self.label_8 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(10, 170, 101, 16))
        self.label_8.setObjectName("label_8")
        self.RendszeresKategoria = QtWidgets.QComboBox(parent=self.tab_2)
        self.RendszeresKategoria.setGeometry(QtCore.QRect(20, 200, 68, 22))
        self.RendszeresKategoria.setObjectName("RendszeresKategoria")
        self.RendszeresKesz = QtWidgets.QPushButton(parent=self.tab_2)
        self.RendszeresKesz.setGeometry(QtCore.QRect(20, 290, 75, 24))
        self.RendszeresKesz.setObjectName("RendszeresKesz")
        self.RendszeresBevetel = QtWidgets.QRadioButton(parent=self.tab_2)
        self.RendszeresBevetel.setGeometry(QtCore.QRect(20, 250, 89, 20))
        self.RendszeresBevetel.setObjectName("RendszeresBevetel")
        self.RendszeresKiadas = QtWidgets.QRadioButton(parent=self.tab_2)
        self.RendszeresKiadas.setGeometry(QtCore.QRect(120, 250, 89, 20))
        self.RendszeresKiadas.setObjectName("RendszeresKiadas")
        self.dateEdit = QtWidgets.QDateEdit(parent=self.tab_2)
        self.dateEdit.setGeometry(QtCore.QRect(150, 200, 110, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.label_17 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_17.setGeometry(QtCore.QRect(140, 170, 141, 16))
        self.label_17.setObjectName("label_17")
        self.RendszeresValasztas = QtWidgets.QComboBox(parent=self.tab_2)
        self.RendszeresValasztas.setGeometry(QtCore.QRect(20, 380, 68, 22))
        self.RendszeresValasztas.setObjectName("RendszeresValasztas")
        self.label_18 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_18.setGeometry(QtCore.QRect(20, 340, 151, 16))
        self.label_18.setObjectName("label_18")
        self.RendszeresTorles = QtWidgets.QPushButton(parent=self.tab_2)
        self.RendszeresTorles.setGeometry(QtCore.QRect(20, 420, 75, 24))
        self.RendszeresTorles.setObjectName("RendszeresTorles")
        self.tabWidget.addTab(self.tab_2, "")
        self.stackedWidget.addWidget(self.KiadasBevetel)
        self.Befektetesek = QtWidgets.QWidget()
        self.Befektetesek.setObjectName("Befektetesek")
        self.BefektetesekOsszeg = QtWidgets.QLineEdit(parent=self.Befektetesek)
        self.BefektetesekOsszeg.setGeometry(QtCore.QRect(20, 40, 113, 21))
        self.BefektetesekOsszeg.setObjectName("BefektetesekOsszeg")
        self.label_6 = QtWidgets.QLabel(parent=self.Befektetesek)
        self.label_6.setGeometry(QtCore.QRect(20, 10, 111, 16))
        self.label_6.setObjectName("label_6")
        self.label_9 = QtWidgets.QLabel(parent=self.Befektetesek)
        self.label_9.setGeometry(QtCore.QRect(20, 70, 49, 16))
        self.label_9.setObjectName("label_9")
        self.BefektetesekAlacsony = QtWidgets.QRadioButton(parent=self.Befektetesek)
        self.BefektetesekAlacsony.setGeometry(QtCore.QRect(20, 100, 89, 20))
        self.BefektetesekAlacsony.setObjectName("BefektetesekAlacsony")
        self.BefektetesekKozepes = QtWidgets.QRadioButton(parent=self.Befektetesek)
        self.BefektetesekKozepes.setGeometry(QtCore.QRect(120, 100, 89, 20))
        self.BefektetesekKozepes.setObjectName("BefektetesekKozepes")
        self.BefektetesekMagas = QtWidgets.QRadioButton(parent=self.Befektetesek)
        self.BefektetesekMagas.setGeometry(QtCore.QRect(220, 100, 89, 20))
        self.BefektetesekMagas.setObjectName("BefektetesekMagas")
        self.BefektetesekRovid = QtWidgets.QRadioButton(parent=self.Befektetesek)
        self.BefektetesekRovid.setGeometry(QtCore.QRect(20, 170, 89, 20))
        self.BefektetesekRovid.setObjectName("BefektetesekRovid")
        self.BefektetesekKozepes2 = QtWidgets.QRadioButton(parent=self.Befektetesek)
        self.BefektetesekKozepes2.setGeometry(QtCore.QRect(120, 170, 89, 20))
        self.BefektetesekKozepes2.setObjectName("BefektetesekKozepes2")
        self.BefektetesekHosszu = QtWidgets.QRadioButton(parent=self.Befektetesek)
        self.BefektetesekHosszu.setGeometry(QtCore.QRect(220, 170, 89, 20))
        self.BefektetesekHosszu.setObjectName("BefektetesekHosszu")
        self.label_10 = QtWidgets.QLabel(parent=self.Befektetesek)
        self.label_10.setGeometry(QtCore.QRect(20, 130, 49, 16))
        self.label_10.setObjectName("label_10")
        self.BefektetesekKesz = QtWidgets.QPushButton(parent=self.Befektetesek)
        self.BefektetesekKesz.setGeometry(QtCore.QRect(20, 210, 75, 24))
        self.BefektetesekKesz.setObjectName("BefektetesekKesz")
        self.stackedWidget.addWidget(self.Befektetesek)
        self.Statisztika = QtWidgets.QWidget()
        self.Statisztika.setObjectName("Statisztika")
        self.stackedWidget.addWidget(self.Statisztika)
        self.Felretetel = QtWidgets.QWidget()
        self.Felretetel.setObjectName("Felretetel")
        self.FelretetelKesz = QtWidgets.QPushButton(parent=self.Felretetel)
        self.FelretetelKesz.setGeometry(QtCore.QRect(0, 70, 75, 24))
        self.FelretetelKesz.setObjectName("FelretetelKesz")
        self.label_12 = QtWidgets.QLabel(parent=self.Felretetel)
        self.label_12.setGeometry(QtCore.QRect(10, 10, 49, 16))
        self.label_12.setObjectName("label_12")
        self.FelretetelOsszeg = QtWidgets.QLineEdit(parent=self.Felretetel)
        self.FelretetelOsszeg.setGeometry(QtCore.QRect(0, 30, 113, 21))
        self.FelretetelOsszeg.setObjectName("FelretetelOsszeg")
        self.FelretetelKategoria = QtWidgets.QComboBox(parent=self.Felretetel)
        self.FelretetelKategoria.setGeometry(QtCore.QRect(10, 110, 68, 22))
        self.FelretetelKategoria.setObjectName("FelretetelKategoria")
        self.FelretetelTorles = QtWidgets.QPushButton(parent=self.Felretetel)
        self.FelretetelTorles.setGeometry(QtCore.QRect(10, 150, 101, 24))
        self.FelretetelTorles.setObjectName("FelretetelTorles")
        self.FelretetelLista = QtWidgets.QListWidget(parent=self.Felretetel)
        self.FelretetelLista.setGeometry(QtCore.QRect(170, 10, 431, 521))
        self.FelretetelLista.setObjectName("FelretetelLista")
        self.stackedWidget.addWidget(self.Felretetel)
        self.MultbeliTranzakciok = QtWidgets.QWidget()
        self.MultbeliTranzakciok.setObjectName("MultbeliTranzakciok")
        self.MultbeliOutput = QtWidgets.QTableView(parent=self.MultbeliTranzakciok)
        self.MultbeliOutput.setGeometry(QtCore.QRect(25, 111, 581, 441))
        self.MultbeliOutput.setObjectName("MultbeliOutput")
        self.MultbeliKesz = QtWidgets.QPushButton(parent=self.MultbeliTranzakciok)
        self.MultbeliKesz.setGeometry(QtCore.QRect(520, 70, 91, 24))
        self.MultbeliKesz.setObjectName("MultbeliKesz")
        self.MultbeliKategoria = QtWidgets.QComboBox(parent=self.MultbeliTranzakciok)
        self.MultbeliKategoria.setGeometry(QtCore.QRect(10, 60, 68, 22))
        self.MultbeliKategoria.setObjectName("MultbeliKategoria")
        self.label_13 = QtWidgets.QLabel(parent=self.MultbeliTranzakciok)
        self.label_13.setGeometry(QtCore.QRect(10, 20, 61, 16))
        self.label_13.setObjectName("label_13")
        self.MultbeliIdo = QtWidgets.QTimeEdit(parent=self.MultbeliTranzakciok)
        self.MultbeliIdo.setGeometry(QtCore.QRect(130, 60, 118, 22))
        self.MultbeliIdo.setObjectName("MultbeliIdo")
        self.label_14 = QtWidgets.QLabel(parent=self.MultbeliTranzakciok)
        self.label_14.setGeometry(QtCore.QRect(130, 20, 49, 16))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(parent=self.MultbeliTranzakciok)
        self.label_15.setGeometry(QtCore.QRect(300, 10, 49, 16))
        self.label_15.setObjectName("label_15")
        self.MultbeliOsszeg = QtWidgets.QLineEdit(parent=self.MultbeliTranzakciok)
        self.MultbeliOsszeg.setGeometry(QtCore.QRect(300, 50, 113, 21))
        self.MultbeliOsszeg.setObjectName("MultbeliOsszeg")
        self.stackedWidget.addWidget(self.MultbeliTranzakciok)
        self.Kategoriak = QtWidgets.QWidget()
        self.Kategoriak.setObjectName("Kategoriak")
        self.KategoriaKategoria = QtWidgets.QLineEdit(parent=self.Kategoriak)
        self.KategoriaKategoria.setGeometry(QtCore.QRect(20, 40, 113, 21))
        self.KategoriaKategoria.setObjectName("KategoriaKategoria")
        self.label_16 = QtWidgets.QLabel(parent=self.Kategoriak)
        self.label_16.setGeometry(QtCore.QRect(20, 10, 91, 16))
        self.label_16.setObjectName("label_16")
        self.KategoriaKesz = QtWidgets.QPushButton(parent=self.Kategoriak)
        self.KategoriaKesz.setGeometry(QtCore.QRect(30, 80, 75, 24))
        self.KategoriaKesz.setObjectName("KategoriaKesz")
        self.KategoriaValaszt = QtWidgets.QComboBox(parent=self.Kategoriak)
        self.KategoriaValaszt.setGeometry(QtCore.QRect(420, 20, 68, 22))
        self.KategoriaValaszt.setObjectName("KategoriaValaszt")
        self.KategoriaTorles = QtWidgets.QPushButton(parent=self.Kategoriak)
        self.KategoriaTorles.setGeometry(QtCore.QRect(400, 70, 121, 24))
        self.KategoriaTorles.setObjectName("KategoriaTorles")
        self.stackedWidget.addWidget(self.Kategoriak)
        self.DevizaValtasa = QtWidgets.QWidget()
        self.DevizaValtasa.setObjectName("DevizaValtasa")
        self.label_11 = QtWidgets.QLabel(parent=self.DevizaValtasa)
        self.label_11.setGeometry(QtCore.QRect(20, 10, 49, 16))
        self.label_11.setObjectName("label_11")
        self.DevizaOsszeg = QtWidgets.QLineEdit(parent=self.DevizaValtasa)
        self.DevizaOsszeg.setGeometry(QtCore.QRect(20, 40, 113, 21))
        self.DevizaOsszeg.setObjectName("DevizaOsszeg")
        self.DevizaMibol = QtWidgets.QComboBox(parent=self.DevizaValtasa)
        self.DevizaMibol.setGeometry(QtCore.QRect(200, 10, 68, 22))
        self.DevizaMibol.setObjectName("DevizaMibol")
        self.DevizaMibe = QtWidgets.QComboBox(parent=self.DevizaValtasa)
        self.DevizaMibe.setGeometry(QtCore.QRect(200, 40, 68, 22))
        self.DevizaMibe.setObjectName("DevizaMibe")
        self.DevizaKimenet = QtWidgets.QLabel(parent=self.DevizaValtasa)
        self.DevizaKimenet.setGeometry(QtCore.QRect(200, 80, 49, 16))
        self.DevizaKimenet.setObjectName("DevizaKimenet")
        self.DevizaKesz = QtWidgets.QPushButton(parent=self.DevizaValtasa)
        self.DevizaKesz.setGeometry(QtCore.QRect(20, 80, 75, 24))
        self.DevizaKesz.setObjectName("DevizaKesz")
        self.stackedWidget.addWidget(self.DevizaValtasa)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Aktuális egyenleg: X Ft"))
        self.pushButton.setText(_translate("MainWindow", "Kiadások/Bevétel"))
        self.pushButton_2.setText(_translate("MainWindow", "Befektetések"))
        self.pushButton_3.setText(_translate("MainWindow", "Statisztika"))
        self.pushButton_4.setText(_translate("MainWindow", "Félretétel"))
        self.pushButton_5.setText(_translate("MainWindow", "Múltbéli tranzakciók"))
        self.pushButton_6.setText(_translate("MainWindow", "Kategóriák"))
        self.pushButton_7.setText(_translate("MainWindow", "Deviza váltása"))
        self.EgyszeriKesz.setText(_translate("MainWindow", "Kész"))
        self.label_2.setText(_translate("MainWindow", "Mekkora összeg?"))
        self.label_3.setText(_translate("MainWindow", "Kinek/kitől érkezik?"))
        self.label_4.setText(_translate("MainWindow", "Milyen kategória?"))
        self.EgyszeriBevetel.setText(_translate("MainWindow", "Bevétel"))
        self.EgyszeriKiadas.setText(_translate("MainWindow", "Kiadás"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Egyszeri"))
        self.label_5.setText(_translate("MainWindow", "Mekkora összeg?"))
        self.label_7.setText(_translate("MainWindow", "Kinek/kitől érkezik?"))
        self.label_8.setText(_translate("MainWindow", "Milyen kategória?"))
        self.RendszeresKesz.setText(_translate("MainWindow", "Kész"))
        self.RendszeresBevetel.setText(_translate("MainWindow", "Bevétel"))
        self.RendszeresKiadas.setText(_translate("MainWindow", "Kiadás"))
        self.label_17.setText(_translate("MainWindow", "Mikor lesz az első utalás?"))
        self.label_18.setText(_translate("MainWindow", "Melyiket szeretnéd törölni?"))
        self.RendszeresTorles.setText(_translate("MainWindow", "Törlés"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Rendszeres"))
        self.label_6.setText(_translate("MainWindow", "Befektetési összeg"))
        self.label_9.setText(_translate("MainWindow", "Kockázat"))
        self.BefektetesekAlacsony.setText(_translate("MainWindow", "Alacsony"))
        self.BefektetesekKozepes.setText(_translate("MainWindow", "Közepes"))
        self.BefektetesekMagas.setText(_translate("MainWindow", "Magas"))
        self.BefektetesekRovid.setText(_translate("MainWindow", "Rövid"))
        self.BefektetesekKozepes2.setText(_translate("MainWindow", "Közepes"))
        self.BefektetesekHosszu.setText(_translate("MainWindow", "Hosszú"))
        self.label_10.setText(_translate("MainWindow", "Időtáv"))
        self.BefektetesekKesz.setText(_translate("MainWindow", "Kalkuláció"))
        self.FelretetelKesz.setText(_translate("MainWindow", "Felvétel"))
        self.label_12.setText(_translate("MainWindow", "Összeg:"))
        self.FelretetelTorles.setText(_translate("MainWindow", "Félretétel törlése"))
        self.MultbeliKesz.setText(_translate("MainWindow", "Keresés"))
        self.label_13.setText(_translate("MainWindow", "Kategória"))
        self.label_14.setText(_translate("MainWindow", "Idő"))
        self.label_15.setText(_translate("MainWindow", "Ár szerint"))
        self.label_16.setText(_translate("MainWindow", "Kategória neve"))
        self.KategoriaKesz.setText(_translate("MainWindow", "Hozzáadás"))
        self.KategoriaTorles.setText(_translate("MainWindow", "Kategória törlése"))
        self.label_11.setText(_translate("MainWindow", "Összeg:"))
        self.DevizaKimenet.setText(_translate("MainWindow", "TextLabel"))
        self.DevizaKesz.setText(_translate("MainWindow", "Futtatás"))
# --- Generált UI kód vége ---

# --- Saját logikai osztály ---
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.DevizaMibol.setCurrentText("HUF")
        self.ui.DevizaMibe.setCurrentText("EUR")
        self.ui.DevizaKesz.clicked.connect(self.valuta_valtas_gomb)

        self.api_key = "1999ae51283cbf54ff2765da"
        valutak = ["HUF", "EUR", "USD", "GBP", "CHF", "JPY", "PLN", "CZK", "RON"]
        self.ui.DevizaMibol.addItems(valutak)
        self.ui.DevizaMibe.addItems(valutak)

        # --- JSON betöltés induláskor ---
        self.ertek = 0
        try:
            with open("adat.json", "r", encoding="utf-8") as f:
                adat = json.load(f)
                self.ertek = int(adat.get("szam", 0))
        except (FileNotFoundError, ValueError):
            self.ertek = 0

        # QLabel frissítése a betöltött értékkel
        self.ui.label.setText(str(self.ertek) + " Ft")
        # --- JSON betöltés vége ---

        # Bal oldali gombok összekötése a lapozó függvénnyel
        # A lambda itt azért kell, hogy átadhassuk a paramétert (0, 1, 2 stb.)
        self.ui.pushButton.clicked.connect(lambda: self.lapozas(0))
        self.ui.pushButton_2.clicked.connect(lambda: self.lapozas(1))
        self.ui.pushButton_3.clicked.connect(lambda: self.lapozas(2))
        self.ui.pushButton_4.clicked.connect(lambda: self.lapozas(3))
        self.ui.pushButton_5.clicked.connect(lambda: self.lapozas(4))
        self.ui.pushButton_6.clicked.connect(lambda: self.lapozas(5))
        self.ui.pushButton_7.clicked.connect(lambda: self.lapozas(6))

        # Egyszeri gomb esemény
        self.ui.EgyszeriKesz.clicked.connect(self.egyszeri_kesz_megnyomva)

        # --- Félretétel DB és lista kezelése ---
        self.tx = TransactionManager()
        # Feltölti a listát indításkor
        self.load_savings_list()

        # Gombok összekötése
        self.ui.FelretetelKesz.clicked.connect(self.add_saving)
        self.ui.FelretetelTorles.clicked.connect(self.delete_saving)

    # Ez a függvény hiányzott az eredeti kódból, pedig a gombok hivatkoztak rá!
    def lapozas(self, index):
        self.ui.stackedWidget.setCurrentIndex(index)

    # Ezt a függvényt kiszedtem az __init__ belsejéből, hogy elérhető legyen
    def egyszeri_kesz_megnyomva(self):
        osszeg_str = self.ui.EgyszeriOsszeg.text()
        try:
            osszeg = float(osszeg_str) if osszeg_str else 0
        except ValueError:
            osszeg = 0
            
        partner = self.ui.EgyszeriPartner.text()
        kategoria = self.ui.EgyszeriKategoria.currentText()
        
        print(f"Osszeg: {osszeg}, Partner: {partner}, Kategoria: {kategoria}")

        # Mentés JSON-ba (itt az osszeg.json-t írod felül)
        self.ertek = int(osszeg) 
        try:
            with open("osszeg.json", "w", encoding="utf-8") as f:
                json.dump({"osszeg": self.ertek}, f, indent=4)
        except Exception as e:
            print(f"Hiba a mentésnél: {e}")

        # QLabel frissítése
        self.ui.label.setText(str(self.ertek) + " Ft")


        # --- EZ AZ ÚJ VALUTAVÁLTÓ FÜGGVÉNY ---
    def valuta_valtas_gomb(self):
        # 1. Adatok kiolvasása
        osszeg_str = self.ui.DevizaOsszeg.text()
        from_curr = self.ui.DevizaMibol.currentText()
        to_curr = self.ui.DevizaMibe.currentText()

        # 2. Ellenőrzés: van-e összeg beírva?
        if not osszeg_str:
            return
            
        try:
            osszeg = float(osszeg_str)
        except ValueError:
            QMessageBox.warning(self, "Hiba", "Kérlek, számot adj meg összegnek!")
            return

        # 3. API hívás összeállítása
        url = f"https://v6.exchangerate-api.com/v6/{self.api_key}/pair/{from_curr}/{to_curr}/{osszeg}"

        # 4. Lekérés az internetről
        try:
            self.ui.DevizaKimenet.setText("Számolás...")
            QtWidgets.QApplication.processEvents() # Frissíti a képernyőt
            
            response = requests.get(url)
            data = response.json()

            if data.get("result") == "success":
                converted_amount = data["conversion_result"]
                # Eredmény kiírása
                self.ui.DevizaKimenet.setText(f"{converted_amount:.2f} {to_curr}")
            else:
                self.ui.DevizaKimenet.setText("API Hiba")
                print("API Error:", data)
                
        except requests.exceptions.RequestException:
             QMessageBox.critical(self, "Hiba", "Nincs internetkapcsolat!")
             self.ui.DevizaKimenet.setText("Hiba")
        except Exception as e:
            print(e)
            self.ui.DevizaKimenet.setText("Hiba")

    # ---- Félretétel: GUI helpers ----
    def load_savings_list(self):
        """Betölti az adatbázisból a félretett tételeket és megjeleníti a listában."""
        try:
            self.ui.FelretetelLista.clear()
            items = self.tx.get_savings_as_list()
            for sid, text in items:
                item = QtWidgets.QListWidgetItem(text)
                item.setData(QtCore.Qt.ItemDataRole.UserRole, sid)
                self.ui.FelretetelLista.addItem(item)
        except Exception as e:
            print(f"Hiba a félretett tételek betöltésénél: {e}")

    def add_saving(self):
        """Gombkezelő: új félretétel mentése az adatbázisba és frissíti a listát."""
        osszeg_str = self.ui.FelretetelOsszeg.text()
        try:
            osszeg = float(osszeg_str)
        except ValueError:
            QMessageBox.warning(self, "Hiba", "Kérlek, számot adj meg összegnek!")
            return

        try:
            # determine selected category (if any)
            kategoria_name = self.ui.FelretetelKategoria.currentText()
            category_obj = None
            if kategoria_name:
                cats = self.tx.get_all_cat()
                category_obj = next((c for c in cats if c.name == kategoria_name), None)

            self.tx.save_savings(osszeg, category=category_obj)
            self.load_savings_list()
            QMessageBox.information(self, "Siker", "Félretett összeg mentve.")
            self.ui.FelretetelOsszeg.clear()
        except Exception as e:
            QMessageBox.critical(self, "Hiba", f"Nem sikerült menteni: {e}")

    def delete_saving(self):
        """Törli a kiválasztott félretételt az adatbázisból."""
        item = self.ui.FelretetelLista.currentItem()
        if not item:
            QMessageBox.information(self, "Info", "Nincs kiválasztva tétel.")
            return

        sid = item.data(QtCore.Qt.ItemDataRole.UserRole)
        try:
            # lekérjük az objektumot és töröljük
            # Directly query Savings model
            from db_manager import Savings
            saving_obj = self.tx.session.query(Savings).filter_by(id=sid).first()
            if saving_obj:
                self.tx.del_savings(saving_obj)
                self.load_savings_list()
                QMessageBox.information(self, "Siker", "Félretétel törölve.")
            else:
                QMessageBox.warning(self, "Hiba", "A kiválasztott tétel nem található.")
        except Exception as e:
            QMessageBox.critical(self, "Hiba", f"Törlés sikertelen: {e}")
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()  
    window.show()          
    sys.exit(app.exec())
