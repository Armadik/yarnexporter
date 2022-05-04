# -*- coding: utf-8 -*-
from prometheus_client.metrics_core import GaugeMetricFamily, InfoMetricFamily
from .utils import get_metrics_yarn
from .utils import get_logger

log = get_logger(__name__)


class AppCollector(object):
    def __init__(self, yarn_rm):
        self.yarn_rm = yarn_rm

    def collect(self):
        log.debug("Get metrics clusterInfo.")
        mtk = get_metrics_yarn(self.yarn_rm)
        cluster_metrics = mtk.cluster_metrics().data['clusterMetrics']
        log.debug(cluster_metrics)

        metrics = GaugeMetricFamily(
            'yarn_exporter_cluster_metrics',
            'cluster_metrics from yarn gauge',
            labels=["cluster_metrics"])
        metrics.add_metric(["appsCompleted"], cluster_metrics.get("appsCompleted"))
        metrics.add_metric(["appsSubmitted"], cluster_metrics.get("appsSubmitted"))
        metrics.add_metric(["appsFailed"], cluster_metrics.get("appsFailed"))
        metrics.add_metric(["appsRunning"], cluster_metrics.get("appsRunning"))
        metrics.add_metric(["appsPending"], cluster_metrics.get("appsPending"))
        metrics.add_metric(["appsKilled"], cluster_metrics.get("appsKilled"))
        log.debug(metrics)

        yield metrics


