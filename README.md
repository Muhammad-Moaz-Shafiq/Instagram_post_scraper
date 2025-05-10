# 📸 Instagram Post Scraper

This is a Python-based tool that scrapes detailed information from **public Instagram posts** using [Instaloader](https://instaloader.github.io/). It is designed to help developers, data analysts, and researchers collect structured data without using the official Instagram API.

---

## 🔍 Features

- ✅ Extracts post caption, hashtags, and timestamp
- 💬 Captures all comments and replies
- 👍 Collects comment likes
- 👤 Retrieves usernames and profile pictures of commenters
- 💾 Saves data in structured formats like JSON or CSV

---

## 📦 Requirements

- Python 3.7+
- Instaloader

Install dependencies:
```bash
pip install instaloader
How to Use
Clone the repository:
git clone https://github.com/your-username/instagram-post-scraper.git
cd instagram-post-scraper
python insta.py

Enter the public post URL when prompted.

Extracted data will be saved in the /output folder.
Output Example
The tool saves data in JSON or CSV format, containing:
 {
        "input_url": "https://www.instagram.com/p/DJEoJ7soZ6G/",
        "id": 3622196604748013190,
        "shortcode": "DJEoJ7soZ6G",
        "type": "image",
        "caption": "We deliver across Pakistan in 3 to 7 days. Each cookie is baked fresh, sealed for protection, and packed to hold its shape and softness through the journey. From our kitchen to your city, with care.",
        "sidebar": "crumblepakistan",
        "url": "https://instagram.fisb31-2.fna.fbcdn.net/v/t51.2885-15/491445892_18063222506284512_8916199488837124420_n.jpg?stp=dst-jpg_e15_fr_p1080x1080_tt6&_nc_ht=instagram.fisb31-2.fna.fbcdn.net&_nc_cat=100&_nc_oc=Q6cZ2QGtCp1rcETqiXiC8F1KPqHXh4tmBES_jn92Ce_rUz9UFl718ZJpXvvcJbrvhtM0gXg&_nc_ohc=P--kj4ImYyoQ7kNvwEM10RG&_nc_gid=qJTvJuczHnBsBGJ1xfL0-g&edm=ANTKIIoBAAAA&ccb=7-5&oh=00_AfKFoq1S-Sg0xjjXZanICLU_IruXUOE4jFjVy8DQghtG6Q&oe=6824D9A1&_nc_sid=d885a2",
        "hashtags": [],
        "mentions": [],
        "likes": 953,
        "timestamp": "2025-04-30 13:25:05",
        "location": null,
        "comments": 27
    }
