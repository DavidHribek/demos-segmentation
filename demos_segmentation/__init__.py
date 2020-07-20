#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""DEMOS Segmentation Service."""

import os

from flask import Flask

from . import app_globals
from .apiv01 import blueprint as apiv01


def create_app():
    app = Flask(__name__)
    app.config.from_object(
        os.getenv("FLASK_CONFIG", "demos_segmentation.config.DevConfig")
    )
    app.register_blueprint(apiv01)
    return app
