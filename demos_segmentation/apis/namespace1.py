# -*- coding: utf-8 -*-
"""REST APIv01."""

import logging

from flask import request
from flask_restx import Namespace, Resource, fields

from .. import app_globals
from ..utils import dispatch_query_img
from ..version import version

LOGGER = logging.getLogger(__name__)


ns = Namespace(
    "demos",
    version=version,
    title="DEMOS Segmentation",
    description="DEMOS Segmentation API",
)

query_img = ns.model(
    "Image Query",
    {
        "img_id": fields.String(
            description="Image identifier", required=True, example="00001"
        ),
        "data": fields.String(
            description="URI data scheme with Base64 encoded image",
            required=True,
            example="data:image/jpeg;base64,data",
        ),
        "model_id": fields.String(
            required=True, description="Inference Model ID", example="v1"
        ),
    },
)

response_detection = ns.model(
    "Detection representation",
    {
        "det_id": fields.Integer(description="Detection id", required=True, example=1),
        "y": fields.Float(description="Up coordinate", required=True, example=22.5),
        "x": fields.Float(description="Left coordinate", required=True, example=20.0),
        "height": fields.Float(
            description="Bounding box height", required=True, example=15.0
        ),
        "width": fields.Float(
            description="Bounding box width", required=True, example=28.25
        ),
        "cls_id": fields.Integer(
            description="Class identifier", required=True, example=1
        ),
        "det_score": fields.Float(
            description="Detection score", required=True, example=0.95
        ),
    },
)

response_img = ns.model(
    "Image Query Response",
    {
        "img_id": fields.String(
            description="Image identifier", required=True, example="00001"
        ),
        "model_id": fields.String(
            required=True, description="Inference model ID", example="v1"
        ),
        "detections": fields.List(fields.Nested(response_detection)),
    },
)


@ns.route("/")
class Api(Resource):
    @ns.doc("About DEMOS segmentation service")
    def get(self):
        """General info."""
        LOGGER.debug("Query on general info DEMOS API v01")
        return "DEMOS Segmentation API v01", 201


@ns.route("/img")
class ApiImg(Resource):
    """DEMOS segmentation."""

    @ns.doc("Query image")
    @ns.expect(query_img)
    @ns.marshal_with(response_img)
    def post(self):
        """Fetch given resource"""
        msg = dispatch_query_img(**request.get_json())
        LOGGER.debug("Query image %s", msg.img_id)
        LOGGER.debug(
            "Query image %s of shape: (%d, %d, %d)", msg.img_id, *msg.img.shape
        )

        return (
            {"img_id": msg.img_id, "model_id": msg.model_id, "detections": []},
            200,
        )
