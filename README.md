# AI Social Media Content Scheduler

An AI-powered tool that generates engaging social media captions and hashtags for any topic, then schedules posts for future publishing.

## Features
- Generates platform-specific captions (Instagram, LinkedIn, Twitter, Facebook) using an LLM
- Automatically suggests 5 relevant hashtags per post
- Schedules posts with a publish date and time
- Stores scheduled posts locally in a simple JSON-based system
- Tracks post status (scheduled vs. published)

## Tech Stack
- Python 3
- OpenAI API (LLM for caption generation)
- JSON (local post storage)
- python-dotenv (environment variable management)

## Project Structure
```
ai-content-scheduler/
│── main.py                    # Entry point — CLI for generating and scheduling posts
│── content_generator.py         # Generates captions and hashtags using the LLM
│── scheduler.py                   # Saves, loads, and manages scheduled posts
│── config.py                        # Loads settings from environment variables
│── requirements.txt                   # Python dependencies
│── env.example                          # Example environment configuration
```

## How It Works
1. The user enters a topic, platform, and desired publish date/time.
2. `content_generator.py` sends the topic to the LLM, which returns a caption and hashtags.
3. The user reviews and confirms the generated content.
4. `scheduler.py` saves the approved post into `scheduled_posts.json` with a "scheduled" status.
5. Upcoming scheduled posts can be viewed at any time.

## Setup

1. Clone the repository:
```bash
git clone https://github.com/sadiaipqbal/ai-content-scheduler.git
cd ai-content-scheduler
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Copy `env.example` to `.env` and add your API key:
```bash
cp env.example .env
```

4. Run the scheduler:
```bash
python main.py
```

## Example Run
```
Enter a topic for your post: Launching our new eco-friendly water bottle
Platform (Instagram/LinkedIn/Twitter/Facebook): Instagram

Caption:
Say hello to your new favorite bottle 🌿 Sustainable, sleek, and ready for
every adventure. Small choices, big impact!

Hashtags: #EcoFriendly #SustainableLiving #NewLaunch #GoGreen #ReuseReduceRecycle

Schedule this post? (y/n): y
Post #1 scheduled for 2026-07-10 09:00 on Instagram.
```

## Future Improvements
- Integrate with real platform APIs (Meta, LinkedIn, X) to auto-publish posts
- Add a web dashboard with a calendar view of scheduled content
- Support image/video generation alongside captions
- Add analytics tracking for published posts

## Disclaimer
This project is for educational and portfolio purposes. Review AI-generated captions before publishing to ensure brand voice and accuracy.
