import os

SETTINGS_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SETTINGS_DIR)
DATA_DIR = os.path.join(ROOT_DIR, 'data')

# Discord Conf
DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN", False)

# Reddit Configuration
REDDIT_APP_ID = os.getenv("REDDIT_APP_ID", False)
REDDIT_APP_SECRET = os.getenv("REDDIT_APP_SECRET", False)
REDDIT_ENABLED_ANIME_SUBREDDITS = [
    'waifu',
    'anime',
]
REDDIT_ENABLED_NSFW_SUBREDDITS = [
    'kpopfap'
    'kpics'
]

# Permissions

MODERATOR_ROLE_NAME = "Moderator"
