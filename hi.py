import subprocess
import ctypes
import webbrowser
import tkinter as tk
from itertools import cycle

# --- 1. Setup für das fliegende Fenster ---
root = tk.Tk()
root.overrideredirect(True)      # Rahmenlos
root.attributes("-topmost", True) # Immer im Vordergrund
root.config(bg='black')
root.attributes("-transparentcolor", 'black') # Hintergrund unsichtbar

label_text = "Hey tobias du verschmierter"
colors = cycle(['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'cyan'])
label = tk.Label(root, text=label_text, font=("Arial", 45, "bold"), bg='black')
label.pack()

# Startposition und Fluggeschwindigkeit
x, y = 100, 100
dx, dy = 7, 7 # Geschwindigkeit (Pixel pro Schritt)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

def move_text():
    global x, y, dx, dy
    x += dx
    y += dy
    
    # Abprallen an den Bildschirmrändern
    # (Die Werte 600 und 100 sind Schätzungen für die Breite/Höhe des Textes)
    if x + 650 >= screen_width or x <= 0:
        dx = -dx
    if y + 80 >= screen_height or y <= 0:
        dy = -dy
        
    root.geometry(f"+{x}+{y}")
    label.config(fg=next(colors))
    
    # Die Funktion ruft sich selbst alle 20ms auf (Endlosschleife)
    root.after(20, move_text)

# --- 2. Chaos-Funktionen ---
def start_chaos():
    # 2x CMD mit Verzeichnis-Scan
    for _ in range(1):
        subprocess.Popen('start cmd /k dir /s', shell=True)
    
    # 2x Taschenrechner
    for _ in range(1):
        subprocess.Popen('calc')
    
    # YouTube Musik/Video
    webbrowser.open("https://www.youtube.com/watch?v=x5cCl6eh47g")
    
    # Die nummerierten Fehlermeldungen (nacheinander)
    root.after(2000, lambda: ctypes.windll.user32.MessageBoxW(0, "Systemmeldung (1)", "Fehler", 0x10))
    root.after(3500, lambda: ctypes.windll.user32.MessageBoxW(0, "Systemmeldung (2)", "Fehler", 0x10))

# --- Start ---
move_text()          # Startet das Fliegen
root.after(500, start_chaos) # Startet CMD, Calc und Web nach 0,5 Sek.

# Beenden mit der Esc-Taste
root.bind('<Escape>', lambda e: root.destroy())

root.mainloop()