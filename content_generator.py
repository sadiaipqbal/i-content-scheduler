"""
Generates social media captions and relevant hashtags using an LLM.
"""

from openai import OpenAI
from config import AI_API_KEY, DEFAULT_TONE

client = OpenAI(api_key=AI_API_KEY)

SYSTEM_PROMPT = """You are a social media content expert. Given a topic and platform,
write an engaging caption suited to that platform's style and length conventions,
plus 5 relevant hashtags.

Respond ONLY with a valid JSON object in this exact format, no extra text:
{
  "caption": "<the generated caption>",
  "hashtags": [<list of 5 hashtag strings, each starting with #>]
}"""


def generate_post_content(topic: str, platform: str, tone: str = DEFAULT_TONE) -> dict:
    """Generate a caption and hashtags for a given topic and platform."""
    user_prompt = f"""Platform: {platform}
Topic: {topic}
Tone: {tone}"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.8,
        max_tokens=250,
    )

    import json
    raw_output = response.choices[0].message.content.strip()

    try:
        return json.loads(raw_output)
    except json.JSONDecodeError:
        return {"caption": raw_output, "hashtags": []}
