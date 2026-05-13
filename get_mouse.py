import pyautogui, time

print("Apna mouse 'Post' wale checkbox ke ekdum center me le jaao aur wahi rakho...")
print("(Script band karne ke liye terminal me Ctrl+C dabana)\n")

try:
    while True:
        x, y = pyautogui.position()
        print(f"👉 Tumhara X-Coordinate hai: {x} ", end='\r')
        time.sleep(0.5)
except KeyboardInterrupt:
    print("\nDone!")