# -*- coding: utf-8 -*-
"""Utilities of DEMOS Segmentation."""

import re
from base64 import b64decode, binascii
from typing import NamedTuple

import cv2
import numpy as np
from flask_restx import abort

from .exceptions import ImageEmptyException
from .messages import MSG_IMAGE_PROCESSING_ERROR, MSG_INCORRECT_DATA_FORMAT

__ALL__ = [
    "decode_image",
]

data_header_regex = re.compile(r"^data:([^,]+?)")


def decode_image(data) -> np.ndarray:
    """Decode base64 string to image (np.ndarray)

    Parameters
    ----------
    data : str
        Base64 encoded string

    Returns
    -------
    np.ndarray
        Decoded image

    """
    image_raw = np.frombuffer(b64decode(data), np.uint8)
    if image_raw.size == 0:
        raise ImageEmptyException()

    img = cv2.imdecode(image_raw, -1)
    if img is None:
        raise ImageEmptyException()

    return img


class ImgMsg(NamedTuple):
    """Image message from REST query.

    Attributes
    ----------
    img_id : str
        Image identifier
    img: np.ndarray
        Image data
    mode_id :str
        Model identifier
        
    """

    img_id: str
    img: np.ndarray
    model_id: str


def dispatch_query_img(img_id: str, data: str, model_id: str) -> ImgMsg:
    """Dispatch image request to ImgMsg with de-serialized image.

    Parameters
    ----------
    img_id : str
        Image identifier
    data : str
        URI data representing image
    model_id : str
        Model identifier

    Returns
    -------
    ImgMsg
        Message with image id, data, and image.

    """
    try:
        header, body = data.split(",", 1) if "," in data else (None, data)
        match = data_header_regex.match(header) if header is not None else True
        if not match:
            abort(
                400,
                message=MSG_INCORRECT_DATA_FORMAT,
                errors={"data": "data header is in a wrong format"},
            )
        img = decode_image(body)
        return ImgMsg(img_id=img_id, img=img, model_id=model_id)

    except binascii.Error:
        abort(
            400,
            message=MSG_IMAGE_PROCESSING_ERROR,
            errors={"data": "data is not in base64"},
        )

    except ImageEmptyException:
        abort(
            400, message=MSG_IMAGE_PROCESSING_ERROR, errors={"data": "image is empty"}
        )
