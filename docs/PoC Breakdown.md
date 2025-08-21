# PoC Breakdown – LinkedIn Assistant

## Introduction

This document details the Proof of Concept (PoC) of the project, breaking it down into clear parts and explaining each module.  
The goal is to create a base that can be extended into a full project.

---

## Part 1 – Setup and Login

**Goal:** Connect to a LinkedIn account and ensure the browser loads successfully.

**Tasks:**  

1. Install Python libraries: Selenium, WebDriver-Manager.  
2. Open Chrome browser (headless optional).  
3. Log in to LinkedIn with username/password.  
4. Verify the main feed page loads successfully.

**Notes:**  

- Use a dedicated test account.  
- `time.sleep()` is essential to wait for page loads.

---

## Part 2 – Search Posts

**Goal:** Collect a list of posts by topic/keyword.

**Tasks:**  

1. Enter a keyword/topic in LinkedIn search.  
2. Load initial results.  
3. Scroll to load a limited number of posts (e.g., 20).  
4. Save post IDs or links to a temporary file.

---

## Part 3 – Data Scraping

**Goal:** Extract basic information from the first 20 posts.

**Tasks:**  

1. For each post, collect:  
   - Post text  
   - Number of likes  
   - Number of comments  
   - Hashtags  
2. Save data to CSV or JSON for analysis.

---

## Part 4 – Basic Analysis

**Goal:** Perform initial analysis on scraped data.

**Tasks:**  

1. Count hashtags and display top 10.  
2. Calculate average likes per hashtag.  
3. Print results to console or simple chart.

---

## Part 5 – AI Post Generation (Future Expansion)

**Goal:** Demonstrate potential for automatic content creation.

**Tasks:**  

1. Provide hashtag/post as input to AI (GPT).  
2. Generate 1–2 post ideas as PoC.  
3. Save or display generated posts.

---

## General Notes

- Each part is independent for easier testing and debugging.  
- Start with mock data if needed before connecting to LinkedIn to save time and avoid account blocking.  
- Successfully tested small modules can be expanded directly into the full PoC.
