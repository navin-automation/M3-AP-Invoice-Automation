# 🚀 M3 AP Invoice Automation Bot

A high-performance Python RPA bot for **M3 Accounting Core**, featuring ultra-fast OCR scanning and self-healing UI navigation for automated batch invoice processing in Citrix environments.

---

## 🛠️ Environment

- **Platform:** Citrix Workspace / M3 Accounting Core  
- **Language:** Python 3.10+  
- **Key Libraries:** PyAutoGUI, OpenCV, Tesseract OCR, Pandas  

---

## ✨ Key Capabilities

- **Automatic Hotel Detection:** Smart navigation through property dropdowns  
- **Vendor-Based Invoice Posting:** Matches vendors and posts invoices accurately  
- **Ultra-Fast OCR:** Uses Tesseract for real-time screen scanning  
- **Smart Error Handling:** Self-healing UI navigation with automatic skipping for already posted invoices  
- **Execution Dashboard:** Real-time terminal logs for monitoring status  

---

## 📋 System Requirements

To ensure smooth execution, verify the following prerequisites:

- **Display Scale:** Windows Display Scale must be set strictly to **100%**  
- **Monitor:** Application must run on the **Primary Monitor**  
- **Tesseract Path:** Must be installed at:

```txt
C:\Program Files\Tesseract-OCR\
```

---

## 🚀 Setup & Installation

### 1. Install Python

Ensure **"Add Python to PATH"** is checked during installation.

---

### 2. Install Tesseract OCR

Download from the official repository:

https://github.com/UB-Mannheim/tesseract/wiki

---

### 3. Install Dependencies

Run the following commands:

```bash
python -m pip install playwright pyautogui pandas pytesseract opencv-python openpyxl numpy

python -m playwright install
```

---

## ⚙️ Configuration (One-Time Setup)

### 1. UI Calibration

Screen resolutions vary, so you must capture fresh screenshots from your machine.

- Take screenshots of:
  - Buttons
  - Hotel names
  - Required UI elements

- Use:

```txt
Windows + Shift + S
```

for tight and clean captures (avoid extra white space).

- Save all images inside the:

```txt
/images
```

folder using the required naming conventions.

---

### 2. Mouse Calibration

Use the included utility tool to find the correct horizontal checkbox coordinate.

#### Steps

1. Run:

```bash
python get_mouse.py
```

2. Hover over the M3 grid checkbox.

3. Note the displayed **X-coordinate**.

4. Update:

```python
CHECKBOX_X_COORD
```

inside:

```txt
Bot.py
```

---

## 🏃 How to Run

### Step 1 — Prepare Data

Update:

```txt
AP_Invoice_Data.xlsx
```

with the latest invoice data and close the file before running the bot.

---

### Step 2 — Auto Login

Run:

```bash
python M3Login.py
```

This will automatically open M3 Accounting Core.

---

### Step 3 — Trigger Bot

Run:

```bash
python Bot.py
```

Immediately switch to the M3 window after starting the bot.

---

### Step 4 — Hands-Free Execution

⚠️ Do **NOT**:

- Move the mouse
- Use the keyboard
- Minimize the application

while the bot is running.

---

## 🛑 Emergency Stop

Move your mouse to the **Top-Left Corner** of the screen to instantly stop the automation.

---

## 🛠️ Troubleshooting Guide

| Issue | Cause | Solution |
| :--- | :--- | :--- |
| `ModuleNotFoundError` | Missing Python library | Re-run the pip install command |
| `TesseractNotFoundError` | Incorrect OCR installation path | Verify installation inside `C:\Program Files\Tesseract-OCR\` |
| Bot clicks wrong area | Display scaling issue | Change Windows Display Scale to **100%** |
| Image Not Found | Missing or renamed PNG file | Check filenames inside the `/images` folder |

---

## 📌 Notes

- Best performance is achieved on stable Citrix sessions.
- Avoid changing monitor resolution after calibration.
- Always keep required PNG assets updated for accurate image detection.

---

## 📄 License

This project is intended for internal automation and workflow optimization purposes.
