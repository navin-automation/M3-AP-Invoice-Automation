# 🚀 M3 AP Invoice Automation Bot

A high-performance Python RPA bot for **M3 Accounting Core**, featuring ultra-fast OCR scanning and self-healing UI navigation for automated batch invoice processing in Citrix environments.

---

## 🛠️ Environment

- **Platform:** Citrix Workspace / M3 Accounting Core
- **Language:** Python 3.10+
- **Key Libraries:** PyAutoGUI, OpenCV, Tesseract OCR, Pandas

---

## ✨ Key Features

- ✅ Automatic Hotel Detection
- ✅ Vendor-Based Invoice Posting
- ✅ Ultra-Fast OCR Scanning
- ✅ Smart Error Handling
- ✅ Auto Skip for Already Posted Invoices
- ✅ Real-Time Execution Logs
- ✅ Self-Healing UI Navigation

---

# 📋 System Requirements

Before running the bot, ensure the following requirements are met:

- Windows PC with stable internet connection
- Citrix Workspace / M3 Accounting Core access
- Python 3.10 or higher
- Tesseract OCR installed
- Windows Display Scale set to **100%**
- Citrix application running on the **Primary Monitor**

---

# 🚀 Installation Guide

## 1️⃣ Install Python

Download Python from the official website:

https://www.python.org/downloads/

### ⚠️ Important

During installation, make sure to enable:

```txt
✅ Add Python to PATH
```

---

## 2️⃣ Install Tesseract OCR

Download Tesseract OCR from:

https://github.com/UB-Mannheim/tesseract/wiki

Install it in the default location:

```txt
C:\Program Files\Tesseract-OCR\
```

---

## 3️⃣ Install Required Libraries

Open Command Prompt and run:

```bash
python -m pip install playwright pyautogui pandas pytesseract opencv-python openpyxl numpy

python -m playwright install
```

---

# 📁 Required Folder Structure

Keep all bot files inside a single folder.

Example:

```txt
C:\Users\<YourUsername>\
```

### Required Files

```txt
Bot.py
get_mouse.py
AP_Invoice_Data.xlsx
/images
```

⚠️ Do NOT rename or delete PNG image files.

---

# ⚙️ First-Time Setup

## 🖼️ UI Calibration

Since Citrix rendering and resolutions vary across systems, you must capture fresh screenshots from your own machine.

### Screenshot Rules

- Use:

```txt
Windows + Shift + S
```

- Take tight and clean screenshots
- Avoid extra white space
- Save images inside the `/images` folder

---

## 🎯 Mouse Calibration

Run the calibration tool:

```bash
python get_mouse.py
```

### Steps

1. Open the M3 invoice grid
2. Hover your mouse over the empty checkbox
3. Note the displayed X-coordinate
4. Open `Bot.py`
5. Update:

```python
CHECKBOX_X_COORD = 327
```

Replace `327` with your own coordinate.

---

# 📊 Excel File Rules

Update:

```txt
AP_Invoice_Data.xlsx
```

with your daily invoice data.

### Important Rules

- Do NOT change column names
- Ensure Property Name matches the system exactly
- Ensure Vendor Name matches exactly
- Save and CLOSE Excel before running the bot

---

# 🏃 How to Run

## Start the Bot

Run:

```bash
python Bot.py
```

Immediately switch to the M3 Accounting Core window.

---

# ⚠️ Important Execution Rules

While the bot is running:

- ❌ Do NOT move the mouse
- ❌ Do NOT type on keyboard
- ❌ Do NOT minimize Citrix
- ❌ Do NOT switch applications

---

# 🛑 Emergency Stop

Move your mouse to the:

```txt
TOP LEFT CORNER
```

of the screen to instantly stop automation.

---

# 📜 Execution Logs

The terminal provides real-time logs including:

- Current Property
- Current Vendor
- Invoice Detection
- Posting Status
- Success / Failed Reports

Example:

```txt
✅ SUCCESS: Invoice Posted
⚠️ ALERT: No Pending Invoice
🚀 BATCH POSTED SUCCESSFULLY
```

---

# 🛠️ Troubleshooting

| Issue | Cause | Solution |
| :--- | :--- | :--- |
| ModuleNotFoundError | Missing Python library | Re-run pip install command |
| OpenCV Error | OpenCV not installed correctly | Run `pip install opencv-python` |
| TesseractNotFoundError | Incorrect OCR path | Verify Tesseract installation |
| Bot clicks wrong area | Display scaling issue | Set Windows Scale to 100% |
| Image Not Found | Missing PNG file | Verify image filenames |
| openpyxl Import Failed | openpyxl missing | Run `pip install openpyxl` |

---

# 🤖 Automation Capabilities

- Automatic Hotel Detection
- Vendor-Based Invoice Posting
- OCR-Based Invoice Recognition
- Smart Invoice Matching
- Auto Recovery Handling
- Real-Time Execution Dashboard

---

# 📄 License

This project is intended for internal automation and workflow optimization purposes.
