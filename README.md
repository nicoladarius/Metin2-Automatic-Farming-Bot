# Metin2 Farm Bot - Auto Farming Tool

This **Metin2 Farm Bot** is an automated tool designed to help you efficiently farm in Metin2 without manual intervention. Built using Python and a variety of libraries such as `pyautogui`, `keyboard`, `pytesseract`, and `imagesearch`, this bot automates several routine in-game tasks like respawning, finding Metin stones, and performing key actions like using skills or breaking stones.

With an easy-to-use GUI, you can start and stop the bot with just a click. Customize your farming session by choosing different Metin stone types, and let the bot handle the repetitive tasks while you focus on other aspects of the game.

Whether you’re a casual player looking to farm efficiently or just exploring automation in gaming, this bot can help streamline your Metin2 experience.

## Disclaimer

This bot is intended for personal use and educational purposes. Use it at your own risk, as it may violate the terms of service of Metin2 or other games. Always ensure you are in compliance with the game's rules and regulations.

## Features

- **Respawn Automation**: The bot automatically detects and clicks the respawn button, ensuring your character is always ready to farm again after completing a task.
- **Metin Stone Farming**: It locates Metin stones on the screen (based on the selected level), clicks on them, and performs actions like using the "Z" key to break the stones.
- **Customizable Settings**: The user can choose from different Metin stone types (45, 70, 90) via a combobox dropdown menu to specify which type of stones they want to farm.
- **Smart Key Pressing**: The bot presses specific keys (like "Z", "E", "G", and "T") to perform various in-game actions like breaking stones, moving, and using skills.
- **Easy Start and Stop Controls**: Using the intuitive Tkinter-based GUI, you can start and stop the bot at any time. The status is clearly displayed on the screen, with an option to stop the app or continue farming.
- **Auto-Farming**: Once the app is started, the bot continuously runs in the background, executing farming tasks automatically based on the selected configuration.

## How It Works

1. **Starting the Bot**: After selecting the desired Metin stone type (45, 70, or 90) from the dropdown, simply click the "Start" button to begin farming.
2. **Farming Process**:
   - The bot searches for the respawn button and clicks it if detected.
   - Once respawned, it looks for Metin stones and performs actions like breaking them with the "Z" key.
   - The bot repeats this process continuously, farming the stones based on the configured time intervals.
3. **Stopping the Bot**: To stop the bot, click the "Stop" button. The bot will halt all farming activities, and the status will update accordingly.

## Requirements

- **Python 3.x**: You need Python 3.x installed to run the bot.
- **Dependencies**: Install the required libraries using `pip`:
  ```bash
  pip install pyautogui keyboard pytesseract numpy opencv-python python-imagesearch pillow

  
Certainly! Here's the full description in README.md format for your Metin2 Farm Bot:

markdown
Copiază
Editează
# Metin2 Farm Bot - Auto Farming Tool

This **Metin2 Farm Bot** is an automated tool designed to help you efficiently farm in Metin2 without manual intervention. Built using Python and a variety of libraries such as `pyautogui`, `keyboard`, `pytesseract`, and `imagesearch`, this bot automates several routine in-game tasks like respawning, finding Metin stones, and performing key actions like using skills or breaking stones.

With an easy-to-use GUI, you can start and stop the bot with just a click. Customize your farming session by choosing different Metin stone types, and let the bot handle the repetitive tasks while you focus on other aspects of the game.

Whether you’re a casual player looking to farm efficiently or just exploring automation in gaming, this bot can help streamline your Metin2 experience.

## Features

- **Respawn Automation**: The bot automatically detects and clicks the respawn button, ensuring your character is always ready to farm again after completing a task.
- **Metin Stone Farming**: It locates Metin stones on the screen (based on the selected level), clicks on them, and performs actions like using the "Z" key to break the stones.
- **Customizable Settings**: The user can choose from different Metin stone types (45, 70, 90) via a combobox dropdown menu to specify which type of stones they want to farm.
- **Smart Key Pressing**: The bot presses specific keys (like "Z", "E", "G", and "T") to perform various in-game actions like breaking stones, moving, and using skills.
- **Easy Start and Stop Controls**: Using the intuitive Tkinter-based GUI, you can start and stop the bot at any time. The status is clearly displayed on the screen, with an option to stop the app or continue farming.
- **Auto-Farming**: Once the app is started, the bot continuously runs in the background, executing farming tasks automatically based on the selected configuration.

## How It Works

1. **Starting the Bot**: After selecting the desired Metin stone type (45, 70, or 90) from the dropdown, simply click the "Start" button to begin farming.
2. **Farming Process**:
   - The bot searches for the respawn button and clicks it if detected.
   - Once respawned, it looks for Metin stones and performs actions like breaking them with the "Z" key.
   - The bot repeats this process continuously, farming the stones based on the configured time intervals.
3. **Stopping the Bot**: To stop the bot, click the "Stop" button. The bot will halt all farming activities, and the status will update accordingly.

## Requirements

- **Python 3.x**: You need Python 3.x installed to run the bot.
- **Dependencies**: Install the required libraries using `pip`:
  ```bash
  pip install pyautogui keyboard pytesseract numpy opencv-python python-imagesearch pillow

## How to Run
- Clone or download the project repository.
- Make sure all dependencies are installed (as mentioned above).
- Run the script and open the Tkinter window. Select your desired Metin stone type, and click "Start" to begin farming.
- To stop the bot, simply press the "Stop" button.
