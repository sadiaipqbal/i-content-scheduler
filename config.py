"""
Configuration settings for the AI Social Media Content Scheduler.
"""

import os
from dotenv import load_dotenv

load_dotenv()

# AI API key (OpenAI used here to generate captions)
AI_API_KEY = os.getenv("AI_API_KEY")

# File where scheduled posts are stored
SCHEDULE_FILE = os.getenv("SCHEDULE_FILE", "scheduled_posts.json")

# Default tone/style used when generating captions
DEFAULT_TONE = os.getenv("DEFAULT_TONE", "friendly and engaging")
