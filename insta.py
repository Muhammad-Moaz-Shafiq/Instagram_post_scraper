import instaloader
import re
from datetime import datetime
from urllib.parse import urlparse

# Load instaloader
L = instaloader.Instaloader()

post_urls = [
    "https://www.instagram.com/p/{post.shortcode}/",
    "https://www.instagram.com/p/{post.shortcode}/",
    # ...up to 1220 URLs
]

def extract_shortcode(url):
    return url.strip("/").split("/")[-1]

def extract_data_from_post(post):
    caption = post.caption or ""
    hashtags = post.caption_hashtags
    mentions = post.caption_mentions
    return {
        "input_url": f"https://www.instagram.com/p/{post.shortcode}/",
        "id": post.mediaid,
        "shortcode": post.shortcode,
        "type": "video" if post.is_video else "image",
        "caption": caption,
        "sidebar": post.owner_username,
        "url": post.url,
        "hashtags": hashtags,
        "mentions": mentions,
        "likes": post.likes,
        "timestamp": post.date_utc.strftime("%Y-%m-%d %H:%M:%S"),
        "location": post.location.name if post.location else None,
        "comments": post.comments,
                        
    }

all_data = []

for url in post_urls:
    shortcode = extract_shortcode(url)
    try:
        post = instaloader.Post.from_shortcode(L.context, shortcode)
        post_data = extract_data_from_post(post)
        all_data.append(post_data)
        print(f"✅ Extracted: {shortcode}")
    except Exception as e:
        print(f"❌ Error with {shortcode}: {e}")

# Save as CSV or JSON if needed
import json
with open("instagram_posts_data.json", "w", encoding="utf-8") as f:
    json.dump(all_data, f, ensure_ascii=False, indent=4)
