#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import date

import os

AUTHOR = "Marc-Olivier Titeux"
SITENAME = "Machines walking in the snow"
SITEURL = ""

PATH = "content"
ARTICLE_PATHS = ['articles']
PAGE_PATHS = ['pages']

DISPLAY_PAGES_ON_MENU = True

# Regional Settings
TIMEZONE = "Europe/Zurich"
DATE_FORMATS = {"en": "%b %d, %Y"}

# Plugins and extensions
MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.admonition": {},
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
        "markdown.extensions.toc": {"permalink": " "},
    }
}

PLUGIN_PATHS = ["plugins"]
PLUGINS = [
    "assets",
    "extract_toc",
    "liquid_tags.img",
    "liquid_tags.include_code",
    "neighbors",
    "related_posts",
    "render_math",
    "series",
    "share_post",
    "tipue_search",
    'better_figures_and_images',
    'post_stats',
]
SITEMAP = {
    "format": "xml",
    "priorities": {"articles": 0.5, "indexes": 0.5, "pages": 0.5},
    "changefreqs": {"articles": "monthly", "indexes": "daily", "pages": "monthly"},
}

# Appearance
THEME = "themes/pelican-elegant"
TYPOGRIFY = True
DEFAULT_PAGINATION = False
USE_SHORTCUT_ICONS = True

# Defaults
DEFAULT_CATEGORY = "miscellaneous"
USE_FOLDER_AS_CATEGORY = False
ARTICLE_URL = "{date:%Y}/{date:%m}/{date:%d}/{slug}/"
ARTICLE_SAVE_AS = "{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html"
PAGE_URL = "{slug}"
PAGE_SAVE_AS = "{slug}.html"
TAGS_URL = "tags"
CATEGORIES_URL = "categories"
ARCHIVES_URL = "archives"
SEARCH_URL = "search"

# Feeds
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None

# Elegant theme
STATIC_PATHS = ["theme/images", "images", "extra/CNAME"]
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'}
    }

if os.environ.get("CONTEXT") == "production":
    STATIC_PATHS.append("extra/robots.txt")
    EXTRA_PATH_METADATA["extra/robots.txt"] = {"path": "robots.txt"}
else:
    STATIC_PATHS.append("extra/robots_deny.txt")
    EXTRA_PATH_METADATA["extra/robots_deny.txt"] = {"path": "robots.txt"}

DIRECT_TEMPLATES = ["index", "tags", "categories", "archives", "search", "404"]
TAG_SAVE_AS = ""
AUTHOR_SAVE_AS = ""
CATEGORY_SAVE_AS = ""

# What do we want archive URLs to look like?
YEAR_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/index.html'
DAY_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/index.html'

# Do something if people visit /blog
ARCHIVES_SAVE_AS = 'blog/index.html'


SUMMARY_MAX_LENGTH = 80

#################################
#
# Cache Settings
#
#################################
CACHE_CONTENT = True
CHECK_MODIFIED_METHOD = 'mtime'
LOAD_CONTENT_CACHE = True
GZIP_CACHE = False

# Elegant Labels
SOCIAL_PROFILE_LABEL = "Stay in Touch"
RELATED_POSTS_LABEL = "Keep Reading"
SHARE_POST_INTRO = "Like this post? Share on:"
COMMENTS_INTRO = "So what do you think? Did I miss something? Is any part unclear? Leave your comments below."

# Social
SOCIAL = (
    ("Github", "https://github.com/motiteux/", "My Github repositories"),
    ("Twitter", "https://twitter.com/MarcoTiteux"),
    ("LinkedIn", "https://www.linkedin.com/in/motiteux/"),
    ("RSS", SITEURL + "/feeds/all.atom.xml"),
    (
        "Calendar",
        "https://github.com/Pelican-Elegant/elegant/milestones",
        "Elegant Project Roadmap",
    ),
)

# Email Subscriptions
EMAIL_SUBSCRIPTION_LABEL = "Get New Content Notifications"
EMAIL_FIELD_PLACEHOLDER = "Enter your email..."
SUBSCRIBE_BUTTON_TITLE = "Notify me"

#FREELISTS_NAME = "oracle-l"
#FREELISTS_FILTER = True

# SMO
TWITTER_USERNAME = "MarcoTiteux"
FEATURED_IMAGE = SITEURL + "/theme/images/apple-touch-icon.png"

# Legal
SITE_LICENSE = """<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/">
    <a property="dct:title" rel="cc:attributionURL"
    href="https://machines-walking-in-the-snow.com/">Machines walking in the snow</a>
    by <a rel="cc:attributionURL dct:creator" property="cc:attributionName"
    href="https://machines-walking-in-the-snow.com/about-me">Marc-Olivier Titeux</a> is licensed
    under <a href="http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1" target="_blank"
    rel="license noopener noreferrer" style="display:inline-block;">CC BY-NC 4.0
    <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;"
    src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1">
    <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;"
    src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1">
    <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;"
    src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1"></a></p>"""

#HOSTED_ON = {"name": "Github Pages", "url": "https://www.github.com/"}

# SEO
SITE_DESCRIPTION = (
    "I try to design some machines that will struggle in life, and I want to write about it"
)

# Share links at bottom of articles
# Supported: twitter, facebook, hacker-news, reddit, linkedin, email
SHARE_LINKS = [("twitter", "Twitter"), ("facebook", "Facebook"), ("email", "Email")]

# Landing Page
PROJECTS_TITLE = "Related Projects"
PROJECTS = [
    {
        "name": "About me",
        "url": SITEURL + "about-me",
        "description": "Some fancy details about myself",
    },
    {
        "name": "View the project on Github",
        "url": "https://github.com/motiteux/machines-walking",
        "description": "Source code of Machines walking in the snow",
    },
]

LANDING_PAGE_TITLE = "My little corner of convergence"

AUTHORS = {
    "Marc-Olivier Titeux": {
        "url": "https://www.machines-walking-in-the-snow.com/",
        "blurb": "",
        "avatar": "/images/motiteux.png",
    },
}
#DISQUS_FILTER = True
#UTTERANCES_FILTER = True
#COMMENTBOX_FILTER = True


# Settings for the related_posts plugin
RELATED_POSTS_MAX = 4
