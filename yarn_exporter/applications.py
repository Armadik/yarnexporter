# -*- coding: utf-8 -*-
from prometheus_client.metrics_core import GaugeMetricFamily, InfoMetricFamily
from .utils import get_logger
from .utils import get_metrics_yarn

log = get_logger(__name__)


class CustomCollector(object):
    def __init__(self, yarn_rm):
        self.yarn_rm = yarn_rm

    def collect(self):

        log.debug("Get metrics apps.")
        mtk = get_metrics_yarn(self.yarn_rm)
        apps = mtk.cluster_applications(state="RUNNING").data['apps']
        log.debug(apps)

        metrics = GaugeMetricFamily(
            'yarn_exporter_app',
            'applications from yarn gauge',
            labels=["applications"])

        if apps.get('app'):
            for a in apps.get('app'):
                metrics.add_metric([a.get("id") + str("_cpu")], a.get("allocatedVCores"))
                metrics.add_metric([a.get("id") + str("_memory")], a.get("allocatedMB"))
                metrics.add_metric([a.get("id") + str("_runningContainers")], a.get("runningContainers"))


        log.debug(metrics)
        yield metrics

        c = InfoMetricFamily('yarn_exporter_app', 'applications from yarn info', labels=["app"])
        if apps.get('app'):
            for a in apps.get('app'):
                c.add_metric([a.get("id")], {'name': a.get("name"), 'user': a.get("user"), 'applicationType': a.get('applicationType')})
                log.debug(c)
        yield c
