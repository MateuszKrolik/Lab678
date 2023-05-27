from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Program z interfejsem użytkownika")
        self.layout = QVBoxLayout()
        self.label = QLabel("Ładowanie pliku:")
        self.line_edit = QLineEdit()
        self.button = QPushButton("Uruchom")
        self.button.clicked.connect(self.process_data)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.line_edit)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

    def process_data(self):
        input_file = self.line_edit.text()
        # Kontynuuj przetwarzanie danych...

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
