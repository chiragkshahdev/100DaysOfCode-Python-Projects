from bs4 import BeautifulSoup
import winsound  # Windows me beep bajane ke liye

TARGET_PRICE = 2000

def check_price():
    try:
        with open("amazon_page.html", encoding="utf-8", errors="ignore") as file:
            soup = BeautifulSoup(file.read(), "html.parser")
    except FileNotFoundError:
        print("ERROR: amazon_page.html nahi mili!")
        return

    try:
        title = soup.find(id="productTitle").get_text().strip()
    except:
        title = "Amazon Product"

    price = None
    try:
        price_text = soup.find(class_="a-price-whole").get_text()
        price = float(price_text.replace(",", "").strip())
    except:
        try:
            price_text = soup.find(class_="a-offscreen").get_text()
            price = float(price_text.replace("₹", "").replace("$", "").replace(",", "").strip())
        except:
            print("Price nahi mila. File dobara save karo.")
            return

    print(f"Product: {title[:80]}")
    print(f"Current Price: {price} | Target: {TARGET_PRICE}")

    if price < TARGET_PRICE:
        print("\n🔥 PRICE HAS BEEN DROPPED BUY NOW! 🔥")
        # 3 baar beep bajega
        for _ in range(3):
            winsound.Beep(1000, 500)
    else:
        print("Abhi price high hai. Baad me check karna.")

check_price()