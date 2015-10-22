#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Interpreter version: python 2.7
#
# Imports =====================================================================
import os.path

import environment_generator


# Functions ===================================================================
def _in_path(fn):
    dirname = os.path.dirname(__file__)
    return os.path.join(os.path.abspath(dirname), "default_data", fn)


# Variables ===================================================================
SERVER_CONF_PATH = _in_path("zeo.conf")
CLIENT_CONF_PATH = _in_path("zeo_client.conf")
