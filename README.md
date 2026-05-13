# 🚀 M3 AP Invoice Automation Bot

A high-performance Python RPA bot for **M3 Accounting Core**, featuring ultra-fast OCR scanning and self-healing UI navigation for automated batch invoice processing in Citrix environments.

---

## 🛠️ Environment
* [cite_start]**Platform:** Citrix Workspace / M3 Accounting Core [cite: 3]
* [cite_start]**Language:** Python 3.10+ [cite: 8]
* [cite_start]**Key Libraries:** PyAutoGUI, OpenCV, Tesseract OCR, Pandas [cite: 22]

---

## ✨ Key Capabilities
* [cite_start]**Automatic Hotel Detection:** Smart navigation through property dropdowns[cite: 231].
* [cite_start]**Vendor-based Invoice Posting:** Matches vendors and posts accurately[cite: 232].
* [cite_start]**Ultra-Fast OCR:** Uses Tesseract for real-time screen scanning[cite: 9, 234].
* [cite_start]**Smart Error Handling:** Self-healing UI navigation and automatic skipping for already posted invoices[cite: 233].
* [cite_start]**Execution Dashboard:** Real-time logs in the terminal for monitoring status[cite: 163].

---

## 📋 System Requirements
To ensure smooth execution, verify the following prerequisites:
* [cite_start]**Display Scale:** Windows Display Scale must be set strictly to **100%**[cite: 10].
* [cite_start]**Monitor:** Application must run on the **Primary Monitor**[cite: 11].
* [cite_start]**Tesseract Path:** Must be installed at `C:\Program Files\Tesseract-OCR\`[cite: 18].

---

## 🚀 Setup & Installation

1. [cite_start]**Install Python:** Ensure "Add Python to PATH" is checked during installation[cite: 14].
2. [cite_start]**Install Tesseract OCR:** Download from [official link](https://github.com/UB-Mannheim/tesseract/wiki)[cite: 16].
3. **Install Dependencies:**
   ```bash
   python -m pip install playwright pyautogui pandas pytesseract opencv-python openpyxl numpy
   python -m playwright install
   
http://googleusercontent.com/immersive_entry_chip/0


## ⚙️ Configuration (One-Time Setup)

### 1. UI Calibration
Screen resolutions vary, so you must capture fresh screenshots from your machine:
* [cite_start]Take screenshots of buttons and hotel names[cite: 39].
* [cite_start]Use `Windows + Shift + S` for tight, clean captures (no extra white space)[cite: 42, 43].
* [cite_start]Save images in the `/images` folder using provided naming conventions[cite: 59].

### 2. Mouse Calibration
Use the included tool to find your specific horizontal coordinate for checkboxes:
1. [cite_start]Run `python get_mouse.py`[cite: 48].
2. [cite_start]Hover over the M3 grid checkbox and note the X-coordinate[cite: 50, 51].
3. [cite_start]Update `CHECKBOX_X_COORD` in `Bot.py`[cite: 54, 55].

---

## 🏃 How to Run

1. [cite_start]**Prepare Data:** Update `AP_Invoice_Data.xlsx` with daily tasks and close the file[cite: 135, 141].
2. [cite_start]**Auto-Login:** Run `python M3Login.py` to open Accounting Core[cite: 145].
3. [cite_start]**Trigger Bot:** Run `python Bot.py` and immediately switch to the M3 window[cite: 152, 153].
4. [cite_start]**Hands-Off:** Do **not** move the mouse or use the keyboard while the bot is running[cite: 157].

> [cite_start]**💡 Emergency Stop:** Move your mouse to the **Top-Left Corner** of the screen to halt automation[cite: 160].

---

## 🛠️ Troubleshooting Guide

| Issue | Cause | Solution |
| :--- | :--- | :--- |
| `ModuleNotFoundError` | Missing library | [cite_start]Re-run pip install command [cite: 229] |
| `TesseractNotFoundError` | Incorrect OCR path | [cite_start]Verify installation in C:\Program Files [cite: 229] |
| Bot clicks wrong area | Scaling issue | [cite_start]Change Windows Display Scale to 100% [cite: 229] |
| Image Not Found | Missing/Renamed PNG | [cite_start]Check `/images` folder for correct filenames [cite: 229] |
