# -*- coding: utf-8 -*-
from flask import Blueprint
from flask_restx import Api

from .apis.namespace1 import ns as ns1
from .version import version

blueprint = Blueprint("apiv01", __name__)
api = Api(
    blueprint,
    title="DEMOS Segmentation API",
    version=version,
    description="Segment records.",
)

api.add_namespace(ns1)
