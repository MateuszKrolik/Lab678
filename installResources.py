# installResources.py

import subprocess

# Lista komponentów do zainstalowania przez PIP
required_packages = [
    "xmltodict",
    "pyyaml",
    "pyqt5",
]

# Instalacja komponentów
for package in required_packages:
    subprocess.call(["pip", "install", package])
