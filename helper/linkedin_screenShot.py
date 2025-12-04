from selenium import webdriver
from helper import scroll

def take_linkedin_screenshot(driver: webdriver.Chrome, file_path: str,PrtSct_count) -> None:
    """Take a screenshot of the current LinkedIn page"""

    driver.execute_script("document.body.style.zoom = '0.75'")
    for _ in range(10):
        scroll.smart_scroll(driver)
        driver.save_screenshot(file_path + f"_part{_+PrtSct_count}.png")

        print(f"Screenshot saved to {file_path}_part{_+PrtSct_count}.png")