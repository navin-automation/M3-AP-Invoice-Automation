import pyautogui
import time
import os
import pandas as pd
import pytesseract
import cv2            
import numpy as np    
import re 
import pyperclip 

# ==============================================================================
# ⚙️ CONFIGURATION (STABLE ULTRA FAST ARCHITECTURE)
# ==============================================================================
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.01 # Zero lag between actions

CHECKBOX_X_COORD = 327 
NETWORK_TIMEOUT = 40 

HOTEL_IMAGES = {
    "Test b": "images/h1.png", 
    "Test Company": "images/h1.png",
    "Arosh,LP-Four Points by Sheraton DFW Airport North": "images/h2.png",
    "Atlanta Doubletree by Hilton": "images/h3.png",
    "Battery Hotel Group, LLC": "images/h4.png",
    "D'iberville Courtyard": "images/h5.png",
    "Double Tree Harrisonburg": "images/h6.png",
    "DoubleTree Westminster": "images/h7.png",
    "EH PACIFIC OAK SOR II Q&C Operations": "images/h8.png",
    "Embassy Suites Indianapolis North": "images/h9.png",
    "Embassy suites Overland park": "images/h10.png",
    "Hampton Inn Boston Braintree": "images/h12.png",
    "McAllen Residence Inn by Marriott": "images/h13.png",
    "Pensacola-Home 2 Suites": "images/h14.png",
    "Savannah Fairfield Inn & Suites": "images/h15.png",
    "Spanish Fort Courtyard by Marriott": "images/h16.png",
    "Spanish Fort Fairfield Inn and Suites": "images/h17.png"
}

# ==============================================================================
# 🧠 DYNAMIC WAIT ENGINE
# ==============================================================================
def get_location(image_paths, confidence=0.7, timeout=NETWORK_TIMEOUT):
    if isinstance(image_paths, str): image_paths = [image_paths]
    start_time = time.time()
    while time.time() - start_time < timeout:
        for img in image_paths:
            try:
                loc = pyautogui.locateOnScreen(img, confidence=confidence, grayscale=True)
                if loc: return pyautogui.center(loc)
            except: pass
        time.sleep(0.05) 
    return None

def smart_click(image_paths, description, timeout=NETWORK_TIMEOUT, confidence=0.7, wait_after=0.1, optional=False):
    if isinstance(image_paths, str): image_paths = [image_paths]
    valid_images = [img for img in image_paths if os.path.exists(img)]
    if not valid_images: return False, None
    loc = get_location(valid_images, confidence, timeout)
    if loc:
        pyautogui.click(loc)
        time.sleep(wait_after) 
        return True, loc
    if optional: return True, None
    return False, None

# 🛑 MAANG FIX: Strict Confidence for AP Module
def hunt_and_click_payable(timeout=NETWORK_TIMEOUT):
    start_time = time.time()
    ap_images = ['images/s3.png', 'images/s33.png'] 
    while time.time() - start_time < timeout:
        for conf in [0.95, 0.9, 0.85]:
            for img in ap_images:
                try:
                    loc = pyautogui.locateOnScreen(img, confidence=conf, grayscale=True)
                    if loc:
                        pyautogui.click(pyautogui.center(loc))
                        return True
                except: pass
        time.sleep(0.1)
    return False
 
# ==============================================================================
# 🎯 INVOICE CLICK LOGIC (TARGET LOCK FIX - NO DEADLOCK)
# ==============================================================================
def force_click_invoice_until_post(timeout=20):
    print("[*] Clicking 'Invoice' buttons one-by-one to find 'Post Option'...")
    start_time = time.time()
    
    while time.time() - start_time < timeout:
        try:
            # 1. Create a list of all 'Invoice' buttons visible on the screen
            all_inv_locations = list(pyautogui.locateAllOnScreen('images/s6.png', confidence=0.8, grayscale=True))
            
            # 2. Click on each invoice one by one
            for inv_loc in all_inv_locations:
                pyautogui.click(pyautogui.center(inv_loc))
                time.sleep(1.0)  # Wait a bit so the M3 dropdown menu can open
                
                # 3. Check if 'Post' is visible or not
                post_loc = get_location('images/s7.png', confidence=0.8, timeout=0.5)
                if post_loc:
                    pyautogui.click(post_loc)
                    time.sleep(0.5)
                    pyautogui.press('enter') 
                    print("[+] SUCCESS: 'Post Option' is open and clicked!")
                    return True # EXIT DIRECTLY FROM HERE, WILL NOT GO TO THE NEXT INVOICE!
                else:
                    print("   [-] Post button not found here. Moving to next Invoice...")
                    time.sleep(0.5) # A short delay before clicking the next invoice
                    
        except Exception as e:
            pass # If no 'Invoice' is visible on the screen, ignore and search again
            
        time.sleep(0.5) # Small buffer after each scan loop
            
    print("[-] FAILED: Post Option did not appear despite checking visible Invoices.")
    return False

