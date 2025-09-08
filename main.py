from linkedin.auth import run_linkedin_login
import os
from dotenv import load_dotenv
from linkedin import search as search_linkedin
from config import SEARCH_TOPICS

def main():
    # Load credentials from .env
    load_dotenv()
    username = os.getenv("LINKEDIN_USERNAME")
    password = os.getenv("LINKEDIN_PASSWORD")

    # Run LinkedIn automation
    driver = run_linkedin_login(username, password)

    # Example: Search for posts on a specific topic
    search_linkedin.search_posts(driver, SEARCH_TOPICS[0])  # Search for the first topic in the list
        



if __name__ == "__main__":
    main()