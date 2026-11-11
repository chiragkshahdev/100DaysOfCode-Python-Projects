import time
import ctypes

# Windows ka built-in mouse click - koi pip nahi chahiye
user32 = ctypes.windll.user32

def click():
    # Left mouse button down + up = 1 click
    user32.mouse_event(0x0002, 0, 0, 0, 0)  # Left Down
    user32.mouse_event(0x0004, 0, 0, 0, 0)  # Left Up

print("=== COOKIE CLICKER BOT - NO PIP, NO SELENIUM ===")
print("")
print("1. Browser me ye kholo: https://orteil.dashnet.org/cookieclicker/")
print("2. Language English select karo")
print("3. Mouse ko Bade Cookie ke UPAR rakh do")
print("")
print("Bot 5 second me start hoga...")
for i in range(5, 0, -1):
    print(f"{i}...")
    time.sleep(1)

print("Bot START! Rokne ke liye Ctrl + C dabao")
print("")

click_count = 0
start_time = time.time()

try:
    while True:
        # 1 second me 30 click
        for _ in range(30):
            click()
            click_count += 1
        time.sleep(0.1)
        print(f"Total Clicks: {click_count} | Time: {int(time.time() - start_time)} sec")

except KeyboardInterrupt:
    print("")
    print(f"Bot Ruk Gaya! Total Clicks: {click_count}")