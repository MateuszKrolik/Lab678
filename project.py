import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Program do konwersji danych obsługujący formaty: .xml, .json i .yml (.yaml)")
    parser.add_argument("input_file", help="Ścieżka do pliku wejściowego")
    parser.add_argument("output_file", help="Ścieżka do pliku wyjściowego")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    input_file = args.input_file
    output_file = args.output_file
    # Kontynuuj przetwarzanie danych...
