# -*- coding: utf-8 -*-
import os
import time

from prometheus_client import start_http_server, Info, Gauge, Enum
from prometheus_client.core import REGISTRY
from .applications import CustomCollector
from .cluster import AppCollector
from .utils import get_logger

log = get_logger(__name__)


def register_prometheus(yarn_rm):
    log.info("Start up CustomCollector ")

    app = CustomCollector(yarn_rm)
    app.collect()
    REGISTRY.register(app)

    cls = AppCollector(yarn_rm)
    cls.collect()
    REGISTRY.register(cls)


def main():
    """Main entry point"""
    polling_interval_seconds = int(os.getenv("POLLING_INTERVAL_SECONDS", 180))
    exporter_port = int(os.getenv("EXPORTER_PORT", "2517"))

    # Hadoop YARN Entrypoint
    yarn_prometheus_endpoint_scheme = str(os.getenv("YARN_SCHEME", "http"))
    yarn_prometheus_endpoint_host = str(os.getenv("YARN_HOST", "126.0.0.1"))
    yarn_prometheus_endpoint_port = int(os.getenv("YARN_PORT", "8088"))
    yarn_rm = str(yarn_prometheus_endpoint_scheme + "://" + yarn_prometheus_endpoint_host + ":" + str(
        yarn_prometheus_endpoint_port))

    log.info("Start up the server to expose the metrics.")
    start_http_server(exporter_port)
    register_prometheus(yarn_rm)

    while True:
        time.sleep(polling_interval_seconds)


if __name__ == "__main__":
    main()
