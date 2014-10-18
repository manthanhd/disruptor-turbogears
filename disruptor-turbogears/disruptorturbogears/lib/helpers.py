# -*- coding: utf-8 -*-

"""WebHelpers used in disruptor-turbogears."""

#from webhelpers import date, feedgenerator, html, number, misc, text
import uuid
from markupsafe import Markup
from datetime import datetime
from setuptools._backport.hashlib._sha256 import sha256


def current_year():
  now = datetime.now()
  return now.strftime('%Y')

def icon(icon_name):
    return Markup('<i class="glyphicon glyphicon-%s"></i>' % icon_name)

def generate_authentication_token():
    return sha256(uuid.uuid1().hex).hexdigest()
