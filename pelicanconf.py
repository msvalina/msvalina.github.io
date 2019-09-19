#!/usr/bin/env python3
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Marijan Svalina'
SITENAME = u'Here Be Dragons'
SITESUBTITLE = u'Thoughts on navigating at the edge of order and chaos. Seriously. And some IT stuff.' 
SITEURL = 'https://msvalina.org'
#SITEURL = ''

DEFAULT_DATE = 'fs'

DEFAULT_DATE_FORMAT = '%d %b %Y'

PATH = 'content'

TIMEZONE = 'Europe/Zagreb'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Leksikon', 'http://leksikon.thinking-garment.com'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

#DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['assets']

EXTRA_PATH_METADATA = {
    'assets/robots.txt': {'path': 'robots.txt'},
    'assets/favicon/favicon.ico': {'path': 'favicon.ico'},
    'assets/CNAME': {'path': 'CNAME'}
}

# Post and Pages path
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

# Tags and Category path
CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
CATEGORIES_SAVE_AS = 'categories.html'
TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}/index.html'
TAGS_SAVE_AS = 'tags.html'

# Author
AUTHOR_URL = 'author/{slug}'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'
AUTHORS_SAVE_AS = 'authors.html'

# Plugins

PLUGIN_PATHS = [
    'pelican-plugins'
]

PLUGINS = [
    'sitemap',
    'neighbors',
    'assets',
    'i18n_subsites',
    'gist_directive'
]

# I18N_SUBSITES = {
#     'hr': {
#         'SITENAME': 'Tu su Zmajevi.',
#     }
# }

# Sitemap
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


# Comments
#DISQUS_SITENAME = "attilademo"

# Analytics
#GOOGLE_ANALYTICS = "UA-3546274-12"

THEME = 'attila'

# To set background image for the home page.
HEADER_COVER = 'assets/images/header_doggy_teacher.jpg'

# Custom Header
HEADER_COVERS_BY_TAG = {'generic': 'assets/images/header_doggy_cool.jpg', 'btc':'assets/images/header_doggy_three.jpg'}


AUTHORS_BIO = {
    "marijan": {
        "name": "Marijan Svalina",
        "cover": "assets/images/header_doggy_cool.jpg",
        "image": "assets/images/msvalina-avatar.jpg",
        "github": "msvalina",
        "twitter": "msvalina",
        "website": "http://msvalina.org/pages/about/",
        "location": "Osijek",
        #"bio": u"Programer. Bitcoiner. Meditator. Majstor svih zanata, najbolji u ni jednom.🧘🏻‍♂️ ₿  💻"
        "bio": u"Programmer. Bitcoiner. Meditator. Jack of all trades master of none.🧘🏻‍♂️ ₿  💻"
    }
}

COLOR_SCHEME_CSS = 'github.css'

CSS_OVERRIDE = ['assets/css/override.css']

# Jinja config - Pelican 4
JINJA_ENVIRONMENT = {
    'extensions': [
        'jinja2.ext.loopcontrols',
        'jinja2.ext.i18n',
        'jinja2.ext.with_',
        'jinja2.ext.do'
    ]
}
