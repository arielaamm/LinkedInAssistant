# LinkedIn Assistant PoC – Part 1: Setup and Login
# This script demonstrates connecting to LinkedIn and opening the main feed.
# It is the first step in the PoC before collecting posts.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# -------------------------
# Configuration
# -------------------------
USERNAME = "your_email"       # Replace with your LinkedIn test account email
PASSWORD = "your_password"    # Replace with your LinkedIn test account password

# -------------------------
# Step 1: Open Chrome Browser
# -------------------------
# Using webdriver-manager to automatically manage ChromeDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()  # Maximize window to ensure elements are visible

# -------------------------
# Step 2: Navigate to LinkedIn Login Page
# -------------------------
driver.get("https://www.linkedin.com/login")
time.sleep(2)  # Wait for the page to load

# -------------------------
# Step 3: Enter Login Credentials
# -------------------------
username_field = driver.find_element(By.ID, "username")
password_field = driver.find_element(By.ID, "password")

username_field.send_keys(USERNAME)
password_field.send_keys(PASSWORD)
password_field.send_keys(Keys.RETURN)  # Press Enter to login

# Wait for login to complete and main feed to load
time.sleep(5)
print("Login successful!")

# -------------------------
# Step 4: Navigate to Main Feed
# -------------------------
driver.get("https://www.linkedin.com/feed/")
time.sleep(5)  # Wait for feed to fully load
print("Feed loaded successfully")

# -------------------------
# Step 5: Close Browser
# -------------------------
driver.quit()
