from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def search_posts(driver, keyword):
    """Search LinkedIn for a topic and go to the Posts tab"""
    
    search_box = driver.find_element(By.XPATH, '//input[contains(@placeholder,"Search")]')
    search_box.clear()
    search_box.send_keys(keyword)
    search_box.send_keys(Keys.RETURN)
    time.sleep(3)

    posts_tab = driver.find_element(By.XPATH, '//button[contains(@aria-label,"Posts")]')
    posts_tab.click()
    time.sleep(5)
    print(f"Search results for '{keyword}' loaded.")