"""
Handles saving, loading, and managing scheduled posts in a local JSON file.
Acts as a simple database for the scheduler.
"""

import json
import os
from datetime import datetime
from config import SCHEDULE_FILE


def _load_all() -> list:
    if not os.path.exists(SCHEDULE_FILE):
        return []
    with open(SCHEDULE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def _save_all(posts: list):
    with open(SCHEDULE_FILE, "w", encoding="utf-8") as f:
        json.dump(posts, f, indent=2)


def schedule_post(platform: str, caption: str, hashtags: list, publish_date: str):
    """Add a new post to the schedule. publish_date format: YYYY-MM-DD HH:MM"""
    posts = _load_all()
    post = {
        "id": len(posts) + 1,
        "platform": platform,
        "caption": caption,
        "hashtags": hashtags,
        "publish_date": publish_date,
        "status": "scheduled",
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    posts.append(post)
    _save_all(posts)
    return post


def get_upcoming_posts() -> list:
    """Return all posts that are still scheduled (not yet marked as published)."""
    posts = _load_all()
    return [p for p in posts if p["status"] == "scheduled"]


def mark_as_published(post_id: int):
    """Update a post's status to 'published' once it has gone live."""
    posts = _load_all()
    for post in posts:
        if post["id"] == post_id:
            post["status"] = "published"
    _save_all(posts)
