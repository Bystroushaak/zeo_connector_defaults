#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Interpreter version: python 2.7
#
# Imports =====================================================================
import os.path

import environment_generator


# Functions ===================================================================
def _in_path(fn, dirname="default_data"):
    dirname = os.path.dirname(__file__)
    return os.path.join(os.path.abspath(dirname), dirname, fn)


# Variables ===================================================================
SERVER_CONF_PATH = _in_path(fn="zeo.conf", dirname="default_data")
CLIENT_CONF_PATH = _in_path(fn="zeo_client.conf", dirname="default_data")

_SERVER_CONF_PATH = _in_path(fn="zeo.conf", dirname="template_data")
_CLIENT_CONF_PATH = _in_path(fn="zeo_client.conf", dirname="template_data")
