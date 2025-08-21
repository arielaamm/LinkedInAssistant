# Architecture Overview – LinkedIn Assistant

## Overview

The LinkedIn Assistant PoC is divided into multiple modules that process data step by step from collection to AI-generated posts.

### Modules (Step-by-Step Description)

1. **Scraper**
   - Collects posts from LinkedIn, including text, likes, comments, and hashtags.  
   - Handles search by keyword/topic and loads a limited number of posts (e.g., 20 for PoC).  

2. **Storage**
   - Saves the scraped data in a structured format (CSV or database).  
   - Ensures data is readable and accessible for further processing.

3. **Analysis**
   - Reads stored data.  
   - Counts hashtags and computes popularity metrics (frequency, average likes).  
   - Identifies top trends for AI content generation.

4. **AI Generator**
   - Receives hashtags/trends as input.  
   - Generates post ideas using AI in different modes (professional, personal, experiential).  
   - Outputs posts ready to copy/paste or for optional automated publishing.

5. **Output / Post**
   - Displays generated posts in a readable format or publishes automatically while simulating human behavior.  

**Data Flow:**  
Scraper → Storage → Analysis → AI Generator → Output/Post  
Each module is independent but sequential, allowing modular testing and expansion.
