import time
from helper.linkedin_screenShot import take_linkedin_screenshot
from linkedin.auth import run_linkedin_login
import os
from dotenv import load_dotenv
from linkedin import search as search_linkedin
from config import SEARCH_TOPICS

def get_linkedin_screenshot(driver, file_path: str, picAmount) -> None:
    """Take a screenshot of the current LinkedIn page"""

    take_linkedin_screenshot(driver, file_path, picAmount)

def main():
    # Load credentials from .env
    load_dotenv()
    username = os.getenv("LINKEDIN_USERNAME")
    password = os.getenv("LINKEDIN_PASSWORD")

    # Run LinkedIn automation
    driver = run_linkedin_login(username, password)

    # Example: Search for posts on a specific topic
    search_linkedin.search_posts(driver, SEARCH_TOPICS[0])  # Search for the first topic in the list


def training_AI():
    # Load credentials from .env
    load_dotenv()
    username = os.getenv("LINKEDIN_USERNAME")
    password = os.getenv("LINKEDIN_PASSWORD")

    # Run LinkedIn automation
    driver = run_linkedin_login(username, password)
    for i in range(0,6):
        search_linkedin.search_posts(driver, SEARCH_TOPICS[i])  
        get_linkedin_screenshot(driver, "data\\images\\Raw linkedin screenShout\\",i*10)


if __name__ == "__main__":
    training_AI()
    # main()