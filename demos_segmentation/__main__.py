#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""DEMOS Segmentation Service."""

import demos_segmentation

if __name__ == "__main__":
    app = demos_segmentation.create_app()
    app.run(host="0.0.0.0", port=5000)
