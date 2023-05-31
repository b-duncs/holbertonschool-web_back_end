#!/usr/bin/env python3
""" init file for views directory
"""
from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

from ...v1.views.index import *
from ...v1.views.users import *
from ...v1.views.session_auth import *


User.load_from_file()
