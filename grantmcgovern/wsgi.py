#!/usr/bin/env python

# -*- coding: utf-8 -*-
#
# @Author: grantmcgovern
# @Date:   2015-06-28 23:09:09
# @Email:   me@grantmcgovern.com
# @Web:    http://grantmcgovern.com
#
# @Last Modified by:   grantmcgovern
# @Last Modified time: 2015-07-12 19:58:29


"""
WSGI config for grantmcgovern project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "grantmcgovern.settings")

from django.core.wsgi import get_wsgi_application
from dj_static import Cling
application = Cling(get_wsgi_application())
#application = get_wsgi_application()
