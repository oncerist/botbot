import os

SETTINGS_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SETTINGS_DIR)
DATA_DIR = os.path.join(ROOT_DIR, 'data')

# Discord Conf
token = os.getenv("token", False)

# Reddit Configuration
REDDIT_APP_ID = os.getenv("REDDIT_APP_ID", False)
REDDIT_APP_SECRET = os.getenv("REDDIT_APP_SECRET", False)
REDDIT_ENABLED_ANIME_SUBREDDITS = [
    'Waifu',
    'Anime',
]
REDDIT_ENABLED_NSFW_SUBREDDITS = [
    'kpopfap',
    'kpics',
    
]

# Permissions

MODERATOR_ROLE_NAME = "Moderator"
