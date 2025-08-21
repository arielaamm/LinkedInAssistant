# Product Backlog – LinkedIn Assistant

## Epic

**Epic:** Collect, analyze, and generate LinkedIn posts using AI to help users understand trends and create relevant content.

---

## User Story 1

**Story:**  
As a new LinkedIn user, I want the system to collect trending posts by topic so I can know the trends.

**Acceptance Criteria:**  

- Returns at least 20 posts per topic.  
- Each post contains text + number of likes + number of comments + hashtags.  
- Posts are collected chronologically or by popularity.  
- Mimics human behavior to avoid blocking.

**Tasks:**  

1. Connect to LinkedIn using Selenium or API.  
2. Perform a search by keyword/topic.  
3. Collect posts – text, likes, comments, hashtags.  
4. Save data to CSV or database.  
5. Verify at least one post is collected correctly.

---

## User Story 2

**Story:**  
As a user, I want the system to analyze hashtags and likes to understand popular topics.

**Acceptance Criteria:**  

- Extracts all hashtags from collected posts.  
- Calculates the frequency of hashtags and shows the top 10.  
- Calculates average likes per hashtag/topic.  
- Analysis is presented in a readable format (table or chart).

**Tasks:**  

1. Read CSV from User Story 1.  
2. Extract hashtags from each post.  
3. Calculate frequency of each hashtag.  
4. Calculate average likes per hashtag.  
5. Present results in a table or chart.

---

## User Story 3

**Story:**  
As a user, I want the system to generate post ideas automatically based on trends so I can create relevant content.

**Acceptance Criteria:**  

- Receives input from hashtags/trends from User Story 2.  
- Generates at least 3 post ideas per trend.  
- Posts are readable and ready for copy/paste.  
- System can select different modes (professional, personal, experiential).

**Tasks:**  

1. Use AI (e.g., GPT) to generate text for posts.  
2. Provide hashtags/trends as input to AI.  
3. Define different modes for post generation.  
4. Save or display generated posts.  
5. Ensure posts are relevant and trend-focused.
