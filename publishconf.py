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
SITEURL = "https://www.machines-walking-in-the-snow.com/"
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
#CLAIM_BING = os.environ.get("CLAIM_BING_PROD")
#STAT_COUNTER_PROJECT = os.environ.get("STAT_COUNTER_PROJECT_PROD")
#STAT_COUNTER_SECURITY = os.environ.get("STAT_COUNTER_SECURITY_PROD")
gOOGLE_ANALYTICS = os.environ.get("GOOGLE_ANALYTICS_PROD")
#DISQUS_SITENAME = os.environ.get("DISQUS_SITENAME")
#COMMENTBOX_PROJECT = os.environ.get("COMMENTBOX_PROJECT")

# MAILCHIMP_FORM_ACTION = os.environ.get("MAILCHIMP_FORM_ACTION")
UTTERANCES_REPO = os.environ.get("UTTERANCES_REPO")
#UTTERANCES_LABEL = os.environ.get("UTTERANCES_LABEL")

RELATIVE_URLS = False
# filetime_from_git is very slow. Use it in production only
# to avoid slow build times during development
PLUGINS.append("filetime_from_git")
PLUGINS.append("sitemap")

DELETE_OUTPUT_DIRECTORY = True
