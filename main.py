"""
AI Social Media Content Scheduler
------------------------------------
Generates AI-powered captions and hashtags for a given topic, then schedules
the post for a chosen date and time.

Usage:
    python main.py
"""

from content_generator import generate_post_content
from scheduler import schedule_post, get_upcoming_posts


def run():
    print("=== AI Social Media Content Scheduler ===\n")

    topic = input("Enter a topic for your post: ").strip()
    platform = input("Platform (Instagram/LinkedIn/Twitter/Facebook): ").strip()
    publish_date = input("Publish date & time (YYYY-MM-DD HH:MM): ").strip()

    print("\nGenerating caption and hashtags...")
    content = generate_post_content(topic, platform)

    print(f"\nCaption:\n{content['caption']}")
    print(f"\nHashtags: {' '.join(content['hashtags'])}")

    confirm = input("\nSchedule this post? (y/n): ").strip().lower()
    if confirm == "y":
        post = schedule_post(platform, content["caption"], content["hashtags"], publish_date)
        print(f"\nPost #{post['id']} scheduled for {publish_date} on {platform}.")
    else:
        print("\nPost discarded.")

    print("\n--- Upcoming Scheduled Posts ---")
    for p in get_upcoming_posts():
        print(f"#{p['id']} | {p['platform']} | {p['publish_date']} | {p['caption'][:50]}...")


if __name__ == "__main__":
    run()
