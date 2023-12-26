from prometheus_client import start_http_server, Gauge
import psutil
import time

# Create gauges for CPU and memory usage
CPU_USAGE = Gauge('cpu_usage', 'CPU usage percentage')
MEMORY_USAGE = Gauge('memory_usage', 'Memory usage in bytes')


def collect_system_metrics():
    while True:
        CPU_USAGE.set(psutil.cpu_percent())
        MEMORY_USAGE.set(psutil.virtual_memory().used)
        time.sleep(1)  # Collect metrics every second


if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8001)

    # Start collecting system metrics
    collect_system_metrics()
