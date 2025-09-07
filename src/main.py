import linkedInSetUp as action
import os
from dotenv import load_dotenv


def main():
    # Load credentials from .env
    load_dotenv()
    username = os.getenv("LINKEDIN_USERNAME")
    password = os.getenv("LINKEDIN_PASSWORD")

    # Run LinkedIn automation
    driver = action.run_linkedin(username, password)

    

if __name__ == "__main__":
    main()