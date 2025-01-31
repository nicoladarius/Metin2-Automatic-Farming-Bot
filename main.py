
import threading
import time
import keyboard
import pytesseract
import cv2
import numpy as np
import pyautogui
from python_imagesearch import imagesearch
import tkinter as tk
from tkinter import ttk, messagebox  # Import the ttk module for the Combobox


# Define the main application class
class AppControl:
    def __init__(self, root):
        self.root = root
        self.root.title("Darus e smecher")
        self.root.geometry("450x250")
        self.root.configure(bg="black")

        # Initialize the state of the app
        self.app_running = False

        # Label to show the status of the app
        self.status_label = tk.Label(root, text="APASA PE START CA NU MERGE", fg="red", font=("Arial", 16), bg="black")
        self.status_label.pack(pady=20)

        # Combobox (Drop-down List) with 2 elements
        self.options = ["45", "70", "90"]  # List of options for the Combobox
        self.combobox = ttk.Combobox(root, values=self.options, font=("Arial", 14))
        self.combobox.set("Selecteaza metinu")  # Set the default text
        self.combobox.pack(pady=10)  # Place the Combobox with some padding

        # Start button
        self.start_button = tk.Button(root, text="Start", command=self.start_app, font=("Arial", 14), bg="green")
        self.start_button.pack(pady=10)

        # Stop button
        self.stop_button = tk.Button(root, text="Stop", command=self.stop_app, font=("Arial", 14), bg="red")
        self.stop_button.pack(pady=10)

    # Function to start the app
    def start_app(self):
        selected_option = self.combobox.get()
        if selected_option == "Selecteaza metinu" or selected_option == "":
            messagebox.showerror("Prost esti", "Ce plm sa spargi daca tu nici nu alesasi metinu!")
            return

        if not self.app_running:
            self.app_running = True
            self.status_label.config(text="Acum farmez", fg="green", bg="black")
            # De aici incepe magia
            threading.Thread(target=self.background_task, args=(selected_option,), daemon=True).start()

    def background_task(self, selected_option):
        while self.app_running:
            time.sleep(1)
            self.respawn()
            self.metinFinder(selected_option)
            #self.detect_and_click_double_text()

            # Function to stop the app
    def stop_app(self):
        if self.app_running:
            self.app_running = False
            self.status_label.config(text="Acum nu farmez", fg="red", bg="black")
            # Here you can add the code to actually stop your app

    def respawn(self):
        canavar_respawn = imagesearch.imagesearch("images/respawn/respawn.png")

        canavarRespawn_x = canavar_respawn[0]
        canavarRespawn_y = canavar_respawn[1]

        if canavarRespawn_x != -1:
            print("Se gaseste butonul de respawn la:", canavar_respawn)
            pyautogui.moveTo(canavarRespawn_x + 5, canavarRespawn_y + 5)
            time.sleep(0.2)
            pyautogui.click(canavarRespawn_x + 5, canavarRespawn_y + 5)
            time.sleep(0.3)
            keyboard.press("2")
            time.sleep(0.1)
            keyboard.release("2")
            time.sleep(2.2)
            keyboard.press("3")
            time.sleep(0.1)
            keyboard.release("3")
            time.sleep(0.3)
            keyboard.press("ctrl+g")
            time.sleep(0.1)
            keyboard.release("ctrl+g")

    def metinFinder(self, selected_option):

        timpSpartMetin90 = 26

        canavar_1 = imagesearch.imagesearch("images/pietreMetin/mtn_" + selected_option + ".png")

        canavar1_x = canavar_1[0]
        canavar1_y = canavar_1[1]

        if canavar1_x != -1:
            print("Se gaseste metinul la: ", canavar_1)
            pyautogui.moveTo(canavar1_x + 30, canavar1_y + 60)
            time.sleep(0.4)
            pyautogui.click(canavar1_x + 30, canavar1_y + 60)
            time.sleep(0.4)
            keyboard.press("z")
            time.sleep(0.1)
            keyboard.release("z")
            time.sleep(timpSpartMetin90)  # setezi timpul in care sa apese pe alt metin. Timpul este in secunde
            keyboard.press("z")
            time.sleep(0.1)
            keyboard.release("z")

        else:
            keyboard.press("z")
            time.sleep(0.2)
            keyboard.release("z")
            keyboard.press("e")
            keyboard.release("e")
            keyboard.press("e")
            time.sleep(0.3)
            keyboard.release("e")
            time.sleep(0.5)
            keyboard.press("g")
            keyboard.release("g")

            keyboard.press("g")
            time.sleep(1.5)
            keyboard.release("g")
            time.sleep(0.5)
            keyboard.press("t")
            keyboard.release("t")

            keyboard.press("t")
            time.sleep(0.7)
            keyboard.release("t")
'''
    def detect_and_click_double_text(self):
        # Capturează ecranul
        screenshot = pyautogui.screenshot()
        screenshot = np.array(screenshot)
        screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)

        # Folosește pytesseract pentru a extrage textul
        data = pytesseract.image_to_data(screenshot, output_type=pytesseract.Output.DICT)

        # Găsește textul de tip pattern
        pattern = r'\b\w{2}\b'  # Caută pattern-ul de 2 caractere (litere/cifre)
        found_positions = []

        for i in range(len(data['text'])):
            text = data['text'][i]
            if len(text) == 2:  # Textul are exact 2 caractere
                found_positions.append((data['left'][i], data['top'][i], data['width'][i], data['height'][i]))

        # Dacă s-au găsit 2 instanțe ale textului, apasă click pe ele
        if len(found_positions) >= 2:
            for pos in found_positions[:2]:  # Limitează la primele 2 găsite
                x, y, w, h = pos
                pyautogui.moveTo(x + w // 2, y + h // 2)
                pyautogui.click()
'''

# Main function to run the tkinter loop
if __name__ == "__main__":
    root = tk.Tk()
    app = AppControl(root)
    root.mainloop()