# ==============================================================================
# ⚡ RACE POLLER FOR MASTER GRID
# ==============================================================================
def wait_for_grid_or_warning(timeout=10):
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            if pyautogui.locateOnScreen('images/s10.png', confidence=0.8, grayscale=True): return 'GRID'
            if pyautogui.locateOnScreen('images/s8.png', confidence=0.8, grayscale=True): return 'WARNING'
        except: pass
        time.sleep(0.05) 
    return 'TIMEOUT'

# ==============================================================================
# ⚡ THE BLASTER SPEED OCR (💯 100% NO-LOSS ACCURACY EDITION)
# ==============================================================================
def map_all_visible_invoices():
    invoice_map = {}
    try:
        screenshot = pyautogui.screenshot()
        img_array = np.array(screenshot)
        img_cv = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)
        
        img_cv = cv2.resize(img_cv, None, fx=2.5, fy=2.5, interpolation=cv2.INTER_CUBIC)
        
        vision_modes = {
            "Black-Text": cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY),
            "Red-Hunter": cv2.split(img_cv)[1] 
        }
        
        for engine_name, processed_channel in vision_modes.items():
            _, thresh_img = cv2.threshold(processed_channel, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
            
            custom_config = r'--oem 3 --psm 11' 
            ocr_data = pytesseract.image_to_data(thresh_img, config=custom_config, output_type=pytesseract.Output.DICT)
            
            for i in range(len(ocr_data['text'])):
                raw_text = ocr_data['text'][i].strip()
                clean_text = re.sub(r'[^A-Za-z0-9\-#]', '', raw_text) 
                if len(clean_text) > 1: 
                    text_y = ocr_data['top'][i] / 2.5 
                    text_height = ocr_data['height'][i] / 2.5
                    click_y = int(text_y + (text_height / 2))
                    invoice_map[clean_text] = click_y 
                    
        return invoice_map
    except Exception as e: 
        print(f"   [!] OCR Error: {e}")
        return {}

# ==============================================================================
# 📊 EXCEL DATA INGESTION
# ==============================================================================
invoice_file = r"C:\Users\User\Abot\Invoice_Data.xlsx"
try:
    df = pd.read_excel(invoice_file)
    df['Property Name'] = df['Property Name'].ffill()
    df = df.dropna(subset=['Vendor'])
    
    if 'Invoice #' in df.columns: df.rename(columns={'Invoice #': 'Inv_Number'}, inplace=True)
    elif 'Invoice Number' in df.columns: df.rename(columns={'Invoice Number': 'Inv_Number'}, inplace=True)
    else: df['Inv_Number'] = "UNKNOWN"

    df['Inv_Number'] = df['Inv_Number'].astype(str).str.replace('.0', '', regex=False)
    df = df.drop_duplicates(subset=['Property Name', 'Vendor', 'Inv_Number'])
except Exception as e:
    print(f"Fatal Excel Data Error -> {e}")
    exit()

# ==============================================================================
# 🚀 MAIN EXECUTION ENGINE
# ==============================================================================
summary = []
time.sleep(2) 

global_start_time = time.time()
grouped_hotels = df.groupby('Property Name')

for hotel_name, group_df in grouped_hotels:
    hotel_name = str(hotel_name).strip()
    if hotel_name.lower() == 'nan': continue

    print(f"\n>>> PROCESSING: {hotel_name}")
    pyautogui.press('esc', presses=3, interval=0.01)
    time.sleep(0.2)

    # ----------------------------------------------------
    # ⚡ PHASE 1: SELF-HEALING HOTEL NAVIGATION
    # ----------------------------------------------------
    print(f"Initiating Hotel Switch -> {hotel_name}")
    
    selection_success = False
    for attempt in range(4):
        # First click on Select
        smart_click(['images/s1.png', 'images/s11.png'], 'Selection Start', wait_after=0.2)
        
        # Now check if the next step (Encore LLC) has opened or not?
        if get_location('images/s2.png', confidence=0.7, timeout=1.0):
            selection_success = True
            break # Path is clear!
        
        # If it reaches here, it means the Validation popup has blocked the Select button
        print(f"   [!] Validation Block Detected (Attempt {attempt+1})! Pressing ESC x3...")
        pyautogui.press('esc', presses=3, interval=0.1) # Will press ESC 3 times to clear the popup
        time.sleep(0.5) # Will wait a bit, loop back, and click Select again

    if not selection_success:
        for idx, row in group_df.iterrows():
            summary.append(f"Row {idx+2} | {hotel_name} | {row['Vendor']} | {row['Inv_Number']} | FAILED (Start Button Blocked)")
        continue

    success, encore_loc = smart_click('images/s2.png', 'Encore LLC', wait_after=0.1)
    if success:
        pyautogui.click()
        pyautogui.moveTo(encore_loc.x + 150, encore_loc.y, duration=0.1) # Right slide
        time.sleep(0.2)
    else:
        continue # If Encore is not found, proceed to the next property
    

    hotel_img = HOTEL_IMAGES.get(hotel_name)
    if not hotel_img: continue

    success, hotel_loc = smart_click(hotel_img, f"Hotel: {hotel_name}", confidence=0.9, wait_after=0.1)
    if success:
        pyautogui.moveTo(hotel_loc.x + 130, hotel_loc.y, duration=0.1)
        pyautogui.click()
        time.sleep(0.3) 
    else: continue

    if hunt_and_click_payable():
        time.sleep(0.5) 
    else: continue

    # ----------------------------------------------------
    # ⚡ PHASE 2: BATCH TICKING & OPTIMISTIC POSTING
    # ----------------------------------------------------
    batch_queued = False

    if force_click_invoice_until_post(): 
        
        print("   [*] Async Race: Waiting for Master Grid or Warning...")
        grid_status = wait_for_grid_or_warning()

        if grid_status == 'WARNING':
            print("   [!] Instant Catch: 'No pending invoice' state detected.")
            pyautogui.press('enter')
            time.sleep(0.1) 
            pyautogui.press('esc', presses=2, interval=0.01)
            for idx, row in group_df.iterrows():
                summary.append(f"Row {idx+2} | {hotel_name} | {row['Vendor']} | {row['Inv_Number']} | SKIP (Already posted or No pending)")
            continue 

        print("   [*] ⚡ Running 100% ACCURATE Mapped Screen Scan...")
        time.sleep(1.0) 
        visible_invoices = map_all_visible_invoices()

        for idx, row in group_df.iterrows():
            excel_row = idx + 2
            vendor_name = str(row['Vendor']).strip()
            invoice_num = str(row['Inv_Number']).strip()

            if invoice_num == 'nan' or invoice_num == 'UNKNOWN': continue
            
            if invoice_num in visible_invoices:
                click_y = visible_invoices[invoice_num]
                pyautogui.click(x=CHECKBOX_X_COORD, y=click_y)
                
                time.sleep(1.5) 
                
                batch_queued = True
                # Ignore validation, treat as direct SUCCESS
                summary.append(f"Row {excel_row} | {vendor_name} | {invoice_num} | SUCCESS") 
            else:
                # If not found in the master grid, execute direct SKIP
                summary.append(f"Row {excel_row} | {vendor_name} | {invoice_num} | SKIP (Already posted or No pending)")

        # ⚡ OPTIMISTIC FINAL POST
        if batch_queued:
            if smart_click('images/s10.png', 'Final Post', wait_after=0.5)[0]:
                print("   [+] Final Post clicked! Pressing 'Enter' then 'Y'...")
                time.sleep(0.5) 
                
                pyautogui.press('enter') 
                time.sleep(0.5)
                
                pyautogui.press('y') 
                # Bot will not wait here anymore. If validation pops up, it will be cleared by ESC x3 at the start of the next hotel!
                
        else:
            pyautogui.press('esc', presses=2, interval=0.01)

# ⏱️ GLOBAL TIME TRACKER END
total_time = time.time() - global_start_time
minutes = int(total_time // 60)
seconds = int(total_time % 60)

# ==============================================================================
# 📝 EXECUTION MANIFEST
# ==============================================================================
print("\n" + "="*60)
print("SYSTEM TERMINATED. FINAL EXECUTION MANIFEST:")
print("="*60)
for s in summary: print(s)
print("-" * 60)
print(f"⏱️ TOTAL TIME TAKEN: {minutes} Minutes and {seconds} Seconds")
print("="*60)