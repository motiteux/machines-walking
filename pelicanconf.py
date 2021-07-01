#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Marc-O'
AUTHOR_EMAIL = 'marcolivier.titeux@gmail.com'
SITENAME = 'Machines walking in the snow'
SITESUBTITLE = u"My little corner of convergence"
SITEURL = 'https://motiteux.github.io/machines-walking/'
DESCRIPTION = ''
ABOUT = u'My little corner'

TIMEZONE = 'Europe/Zurich'
PDF_GENERATOR = False
REVERSE_CATEGORY_ORDER = True
LOCALE = "C"
PATH = 'content'

DEFAULT_LANG = 'en'

THEME = 'themes/pelican-elegant'
TYPOGRIFY = True

# url
INDEX_URL = 'blog'
INDEX_SAVE_AS = INDEX_URL+'/index.html'

ARTICLE_URL = INDEX_URL+'/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = ARTICLE_URL+'/index.html'
YEAR_ARCHIVE_SAVE_AS = INDEX_URL + '/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = INDEX_URL + '/{date:%Y}/{date:%m}/index.html'

page_dir = 'pages'
PAGE_URL = page_dir+'/{slug}'
PAGE_SAVE_AS = PAGE_URL+'/index.html'

# Feeds
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
TAG_FEED_ATOM = 'feeds/%s.atom.xml'
TAG_FEED_RSS = 'feeds/%s.rss.xml'
TRANSLATION_FEED_ATOM = None

# Social
SOCIAL = (("twitter", 'https://twitter.com/MarcoTiteux'),
          ("linkedin", 'https://www.linkedin.com/in/marcoliviertiteux'),
          ("github", 'http://github.com/motiteux/'),
          ("bitbucket", 'https://bitbucket.org/marc_olivier'),)
                                                  
CONTACT = u'marcolivier.titeux@gmail.com'
CONTACT_EMAIL = CONTACT
CONTACTS = SOCIAL

GOOGLE_ANALYTICS = 'UA-26850780-1'

GITHUB_INTEGRATION_ENABLED = True
GITHUB_URL = 'http://github.com/motiteux/'
GITHUB_USERNAME = 'motiteux'

TWITTER_INTEGRATION_ENABLED = True
TWITTER_USERNAME = 'MarcoTiteux'

DISQUS_SITENAME = "marcolivier"

GOOGLE_ANALYTICS = 'UA-26850780-1'

STATIC_PATHS = ['images', 'extra/CNAME', 'extra/favicon.ico', 'extra/robots.txt']
EXTRA_PATH_METADATA = {
          'extra/CNAME': {'path': 'CNAME'},
          'extra/favicon.ico': {'path': 'favicon.ico'},
          'extra/robots.txt': {'path': 'robots.txt'},
}

# code blocks with line numbers
PYGMENTS_RST_OPTIONS = {'linenos': 'table'}

USE_CUSTOM_MENU = True
CUSTOM_MENUITEMS = (('Blog', INDEX_URL),
                    ('Contact', 'contact'),
                    ('Projects', page_dir + '/projects'))

MENUITEMS = (('Blog', INDEX_URL),
             ('Contact', 'contact'),
             ('Projects', page_dir + '/projects'))

# Plugins
PLUGIN_PATH = 'plugins'
# PLUGINS=['sitemap', 'gzip_cache', 'assets', 'gravatar',]
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}
