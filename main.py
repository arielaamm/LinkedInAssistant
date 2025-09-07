import linkedin.auth as login_linkedin
import os
from dotenv import load_dotenv


def main():
    # Load credentials from .env
    load_dotenv()
    username = os.getenv("LINKEDIN_USERNAME")
    password = os.getenv("LINKEDIN_PASSWORD")

    # Run LinkedIn automation
    driver = login_linkedin.run_linkedin_login(username, password)



if __name__ == "__main__":
    main()