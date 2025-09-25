"""
Selenium script template: login -> search -> open product -> add to cart
Note: This is a demo script. Use staging URL and test credentials. Avoid running on production.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def main():
    # Configure options if needed
    driver = webdriver.Chrome()  # ensure chromedriver in PATH
    driver.maximize_window()
    try:
        # Open site (replace with staging URL)
        driver.get("https://www.flipkart.com")
        time.sleep(2)

        # Close login popup if appears
        try:
            close_btn = driver.find_element(By.XPATH, "//button[contains(., '✕') or contains(., 'Close')]")
            close_btn.click()
            time.sleep(1)
        except Exception:
            pass

        # Search for product
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("mobile")
        search_box.send_keys(Keys.ENTER)
        time.sleep(3)

        # Click first product
        products = driver.find_elements(By.CSS_SELECTOR, "a._1fQZEK, a.s1Q9rs")
        if products:
            products[0].click()
            time.sleep(3)
        else:
            print("No products found")
            return

        # Switch to product window if opened in new tab
        if len(driver.window_handles) > 1:
            driver.switch_to.window(driver.window_handles[1])
            time.sleep(1)

        # Add to cart (best-effort)
        try:
            add_btn = driver.find_element(By.XPATH, "//button[contains(., 'Add to cart') or contains(., 'ADD TO CART')]")
            add_btn.click()
            time.sleep(2)
            print("Clicked Add to Cart")
        except Exception as e:
            print("Add to cart not found or failed:", e)

    finally:
        time.sleep(2)
        driver.quit()

if __name__ == '__main__':
    main()
