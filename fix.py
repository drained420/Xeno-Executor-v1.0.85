import subprocess
import sys

# Funkcja do instalowania pakietów
def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Sprawdzamy, czy tkinter jest dostępne, jeśli nie - instalujemy
try:
    import tkinter as tk
except ImportError:
    print("Tkinter nie jest zainstalowane. Instalowanie...")
    install_package('tk')
    import tkinter as tk

# Tworzymy główne okno aplikacji
root = tk.Tk()

# Ustawiamy tytuł okna na 'Hacked'
root.title("Hacked")

# Tworzymy etykietę z komunikatem "Twój komputer został zhakowany"
label = tk.Label(root, text="Twój komputer został zhakowany!", font=("Arial", 20, "bold"), fg="red")
label.pack(padx=20, pady=20)

# Przycisk do zamknięcia okna
button = tk.Button(root, text="OK", command=root.quit, font=("Arial", 12))
button.pack(padx=10, pady=10)

# Uruchamiamy główną pętlę aplikacji
root.mainloop()
