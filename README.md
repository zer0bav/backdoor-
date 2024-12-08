
# Backdoor Toolkit

A Python-based backdoor creation and management tool for educational and ethical use only. The project consists of modules for creating, injecting, and managing backdoor connections.

---

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Usage](#usage)
  - [Creating a Backdoor](#creating-a-backdoor)
  - [Injecting and Managing](#injecting-and-managing)
  - [Listening to Backdoor Connections](#listening-to-backdoor-connections)
- [Disclaimer](#disclaimer)

---

## Features

1. **Backdoor Creation:** Generate a Python-based backdoor script with optional persistence setup.
2. **Command Execution:** Allows remote execution of commands on the target machine.
3. **Modules for Exploitation:** Additional features like location tracking, keylogging, screenshot capture, and more.
4. **Automatic Reconnections:** Automatically attempts to reconnect if the connection is lost.

---

## Requirements

Ensure the following are installed:
- Python 3.6+
- `colorama`
- `pyfiglet`
- `opencv-python`
- `requests`
- `pynput`
- `pyautogui`
- `pyaudio` 
- `wave` 
- `gps`


Install dependencies using:
```bash
pip install -r requirements.txt
```

---

## Usage

### Creating a Backdoor
1. Run the `start.py` script:
   ```bash
   python3 start.py
   ```
2. Choose the "Backdoor Create" option and provide the attacker's IP address.
3. The generated backdoor script will be saved as `project.py`.

### Injecting and Managing
1. Run the `start.py` script and choose the "Backdoor Injection" option.
2. Select additional functionalities:
   - Find Location
   - Screenshot Capture
   - Record Audio
   - Keylogging
   - Cookie Stealing
3. The required modules will execute based on the chosen options.

### Listening to Backdoor Connections
1. Choose the "Backdoor Listen" option in the main menu.
2. Select either:
   - **Netcat Listener:** Opens a Netcat listener on port 4444.
   - **Custom Listener:** Uses the `listen_backdoor()` function for managing connections.

---

## Disclaimer

This tool is intended for **educational purposes only**. Use it only in controlled environments and with appropriate permissions. Unauthorized usage of this tool is illegal and unethical.
