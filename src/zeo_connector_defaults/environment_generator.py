#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Interpreter version: python 2.7
#
# Imports =====================================================================
import shutil
import os.path
import tempfile
import threading
import subprocess
from string import Template


# Variables ===================================================================
SERV = None
TMP_DIR = None


# Functions & classes =========================================================
def data_context_name(fn):
    return os.path.join(os.path.dirname(__file__), "test_data", fn)


def data_context(fn, mode="r"):
    with open(data_context_name(fn), mode) as f:
        return f.read()


def tmp_context_name(fn):
    return os.path.join(TMP_DIR, fn)


def tmp_context(fn, mode="r"):
    with open(tmp_context_name(fn), mode) as f:
        return f.read()


# Environment generators ======================================================
def generate_environment():
    global TMP_DIR
    TMP_DIR = tempfile.mkdtemp()

    # write ZEO server config to  temp directory
    zeo_conf_path = os.path.join(TMP_DIR, "zeo.conf")
    with open(zeo_conf_path, "w") as f:
        f.write(
            Template(data_context("zeo.conf")).substitute(path=TMP_DIR)
        )

    # write client config to temp directory
    client_config_path = os.path.join(TMP_DIR, "zeo_client.conf")
    shutil.copy(data_context_name("zeo_client.conf"), client_config_path)

    # run the ZEO server
    def run_zeo():
        global SERV
        SERV = subprocess.Popen(["runzeo", "-C", zeo_conf_path])

    serv = threading.Thread(target=run_zeo)
    serv.setDaemon(True)
    serv.start()


def cleanup_environment():
    SERV.terminate()
    shutil.rmtree(TMP_DIR)