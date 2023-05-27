import argparse
import json
import yaml
import xml.etree.ElementTree as ET
import ui
from PyQt5.QtCore import QRunnable, QThreadPool, QTimer



if __name__ == "__main__":
    app = QApplication([])
    window = ui.MainWindow()
    window.show()
    app.exec_()
    # Wczytanie danych z pliku JSON
    try:
        with open(input_file, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"Plik {input_file} nie został odnaleziony.")
        exit(1)
    except json.JSONDecodeError as e:
        print(f"Błąd podczas wczytywania pliku {input_file}: {e}")
        exit(1)

    # Kontynuuj przetwarzanie danych...

    # Zapis danych do pliku JSON
    try:
        with open(output_file, "w") as file:
            json.dump(data, file, indent=4)
        print(f"Dane zapisano do pliku {output_file} w formacie JSON.")
    except IOError:
        print(f"Błąd podczas zapisywania danych do pliku {output_file}.")
        exit(1)
    # Wczytanie danych z pliku YAML
    try:
        with open(input_file, "r") as file:
            data = yaml.safe_load(file)
    except FileNotFoundError:
        print(f"Plik {input_file} nie został odnaleziony.")
        exit(1)
    except yaml.YAMLError as e:
        print(f"Błąd podczas wczytywania pliku {input_file}: {e}")
        exit(1)

    # Kontynuuj przetwarzanie danych...
   
    # Zapis danych do pliku YAML
    try:
        with open(output_file, "w") as file:
            yaml.dump(data, file)
        print(f"Dane zapisano do pliku {output_file} w formacie YAML.")
    except IOError:
        print(f"Błąd podczas zapisywania danych do pliku {output_file}.")
        exit(1)
    # Wczytanie danych z pliku XML
    try:
        tree = ET.parse(input_file)
        root = tree.getroot()
    except FileNotFoundError:
        print(f"Plik {input_file} nie został odnaleziony.")
        exit(1)
    except ET.ParseError as e:
        print(f"Błąd podczas wczytywania pliku {input_file}: {e}")
        exit(1)

    # Kontynuuj przetwarzanie danych...
    
    # Zapis danych do pliku XML
    try:
        tree.write(output_file)
        print(f"Dane zapisano do pliku {output_file} w formacie XML.")
    except IOError:
        print(f"Błąd podczas zapisywania danych do pliku {output_file}.")
        exit(1)
class DataProcessingTask(QRunnable):
    def __init__(self, input_file, output_file):
        super().__init__()
        self.input_file = input_file
        self.output_file = output_file

    def run(self):
        # Wczytywanie danych z pliku i przetwarzanie...

        # Symulacja czasochłonnego zadania
        QTimer.singleShot(3000, self.save_data)

    def save_data(self):
        # Zapis danych do pliku

        # Zakończ zadanie
        QThreadPool.globalInstance().releaseThread()
