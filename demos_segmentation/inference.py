# -*- coding: utf-8 -*-
import attr


@attr.s(auto_attribs=True)
class BBox:
    x: float
    y: float
    width: float
    height: float


@attr.s(auto_attribs=True)
class Segment:
    id: str
    cls_id: str
    confidence: float
    bbox: BBox

