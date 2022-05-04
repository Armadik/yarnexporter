# -*- coding: utf-8 -*-
import sys
import logging
from logging import StreamHandler
from yarn_api_client import ResourceManager


def get_logger(mode_name):
    log = logging.getLogger(mode_name)
    log.setLevel(logging.DEBUG)
    handler = StreamHandler(stream=sys.stdout)
    fmt = logging.Formatter(fmt='%(asctime)s: %(message)s')
    handler.setFormatter(fmt)
    log.addHandler(handler)
    return log


log = get_logger(__name__)


def get_metrics_yarn(yarn_rm, timeout=180):
    rm = ResourceManager([yarn_rm], timeout=timeout)
    return rm
