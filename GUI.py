import platform, os, subprocess
from SaveVault import SavesManager
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, QStringListModel)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QLabel,
    QListView, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTextEdit,
    QWidget, QMessageBox)
import sys

class Ui_SaveVault(object):
    def setupUi(self, SaveVault):
        self.window = SaveVault
        self.SaveManager = SavesManager()
        self.PROFILES = self.SaveManager.Get_profiles()

        if not SaveVault.objectName():
            SaveVault.setObjectName(u"SaveVault")
        SaveVault.resize(608, 455)
        self.Show_in_explorer = QAction(SaveVault)
        self.Show_in_explorer.setObjectName(u"Show_in_explorer")
        self.AboutProgram = QAction(SaveVault)
        self.AboutProgram.setObjectName(u"About_program")
        self.actionDelete = QAction(SaveVault)
        self.actionDelete.setObjectName(u"actionDelete")
        self.centralwidget = QWidget(SaveVault)
        self.centralwidget.setObjectName(u"centralwidget")
        self.SavesList = QListView(self.centralwidget)
        self.SavesList.setObjectName(u"SavesList")
        self.SavesList.setGeometry(QRect(10, 30, 291, 341))

        self.saves_model = QStringListModel()
        self.SavesList.setModel(self.saves_model)

        self.SavesList.setStyleSheet(u"background-color: rgb(48, 48, 48);")
        self.CreateSave = QPushButton(self.centralwidget)
        self.CreateSave.setObjectName(u"CreateSave")
        self.CreateSave.setGeometry(QRect(310, 30, 281, 41))
        self.CreateSave.setStyleSheet(u"background-color: rgb(26, 95, 180);")
        self.Load_save = QPushButton(self.centralwidget)
        self.Load_save.setObjectName(u"Load_save")
        self.Load_save.setGeometry(QRect(310, 80, 281, 41))
        self.Load_save.setStyleSheet(u"background-color: rgb(38, 162, 105);")
        self.Delete_save = QPushButton(self.centralwidget)
        self.Delete_save.setObjectName(u"Delete_save")
        self.Delete_save.setGeometry(QRect(310, 130, 281, 41))
        self.Delete_save.setStyleSheet(u"background-color: rgb(165, 29, 45);")
        self.Reset_game = QPushButton(self.centralwidget)
        self.Reset_game.setObjectName(u"Reset_game")
        self.Reset_game.setGeometry(QRect(310, 180, 281, 41))
        self.Reset_game.setStyleSheet(u"background-color: rgb(165, 29, 45);")
        self.Show_in_explorer_2 = QPushButton(self.centralwidget)
        self.Show_in_explorer_2.setObjectName(u"Show_in_explorer_2")
        self.Show_in_explorer_2.setGeometry(QRect(10, 380, 291, 31))
        self.saves_label = QLabel(self.centralwidget)
        self.saves_label.setObjectName(u"saves_label")
        self.saves_label.setGeometry(QRect(9, 5, 291, 21))
        self.Name_panel = QGroupBox(self.centralwidget)
        self.Name_panel.setObjectName(u"Name_panel")
        self.Name_panel.setEnabled(True)
        self.Name_panel.setGeometry(QRect(310, 280, 291, 80))
        self.name_textedit = QTextEdit(self.Name_panel)
        self.name_textedit.setObjectName(u"name_textedit")
        self.name_textedit.setGeometry(QRect(0, 20, 291, 31))
        self.ok_btn = QPushButton(self.Name_panel)
        self.ok_btn.setObjectName(u"ok_btn")
        self.ok_btn.setGeometry(QRect(-6, 50, 301, 31))
        self.ok_btn.setStyleSheet(u"background-color: rgb(38, 162, 105);")
        self.Name_panel_2 = QGroupBox(self.centralwidget)
        self.Name_panel_2.setObjectName(u"Name_panel_2")
        self.Name_panel_2.setEnabled(True)
        self.Name_panel_2.setGeometry(QRect(310, 230, 291, 50))
        self.GameProfileCombobox = QComboBox(self.Name_panel_2)
        self.GameProfileCombobox.setObjectName(u"GameProfileCombobox")
        self.GameProfileCombobox.setGeometry(QRect(0, 20, 291, 31))
        SaveVault.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(SaveVault)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 608, 21))
        self.menuProfiles = QMenu(self.menubar)
        self.menuProfiles.setObjectName(u"menuProfiles")
        self.About = QMenu(self.menubar)
        self.About.setObjectName(u"About")
        SaveVault.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(SaveVault)
        self.statusbar.setObjectName(u"statusbar")
        SaveVault.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuProfiles.menuAction())
        self.menubar.addAction(self.About.menuAction())
        self.menuProfiles.addAction(self.Show_in_explorer)
        self.About.addAction(self.AboutProgram)

        self.retranslateUi(SaveVault)
        self.update_ui()

        self.CreateSave.clicked.connect(self.create_save_clicked)
        self.Load_save.clicked.connect(self.load_save_clicked)
        self.Delete_save.clicked.connect(self.delete_save_clicked)
        self.Reset_game.clicked.connect(self.reset_game_clicked)
        self.Show_in_explorer_2.clicked.connect(self.show_in_explorer_clicked)
        self.ok_btn.clicked.connect(self.ok_button_clicked)
        self.Show_in_explorer.triggered.connect(self.show_in_explorer_menu_triggered)
        self.About.triggered.connect(self.about_click)
        QMetaObject.connectSlotsByName(SaveVault)
        

    def retranslateUi(self, SaveVault):
        SaveVault.setWindowTitle(QCoreApplication.translate("SaveVault", u"SaveVault", None))
        self.Show_in_explorer.setText(QCoreApplication.translate("SaveVault", u"Show in explorer", None))
        self.AboutProgram.setText(QCoreApplication.translate("SaveVault", u"About program", None))
        self.actionDelete.setText(QCoreApplication.translate("SaveVault", u"Delete", None))
        self.CreateSave.setText(QCoreApplication.translate("SaveVault", u"Create save", None))
        self.Load_save.setText(QCoreApplication.translate("SaveVault", u"Load save", None))
        self.Delete_save.setText(QCoreApplication.translate("SaveVault", u"Delete save", None))
        self.Reset_game.setText(QCoreApplication.translate("SaveVault", u"Reset game", None))
        self.Show_in_explorer_2.setText(QCoreApplication.translate("SaveVault", u"Show in explorer", None))
        self.saves_label.setText(QCoreApplication.translate("SaveVault", u"Saves", None))
        self.Name_panel.setTitle(QCoreApplication.translate("SaveVault", u"Name", None))
        self.ok_btn.setText(QCoreApplication.translate("SaveVault", u"OK", None))
        self.Name_panel_2.setTitle(QCoreApplication.translate("SaveVault", u"Game profile", None))
        self.menuProfiles.setTitle(QCoreApplication.translate("SaveVault", u"Profiles", None))
        self.About.setTitle(QCoreApplication.translate("SaveVault", u"About", None))
        

    def update_ui(self):
        self.Name_panel.hide()
        self.update_saves_list()
        for profile in self.PROFILES:
            self.GameProfileCombobox.addItem(profile)

    def show_in_explorer_menu_triggered(self):
        self.open_in_explorer("PROFILES")

    def about_click(self):
        QMessageBox.information(self.window, "About", "SaveVault by Adil-Master \nTG: @RazrabotchikProgramm \nGithub: https://github.com/Adil-Master\n\nv1.0 (03.2026)")

    def create_save_clicked(self):
        self.Name_panel.show()
        
    def load_save_clicked(self):
        item = self.SavesList.selectedIndexes()[0]
        name = self.saves_model.data(item, Qt.DisplayRole)
        self.SaveManager.Load_save(name)
        
    def delete_save_clicked(self):
        item = self.SavesList.selectedIndexes()[0]
        name = self.saves_model.data(item, Qt.DisplayRole)
        self.SaveManager.Delete_save(name)
        self.update_saves_list()
        
    def reset_game_clicked(self):
        item = self.SavesList.selectedIndexes()[0]
        name = self.saves_model.data(item, Qt.DisplayRole)
        self.SaveManager.Reset(name)
    
    def show_in_explorer_clicked(self):
        self.open_in_explorer("SAVES")

    def open_in_explorer(self, folder_path):
        system = platform.system()

        try:
            if system == "Windows":
                os.startfile(folder_path)
                
            elif system == "Linux":
                commands = [
                    ['xdg-open', folder_path],
                    ['nautilus', folder_path],
                    ['dolphin', folder_path],
                    ['thunar', folder_path],
                    ['nemo', folder_path],
                    ['pcmanfm', folder_path] 
                ]
                
                for cmd in commands:
                    try:
                        subprocess.run(cmd, check=True)
                        break
                    except (subprocess.SubprocessError, FileNotFoundError):
                        continue
                else:
                    print("Не удалось открыть файловый менеджер в Linux")
                    return False
                    
            elif system == "Darwin":  # macOS
                subprocess.run(['open', folder_path], check=True)
                
            else:
                print(f"Неподдерживаемая ОС: {system}")
                return False
                
            return True
        
        except Exception as e:
            print(f"Ошибка при открытии папки: {e}")
            return False
        
    def ok_button_clicked(self):
        name = self.name_textedit.toPlainText()
        self.Name_panel.hide()
        self.SaveManager.Create_save(name, self.GameProfileCombobox.currentText())
        self.update_saves_list()

    def update_saves_list(self):
        self.saves_model.setStringList(self.SaveManager.Get_saves_names())
        

class SaveVaultWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_SaveVault()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SaveVaultWindow()
    window.show()
    sys.exit(app.exec())