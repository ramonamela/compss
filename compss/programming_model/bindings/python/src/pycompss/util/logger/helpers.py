#!/usr/bin/python
#
#  Copyright 2002-2019 Barcelona Supercomputing Center (www.bsc.es)
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#

# -*- coding: utf-8 -*-

"""
PyCOMPSs Util - logs
=====================
    This file contains all logging methods.
"""

import os
import logging
import json

from logging import config

CONFIG_FUNC = config.dictConfig


def init_logging(log_config_file, log_path):
    """
    Logging initialization.

    :param log_config_file: Log file name.
    :param log_path: Json log files path.
    :return: None
    """
    if os.path.exists(log_config_file):
        f = open(log_config_file, 'rt')
        conf = json.loads(f.read())
        f.close()
        if "error_file_handler" in conf["handlers"]:
            handler = "error_file_handler"
            errors_file = conf["handlers"][handler].get("filename")
            conf["handlers"][handler]["filename"] = log_path + errors_file
        if "error_file_handler" in conf["handlers"]:
            handler = "debug_file_handler"
            debug_file = conf["handlers"][handler].get("filename")
            conf["handlers"][handler]["filename"] = log_path + debug_file
        CONFIG_FUNC(conf)
    else:
        logging.basicConfig(level=logging.INFO)


def init_logging_worker(log_config_file):
    """
    Worker logging initialization.

    :param log_config_file: Log file name.
    :return: None
    """
    if os.path.exists(log_config_file):
        f = open(log_config_file, 'rt')
        conf = json.loads(f.read())
        f.close()
        CONFIG_FUNC(conf)
    else:
        logging.basicConfig(level=logging.INFO)
