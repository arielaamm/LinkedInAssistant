from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

def search_posts(driver, keyword):
    """Search LinkedIn for a topic and go to the Posts tab"""
    
    search_box = driver.find_element(By.XPATH, '//input[contains(@placeholder,"Search")]')
    search_box.clear()
    search_box.send_keys(keyword)
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)
    posts_tab = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Posts']"))
    )
    posts_tab.click()
    time.sleep(2)
    print(f"Search results for '{keyword}' loaded.")