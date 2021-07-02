#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *


# Important: Changing SITEURL may break links in deploy-previews
if os.environ.get("CONTEXT") == "production":
    SITEURL = "https://www.machines-walking-in-the-snow.com"
    FEED_DOMAIN = SITEURL
    FEED_ALL_ATOM = "feeds/all.atom.xml"
    CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
    MODERN_GOOGLE_ANALYTICS = os.environ.get("GOOGLE_TAG_MEASUREMENT_ID")
    UTTERANCES_REPO = os.environ.get("UTTERANCES_REPO")
    UTTERANCES_LABEL = os.environ.get("UTTERANCES_LABEL")

elif os.environ.get("CONTEXT") == "staging":
    SITENAME = "Machines walking in the snow (next)"
    SITEURL = "http://next.www.machines-walking-in-the-snow.com"
    FEED_DOMAIN = SITEURL
    MODERN_GOOGLE_ANALYTICS = ""

else:
   SITENAME = ""
   SITEURL = ""


# MAILCHIMP_FORM_ACTION = os.environ.get("MAILCHIMP_FORM_ACTION")

RELATIVE_URLS = False
# filetime_from_git is very slow. Use it in production only
# to avoid slow build times during development
PLUGINS.append("filetime_from_git")
PLUGINS.append("sitemap")

DELETE_OUTPUT_DIRECTORY = True
