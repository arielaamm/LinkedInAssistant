# LinkedIn Assistant PoC – Part 1: Setup and Login
# This script demonstrates connecting to LinkedIn and opening the main feed.
# It is the first step in the PoC before collecting posts.

#auth.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


def start_browser():
    """Using webdriver-manager to automatically manage ChromeDriver"""
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()  # Maximize window to ensure elements are visible
    return driver

def login_linkedin(driver, username, password):
    """Navigate to LinkedIn login page and enter login credentials"""
    driver.get("https://www.linkedin.com/login")
    time.sleep(2)  # Wait for the page to load

    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")

    username_field.send_keys(username)
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)  # Press Enter to login

    # Wait for login to complete and main feed to load
    time.sleep(2)
    print("Login successful!")

def open_feed(driver):
    """Navigate to the LinkedIn main feed"""
    driver.get("https://www.linkedin.com/feed/")
    time.sleep(2)  # Wait for feed to fully load
    print("Feed loaded successfully")

def run_linkedin_login(username, password) -> webdriver.Chrome:
    """Full LinkedIn login flow"""
    driver = start_browser()
    login_linkedin(driver, username, password)
    open_feed(driver)
    return driver