import random
from time import sleep
from selenium.webdriver.common.by import By

def smart_scroll(driver, base_wait=0.25):
    """
    Scrolls like a human, expands 'more', and ensures the full post
    is visible on screen so screenshots capture the whole content.
    """

    def expand_more_in_post(post):
        """Expand 'more' buttons inside a given post."""
        try:
            buttons = post.find_elements(By.XPATH, ".//button[contains(., 'more') or contains(., 'See more')]")
            for btn in buttons:
                driver.execute_script("arguments[0].scrollIntoView({block:'center'});", btn)
                sleep(0.15)
                driver.execute_script("arguments[0].click();", btn)
                sleep(0.25)
        except:
            pass

    def get_post_in_center():
        """Return the post element closest to screen center."""
        viewport_height = driver.execute_script("return window.innerHeight;")
        center_y = viewport_height // 2

        posts = driver.find_elements(By.CSS_SELECTOR, "div.feed-shared-update-v2")  # לוכד את כל הפוסטים

        best_post = None
        best_distance = 999999

        for p in posts:
            try:
                rect = driver.execute_script("return arguments[0].getBoundingClientRect();", p)
                post_center = (rect["top"] + rect["bottom"]) / 2
                distance = abs(post_center - center_y)
                if distance < best_distance:
                    best_distance = distance
                    best_post = p
            except:
                continue

        return best_post

    # ---- שלב 1 — גלילה אנושית ----
    scroll_amount = random.randint(220, 480)
    if random.random() < 0.1:
        scroll_amount = -random.randint(40, 80)

    driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
    sleep(base_wait + random.uniform(0.1, 0.35))

    # ---- שלב 2 — לזהות איזה פוסט עלינו לצלם ----
    post = get_post_in_center()
    if post is None:
        print("No post found in center — skipping.")
        return

    # ---- שלב 3 — לפתוח MORE ----
    expand_more_in_post(post)

    # ---- שלב 4 — לוודא שהפוסט כולו גלוי למסך ----
    # מביאים את החלק העליון למסך:
    driver.execute_script("arguments[0].scrollIntoView({block:'start'});", post)
    sleep(0.25)

    # גובה הפוסט עצמו
    height = driver.execute_script("return arguments[0].offsetHeight;", post)

    # אם הפוסט גדול מהמסך — נגלול חלקים עד שהוא כולו ייחשף
    viewport = driver.execute_script("return window.innerHeight;")

    scrolled = 0
    while scrolled + viewport < height:
        driver.execute_script("window.scrollBy(0, arguments[0]);", viewport - 50)
        scrolled += viewport - 50
        sleep(0.25)

    # בסוף הפוסט יהיה כולו גלוי
    print("Post is fully visible and ready for screenshot.")
