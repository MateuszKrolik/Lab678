import argparse
import json

def parse_arguments():
    parser = argparse.ArgumentParser(description="Program do konwersji danych obsługujący formaty: .xml, .json i .yml (.yaml)")
    parser.add_argument("input_file", help="Ścieżka do pliku wejściowego")
    parser.add_argument("output_file", help="Ścieżka do pliku wyjściowego")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    input_file = args.input_file
    output_file = args.output_file
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
