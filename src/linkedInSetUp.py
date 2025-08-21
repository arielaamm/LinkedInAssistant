from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# פתיחת הדפדפן
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

# כניסה ללינקדאין
driver.get("https://www.linkedin.com/login")

# הכנס את פרטי המשתמש שלך כאן
USERNAME = "arialaamm@gmail.com"
PASSWORD = "trhtkaamm"

# מציאת שדות ההתחברות והזנת פרטים
driver.find_element(By.ID, "username").send_keys(USERNAME)
driver.find_element(By.ID, "password").send_keys(PASSWORD)
driver.find_element(By.ID, "password").send_keys(Keys.RETURN)

time.sleep(5)  # המתנה לטעינת הדף
print("Login successful!")

# אפשר לבדוק פתיחת הדף הראשי
driver.get("https://www.linkedin.com/feed/")
time.sleep(5)

print("Feed loaded")
driver.quit()
